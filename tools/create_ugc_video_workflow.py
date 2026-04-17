#!/usr/bin/env python3
"""
Create AI UGC Video Ad Generator Workflow
Builds an n8n workflow that generates UGC-style video ads using AI
"""

import json
import uuid

def create_ugc_video_workflow():
    """Create the complete workflow JSON"""

    workflow = {
        "name": "AI UGC Video Ad Generator",
        "nodes": [],
        "connections": {},
        "active": False,
        "settings": {
            "executionOrder": "v1"
        },
        "meta": {
            "description": "Receives product info via webhook, generates UGC script with OpenAI, creates video with AI video API"
        }
    }

    # Node 1: Webhook Trigger
    webhook_node = {
        "parameters": {
            "path": "ugc-video-generator",
            "httpMethod": "POST",
            "responseMode": "onReceived",
            "options": {}
        },
        "id": str(uuid.uuid4()),
        "name": "Webhook",
        "type": "n8n-nodes-base.webhook",
        "typeVersion": 2,
        "position": [240, 300],
        "webhookId": str(uuid.uuid4())
    }
    workflow["nodes"].append(webhook_node)

    # Node 2: Extract and Validate Input
    validate_node = {
        "parameters": {
            "jsCode": """// Extract webhook data
const input = $input.first().json.body || $input.first().json;

// Validate required fields
const required = ['product_name', 'product_photo', 'avatar_description', 'product_features', 'video_setting'];
const missing = required.filter(field => !input[field]);

if (missing.length > 0) {
  throw new Error(`Missing required fields: ${missing.join(', ')}`);
}

// Return validated data
return [{
  json: {
    product_name: input.product_name,
    product_photo: input.product_photo,
    avatar_description: input.avatar_description,
    product_features: input.product_features,
    video_setting: input.video_setting,
    timestamp: new Date().toISOString()
  }
}];"""
        },
        "id": str(uuid.uuid4()),
        "name": "Validate Input",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [460, 300]
    }
    workflow["nodes"].append(validate_node)

    # Node 3: Generate Script with OpenAI
    openai_node = {
        "parameters": {
            "resource": "text",
            "operation": "message",
            "modelId": "gpt-4o",
            "messages": {
                "values": [
                    {
                        "role": "system",
                        "content": "You are a UGC video script writer. Create authentic, conversational 15-second scripts for user-generated content style ads. Keep it natural and relatable."
                    },
                    {
                        "role": "user",
                        "content": "=Create a 15-second UGC-style video script for:\n\nProduct: {{ $json.product_name }}\nFeatures: {{ $json.product_features }}\nSetting: {{ $json.video_setting }}\nAvatar: {{ $json.avatar_description }}\n\nMake it authentic and conversational. The script should feel like a real person sharing their experience."
                    }
                ]
            },
            "options": {
                "temperature": 0.8,
                "maxTokens": 200
            }
        },
        "id": str(uuid.uuid4()),
        "name": "Generate Script (OpenAI)",
        "type": "@n8n/n8n-nodes-langchain.openAi",
        "typeVersion": 1.3,
        "position": [680, 300],
        "credentials": {
            "openAiApi": {
                "id": "1",
                "name": "OpenAI API"
            }
        }
    }
    workflow["nodes"].append(openai_node)

    # Node 4: Extract Script from OpenAI Response
    extract_script_node = {
        "parameters": {
            "jsCode": """// Extract the generated script from OpenAI response
const openaiResponse = $input.first().json;
const script = openaiResponse.choices?.[0]?.message?.content || openaiResponse.message?.content || '';

if (!script) {
  throw new Error('Failed to generate script from OpenAI');
}

// Pass through all data plus the script
return [{
  json: {
    ...openaiResponse,
    generated_script: script.trim(),
    product_name: $('Validate Input').first().json.product_name,
    product_photo: $('Validate Input').first().json.product_photo,
    avatar_description: $('Validate Input').first().json.avatar_description,
    video_setting: $('Validate Input').first().json.video_setting
  }
}];"""
        },
        "id": str(uuid.uuid4()),
        "name": "Extract Script",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [900, 300]
    }
    workflow["nodes"].append(extract_script_node)

    # Node 5: Call AI Video API (HeyGen/D-ID/Tavus)
    video_api_node = {
        "parameters": {
            "method": "POST",
            "url": "https://api.heygen.com/v2/video/generate",
            "authentication": "predefinedCredentialType",
            "nodeCredentialType": "heyGenApi",
            "sendHeaders": True,
            "headerParameters": {
                "parameters": [
                    {
                        "name": "Content-Type",
                        "value": "application/json"
                    }
                ]
            },
            "sendBody": True,
            "bodyParameters": {
                "parameters": [
                    {
                        "name": "video_inputs",
                        "value": "={{ [{\"character\": {\"type\": \"avatar\", \"avatar_id\": \"default\"}, \"voice\": {\"type\": \"text\", \"input_text\": $json.generated_script}, \"background\": {\"type\": \"color\", \"value\": \"#ffffff\"}}] }}"
                    },
                    {
                        "name": "dimension",
                        "value": "={{ {\"width\": 1080, \"height\": 1920} }}"
                    },
                    {
                        "name": "test",
                        "value": "={{ false }}"
                    }
                ]
            },
            "options": {}
        },
        "id": str(uuid.uuid4()),
        "name": "Generate Video (HeyGen)",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.2,
        "position": [1120, 300],
        "credentials": {
            "heyGenApi": {
                "id": "2",
                "name": "HeyGen API"
            }
        },
        "notes": "Replace with your preferred AI video API (HeyGen, D-ID, Tavus, etc.)"
    }
    workflow["nodes"].append(video_api_node)

    # Node 6: Extract Video Job ID
    extract_job_node = {
        "parameters": {
            "jsCode": """// Extract job/video ID from API response
const response = $input.first().json;

// Handle different API response formats
const videoId = response.data?.video_id || response.video_id || response.id || response.data?.id;
const status = response.data?.status || response.status || 'pending';

if (!videoId) {
  throw new Error('No video ID returned from API');
}

return [{
  json: {
    video_id: videoId,
    status: status,
    api_response: response,
    product_name: $('Extract Script').first().json.product_name,
    generated_script: $('Extract Script').first().json.generated_script
  }
}];"""
        },
        "id": str(uuid.uuid4()),
        "name": "Extract Video Job ID",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [1340, 300]
    }
    workflow["nodes"].append(extract_job_node)

    # Node 7: Wait for Video Processing
    wait_node = {
        "parameters": {
            "amount": 30,
            "unit": "seconds"
        },
        "id": str(uuid.uuid4()),
        "name": "Wait",
        "type": "n8n-nodes-base.wait",
        "typeVersion": 1.1,
        "position": [1560, 300],
        "webhookId": str(uuid.uuid4())
    }
    workflow["nodes"].append(wait_node)

    # Node 8: Check Video Status
    check_status_node = {
        "parameters": {
            "method": "GET",
            "url": "=https://api.heygen.com/v1/video_status.get?video_id={{ $json.video_id }}",
            "authentication": "predefinedCredentialType",
            "nodeCredentialType": "heyGenApi",
            "options": {}
        },
        "id": str(uuid.uuid4()),
        "name": "Check Video Status",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.2,
        "position": [1780, 300],
        "credentials": {
            "heyGenApi": {
                "id": "2",
                "name": "HeyGen API"
            }
        }
    }
    workflow["nodes"].append(check_status_node)

    # Node 9: Check if Complete
    if_complete_node = {
        "parameters": {
            "conditions": {
                "string": [
                    {
                        "value1": "={{ $json.data.status || $json.status }}",
                        "operation": "equals",
                        "value2": "completed"
                    }
                ]
            }
        },
        "id": str(uuid.uuid4()),
        "name": "Is Complete?",
        "type": "n8n-nodes-base.if",
        "typeVersion": 2,
        "position": [2000, 300]
    }
    workflow["nodes"].append(if_complete_node)

    # Node 10: Return Video URL (True branch)
    return_video_node = {
        "parameters": {
            "jsCode": """// Extract final video URL
const response = $input.first().json;
const videoUrl = response.data?.video_url || response.video_url || response.data?.url;

return [{
  json: {
    success: true,
    video_url: videoUrl,
    video_id: $('Extract Video Job ID').first().json.video_id,
    product_name: $('Extract Video Job ID').first().json.product_name,
    script: $('Extract Video Job ID').first().json.generated_script,
    status: 'completed',
    completed_at: new Date().toISOString()
  }
}];"""
        },
        "id": str(uuid.uuid4()),
        "name": "Return Video URL",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [2220, 200]
    }
    workflow["nodes"].append(return_video_node)

    # Node 11: Loop Back to Wait (False branch)
    loop_back_node = {
        "parameters": {
            "jsCode": """// Check if we've waited too long (max 5 minutes)
const startTime = $('Extract Video Job ID').first().json.api_response?.created_at || Date.now();
const elapsed = Date.now() - new Date(startTime).getTime();
const maxWait = 5 * 60 * 1000; // 5 minutes

if (elapsed > maxWait) {
  throw new Error('Video generation timeout - exceeded 5 minutes');
}

// Pass data back to wait node
return [{
  json: {
    video_id: $('Extract Video Job ID').first().json.video_id,
    status: 'processing',
    product_name: $('Extract Video Job ID').first().json.product_name,
    generated_script: $('Extract Video Job ID').first().json.generated_script
  }
}];"""
        },
        "id": str(uuid.uuid4()),
        "name": "Still Processing",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [2220, 400]
    }
    workflow["nodes"].append(loop_back_node)

    # Create connections
    workflow["connections"] = {
        "Webhook": {
            "main": [[{"node": "Validate Input", "type": "main", "index": 0}]]
        },
        "Validate Input": {
            "main": [[{"node": "Generate Script (OpenAI)", "type": "main", "index": 0}]]
        },
        "Generate Script (OpenAI)": {
            "main": [[{"node": "Extract Script", "type": "main", "index": 0}]]
        },
        "Extract Script": {
            "main": [[{"node": "Generate Video (HeyGen)", "type": "main", "index": 0}]]
        },
        "Generate Video (HeyGen)": {
            "main": [[{"node": "Extract Video Job ID", "type": "main", "index": 0}]]
        },
        "Extract Video Job ID": {
            "main": [[{"node": "Wait", "type": "main", "index": 0}]]
        },
        "Wait": {
            "main": [[{"node": "Check Video Status", "type": "main", "index": 0}]]
        },
        "Check Video Status": {
            "main": [[{"node": "Is Complete?", "type": "main", "index": 0}]]
        },
        "Is Complete?": {
            "main": [
                [{"node": "Return Video URL", "type": "main", "index": 0}],
                [{"node": "Still Processing", "type": "main", "index": 0}]
            ]
        },
        "Still Processing": {
            "main": [[{"node": "Wait", "type": "main", "index": 0}]]
        }
    }

    return workflow

if __name__ == "__main__":
    workflow = create_ugc_video_workflow()

    output_path = ".tmp/ugc_video_workflow.json"
    with open(output_path, 'w') as f:
        json.dump(workflow, f, indent=2)

    print(f"Workflow created: {output_path}")
    print("\nNext Steps:")
    print("1. Go to your n8n instance: https://pakfawad.app.n8n.cloud")
    print("2. Click 'Add workflow' -> 'Import from File'")
    print("3. Upload the generated JSON file")
    print("4. Configure credentials:")
    print("   - OpenAI API key")
    print("   - HeyGen API key (or replace with D-ID/Tavus)")
    print("5. Activate the workflow")
    print("\nWebhook URL will be:")
    print("   https://pakfawad.app.n8n.cloud/webhook/ugc-video-generator")
