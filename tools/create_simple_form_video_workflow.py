#!/usr/bin/env python3
"""
Simple Google Form to Video Workflow
Uses Google Forms trigger (no Apps Script needed) and Gemini (free)
"""

import json
import uuid

def create_simple_form_video_workflow():
    """Create the simplest possible workflow"""

    workflow = {
        "name": "Simple Form to AI Video (Gemini Free)",
        "nodes": [],
        "connections": {},
        "active": False,
        "settings": {
            "executionOrder": "v1"
        },
        "meta": {
            "description": "Simple workflow: Google Form → Gemini (free) → D-ID video"
        }
    }

    # Node 1: Google Forms Trigger
    form_trigger = {
        "parameters": {
            "formId": {
                "__rl": True,
                "value": "",
                "mode": "list",
                "cachedResultName": ""
            },
            "triggerOn": "formSubmit"
        },
        "id": str(uuid.uuid4()),
        "name": "Google Form Trigger",
        "type": "n8n-nodes-base.googleFormsTrigger",
        "typeVersion": 1,
        "position": [240, 300],
        "webhookId": str(uuid.uuid4()),
        "credentials": {
            "googleFormsOAuth2Api": {
                "id": "1",
                "name": "Google Forms account"
            }
        },
        "notes": "Triggers automatically when form is submitted - no Apps Script needed!"
    }
    workflow["nodes"].append(form_trigger)

    # Node 2: Extract Form Data
    extract_data = {
        "parameters": {
            "jsCode": """// Extract form responses
const responses = $input.first().json.responses || {};

return [{
  json: {
    product_name: responses.product_name || responses['Product Name'] || '',
    product_photo: responses.product_photo || responses['Product Photo URL'] || '',
    avatar_description: responses.avatar_description || responses['Avatar Description'] || '',
    product_features: responses.product_features || responses['Product Features'] || '',
    video_setting: responses.video_setting || responses['Video Setting'] || '',
    email: responses.email || responses['Email'] || '',
    timestamp: new Date().toISOString()
  }
}];"""
        },
        "id": str(uuid.uuid4()),
        "name": "Extract Data",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [460, 300]
    }
    workflow["nodes"].append(extract_data)

    # Node 3: Generate Script with Gemini (FREE)
    gemini_node = {
        "parameters": {
            "method": "POST",
            "url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
            "authentication": "genericCredentialType",
            "genericAuthType": "queryAuth",
            "sendBody": True,
            "specifyBody": "json",
            "jsonBody": "={{ {\n  \"contents\": [{\n    \"parts\": [{\n      \"text\": \"You are a UGC video script writer. Create an authentic, conversational 15-second script for a user-generated content style ad.\\n\\nProduct: \" + $json.product_name + \"\\nFeatures: \" + $json.product_features + \"\\nSetting: \" + $json.video_setting + \"\\nAvatar: \" + $json.avatar_description + \"\\n\\nMake it natural and relatable. The script should feel like a real person sharing their experience. Return ONLY the script text, nothing else.\"\n    }]\n  }]\n} }}",
            "options": {}
        },
        "id": str(uuid.uuid4()),
        "name": "Generate Script (Gemini FREE)",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.2,
        "position": [680, 300],
        "credentials": {
            "httpQueryAuth": {
                "id": "2",
                "name": "Gemini API"
            }
        },
        "notes": "Uses Google Gemini - completely FREE!"
    }
    workflow["nodes"].append(gemini_node)

    # Node 4: Extract Script from Gemini
    extract_script = {
        "parameters": {
            "jsCode": """// Extract script from Gemini response
const response = $input.first().json;
const script = response.candidates?.[0]?.content?.parts?.[0]?.text || '';

if (!script) {
  throw new Error('Failed to generate script from Gemini');
}

const formData = $('Extract Data').first().json;

return [{
  json: {
    generated_script: script.trim(),
    product_name: formData.product_name,
    product_photo: formData.product_photo,
    email: formData.email
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
                "id": "3",
                "name": "D-ID API"
            }
        }
    }
    workflow["nodes"].append(did_create)

    # Node 6: Extract Video ID
    extract_id = {
        "parameters": {
            "jsCode": """const response = $input.first().json;
const videoId = response.id;

if (!videoId) {
  throw new Error('No video ID returned');
}

return [{
  json: {
    video_id: videoId,
    status: response.status || 'created',
    script: $('Extract Script').first().json.generated_script,
    product_name: $('Extract Script').first().json.product_name,
    email: $('Extract Script').first().json.email
  }
}];"""
        },
        "id": str(uuid.uuid4()),
        "name": "Extract Video ID",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [1340, 300]
    }
    workflow["nodes"].append(extract_id)

    # Node 7: Wait
    wait_node = {
        "parameters": {
            "amount": 30,
            "unit": "seconds"
        },
        "id": str(uuid.uuid4()),
        "name": "Wait 30s",
        "type": "n8n-nodes-base.wait",
        "typeVersion": 1.1,
        "position": [1560, 300],
        "webhookId": str(uuid.uuid4())
    }
    workflow["nodes"].append(wait_node)

    # Node 8: Get Video URL
    get_video = {
        "parameters": {
            "method": "GET",
            "url": "=https://api.d-id.com/talks/{{ $json.video_id }}",
            "authentication": "genericCredentialType",
            "genericAuthType": "httpHeaderAuth",
            "options": {}
        },
        "id": str(uuid.uuid4()),
        "name": "Get Video URL",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.2,
        "position": [1780, 300],
        "credentials": {
            "httpHeaderAuth": {
                "id": "3",
                "name": "D-ID API"
            }
        }
    }
    workflow["nodes"].append(get_video)

    # Node 9: Show Result
    show_result = {
        "parameters": {
            "jsCode": """const response = $input.first().json;
const videoUrl = response.result_url || 'Processing...';
const status = response.status;

return [{
  json: {
    status: status,
    video_url: videoUrl,
    product_name: $('Extract Video ID').first().json.product_name,
    script: $('Extract Video ID').first().json.script,
    message: status === 'done' ? 'Video ready!' : 'Still processing, check back in 1 minute'
  }
}];"""
        },
        "id": str(uuid.uuid4()),
        "name": "Show Result",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [2000, 300]
    }
    workflow["nodes"].append(show_result)

    # Create connections
    workflow["connections"] = {
        "Google Form Trigger": {
            "main": [[{"node": "Extract Data", "type": "main", "index": 0}]]
        },
        "Extract Data": {
            "main": [[{"node": "Generate Script (Gemini FREE)", "type": "main", "index": 0}]]
        },
        "Generate Script (Gemini FREE)": {
            "main": [[{"node": "Extract Script", "type": "main", "index": 0}]]
        },
        "Extract Script": {
            "main": [[{"node": "Create Video (D-ID)", "type": "main", "index": 0}]]
        },
        "Create Video (D-ID)": {
            "main": [[{"node": "Extract Video ID", "type": "main", "index": 0}]]
        },
        "Extract Video ID": {
            "main": [[{"node": "Wait 30s", "type": "main", "index": 0}]]
        },
        "Wait 30s": {
            "main": [[{"node": "Get Video URL", "type": "main", "index": 0}]]
        },
        "Get Video URL": {
            "main": [[{"node": "Show Result", "type": "main", "index": 0}]]
        }
    }

    return workflow

if __name__ == "__main__":
    workflow = create_simple_form_video_workflow()

    output_path = ".tmp/simple_form_video_workflow.json"
    with open(output_path, 'w') as f:
        json.dump(workflow, f, indent=2)

    print(f"Workflow created: {output_path}")
    print("\nSIMPLE VERSION:")
    print("- Google Form trigger (built-in, no Apps Script!)")
    print("- Gemini for script (FREE)")
    print("- D-ID for video (20 free credits/month)")
    print("- Total cost: FREE for first 10 videos/month!")
