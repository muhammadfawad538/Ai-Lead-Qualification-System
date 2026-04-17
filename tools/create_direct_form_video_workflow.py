#!/usr/bin/env python3
"""
Create Direct Google Form to Video Workflow
Triggers directly from Google Form webhook, not from sheets
"""

import json
import uuid

def create_direct_form_video_workflow():
    """Create workflow that triggers directly from Google Form"""

    workflow = {
        "name": "Direct Google Form to AI Video",
        "nodes": [],
        "connections": {},
        "active": False,
        "settings": {
            "executionOrder": "v1"
        },
        "meta": {
            "description": "Receives Google Form submissions directly via webhook, generates script with OpenAI, creates video with D-ID"
        }
    }

    # Node 1: Webhook Trigger (receives Google Form data)
    webhook_node = {
        "parameters": {
            "path": "video-form-submit",
            "httpMethod": "POST",
            "responseMode": "lastNode",
            "responseData": "={{ { \"success\": true, \"message\": \"Video generation started\", \"request_id\": $json.request_id } }}",
            "options": {}
        },
        "id": str(uuid.uuid4()),
        "name": "Form Webhook",
        "type": "n8n-nodes-base.webhook",
        "typeVersion": 2,
        "position": [240, 300],
        "webhookId": str(uuid.uuid4())
    }
    workflow["nodes"].append(webhook_node)

    # Node 2: Parse and Validate Form Data
    parse_form = {
        "parameters": {
            "jsCode": """// Parse Google Form webhook data
const input = $input.first().json;

// Google Forms sends data in body or query params
const formData = input.body || input.query || input;

// Generate unique request ID
const requestId = Date.now() + '-' + Math.random().toString(36).substr(2, 9);

// Extract form fields
const data = {
  request_id: requestId,
  product_name: formData.product_name || formData['entry.product_name'] || '',
  product_photo: formData.product_photo || formData['entry.product_photo'] || '',
  avatar_description: formData.avatar_description || formData['entry.avatar_description'] || '',
  product_features: formData.product_features || formData['entry.product_features'] || '',
  video_setting: formData.video_setting || formData['entry.video_setting'] || '',
  email: formData.email || formData['entry.email'] || '',
  timestamp: new Date().toISOString()
};

// Validate required fields
const required = ['product_name', 'avatar_description', 'product_features', 'video_setting'];
const missing = required.filter(field => !data[field]);

if (missing.length > 0) {
  throw new Error(`Missing required fields: ${missing.join(', ')}`);
}

return [{ json: data }];"""
        },
        "id": str(uuid.uuid4()),
        "name": "Parse Form Data",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [460, 300]
    }
    workflow["nodes"].append(parse_form)

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

    # Node 4: Extract Script
    extract_script = {
        "parameters": {
            "jsCode": """// Extract the generated script
const openaiResponse = $input.first().json;
const script = openaiResponse.choices?.[0]?.message?.content || openaiResponse.message?.content || '';

if (!script) {
  throw new Error('Failed to generate script from OpenAI');
}

const formData = $('Parse Form Data').first().json;

return [{
  json: {
    request_id: formData.request_id,
    generated_script: script.trim(),
    product_name: formData.product_name,
    product_photo: formData.product_photo,
    avatar_description: formData.avatar_description,
    video_setting: formData.video_setting,
    email: formData.email,
    timestamp: formData.timestamp
  }
}];"""
        },
        "id": str(uuid.uuid4()),
        "name": "Extract Script",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [900, 300]
    }
    workflow["nodes"].append(extract_script)

    # Node 5: Create Video with D-ID
    did_create = {
        "parameters": {
            "method": "POST",
            "url": "https://api.d-id.com/talks",
            "authentication": "genericCredentialType",
            "genericAuthType": "httpHeaderAuth",
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
            "specifyBody": "json",
            "jsonBody": "={{ {\n  \"script\": {\n    \"type\": \"text\",\n    \"input\": $json.generated_script,\n    \"provider\": {\n      \"type\": \"microsoft\",\n      \"voice_id\": \"en-US-JennyNeural\"\n    }\n  },\n  \"config\": {\n    \"fluent\": true,\n    \"pad_audio\": 0\n  },\n  \"source_url\": $json.product_photo || \"https://create-images-results.d-id.com/default_presenter.jpg\"\n} }}",
            "options": {}
        },
        "id": str(uuid.uuid4()),
        "name": "Create Video (D-ID)",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.2,
        "position": [1120, 300],
        "credentials": {
            "httpHeaderAuth": {
                "id": "2",
                "name": "D-ID API"
            }
        }
    }
    workflow["nodes"].append(did_create)

    # Node 6: Extract Talk ID
    extract_talk_id = {
        "parameters": {
            "jsCode": """// Extract talk ID from D-ID response
const response = $input.first().json;
const talkId = response.id;

if (!talkId) {
  throw new Error('No talk ID returned from D-ID API');
}

const scriptData = $('Extract Script').first().json;

return [{
  json: {
    request_id: scriptData.request_id,
    talk_id: talkId,
    status: response.status || 'created',
    product_name: scriptData.product_name,
    generated_script: scriptData.generated_script,
    email: scriptData.email,
    created_at: new Date().toISOString()
  }
}];"""
        },
        "id": str(uuid.uuid4()),
        "name": "Extract Talk ID",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [1340, 300]
    }
    workflow["nodes"].append(extract_talk_id)

    # Node 7: Wait
    wait_node = {
        "parameters": {
            "amount": 20,
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
    check_status = {
        "parameters": {
            "method": "GET",
            "url": "=https://api.d-id.com/talks/{{ $json.talk_id }}",
            "authentication": "genericCredentialType",
            "genericAuthType": "httpHeaderAuth",
            "options": {}
        },
        "id": str(uuid.uuid4()),
        "name": "Check Video Status",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.2,
        "position": [1780, 300],
        "credentials": {
            "httpHeaderAuth": {
                "id": "2",
                "name": "D-ID API"
            }
        }
    }
    workflow["nodes"].append(check_status)

    # Node 9: Is Complete?
    if_complete = {
        "parameters": {
            "conditions": {
                "string": [
                    {
                        "value1": "={{ $json.status }}",
                        "operation": "equals",
                        "value2": "done"
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
    workflow["nodes"].append(if_complete)

    # Node 10: Send Email with Video (True branch)
    send_email = {
        "parameters": {
            "fromEmail": "noreply@yourdomain.com",
            "toEmail": "={{ $('Extract Talk ID').first().json.email }}",
            "subject": "=Your AI Video is Ready - {{ $('Extract Talk ID').first().json.product_name }}",
            "emailType": "html",
            "message": "=<h2>Your AI Video is Ready!</h2>\n\n<p>Hi there,</p>\n\n<p>Your UGC-style video for <strong>{{ $('Extract Talk ID').first().json.product_name }}</strong> has been generated successfully!</p>\n\n<p><strong>Video URL:</strong><br>\n<a href=\"{{ $json.result_url }}\">{{ $json.result_url }}</a></p>\n\n<p><strong>Generated Script:</strong><br>\n{{ $('Extract Talk ID').first().json.generated_script }}</p>\n\n<p><strong>Request ID:</strong> {{ $('Extract Talk ID').first().json.request_id }}</p>\n\n<p>Thanks for using our AI Video Generator!</p>",
            "options": {}
        },
        "id": str(uuid.uuid4()),
        "name": "Send Email with Video",
        "type": "n8n-nodes-base.emailSend",
        "typeVersion": 2.1,
        "position": [2220, 200],
        "credentials": {
            "smtp": {
                "id": "3",
                "name": "SMTP account"
            }
        },
        "notes": "Optional: Configure SMTP to send email notifications"
    }
    workflow["nodes"].append(send_email)

    # Node 11: Still Processing - Loop Back
    loop_back = {
        "parameters": {
            "jsCode": """// Check timeout (max 3 minutes for D-ID)
const startTime = $('Extract Talk ID').first().json.created_at;
const elapsed = Date.now() - new Date(startTime).getTime();
const maxWait = 3 * 60 * 1000; // 3 minutes

if (elapsed > maxWait) {
  throw new Error('Video generation timeout - exceeded 3 minutes');
}

// Pass data back
return [{
  json: {
    request_id: $('Extract Talk ID').first().json.request_id,
    talk_id: $('Extract Talk ID').first().json.talk_id,
    status: 'processing',
    product_name: $('Extract Talk ID').first().json.product_name,
    generated_script: $('Extract Talk ID').first().json.generated_script,
    email: $('Extract Talk ID').first().json.email,
    created_at: $('Extract Talk ID').first().json.created_at
  }
}];"""
        },
        "id": str(uuid.uuid4()),
        "name": "Still Processing",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [2220, 400]
    }
    workflow["nodes"].append(loop_back)

    # Create connections
    workflow["connections"] = {
        "Form Webhook": {
            "main": [[{"node": "Parse Form Data", "type": "main", "index": 0}]]
        },
        "Parse Form Data": {
            "main": [[{"node": "Generate Script (OpenAI)", "type": "main", "index": 0}]]
        },
        "Generate Script (OpenAI)": {
            "main": [[{"node": "Extract Script", "type": "main", "index": 0}]]
        },
        "Extract Script": {
            "main": [[{"node": "Create Video (D-ID)", "type": "main", "index": 0}]]
        },
        "Create Video (D-ID)": {
            "main": [[{"node": "Extract Talk ID", "type": "main", "index": 0}]]
        },
        "Extract Talk ID": {
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
                [{"node": "Send Email with Video", "type": "main", "index": 0}],
                [{"node": "Still Processing", "type": "main", "index": 0}]
            ]
        },
        "Still Processing": {
            "main": [[{"node": "Wait", "type": "main", "index": 0}]]
        }
    }

    return workflow

if __name__ == "__main__":
    workflow = create_direct_form_video_workflow()

    output_path = ".tmp/direct_form_video_workflow.json"
    with open(output_path, 'w') as f:
        json.dump(workflow, f, indent=2)

    print(f"Workflow created: {output_path}")
    print("\nThis workflow:")
    print("- Receives Google Form data directly via webhook")
    print("- No Google Sheets needed!")
    print("- Generates script with OpenAI")
    print("- Creates video with D-ID")
    print("- Sends email with video URL when complete")
