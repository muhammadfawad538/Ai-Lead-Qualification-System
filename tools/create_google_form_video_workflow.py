#!/usr/bin/env python3
"""
Create Google Form to Video Workflow
Receives data from Google Form, generates script with OpenAI, creates video with D-ID
"""

import json
import uuid

def create_google_form_video_workflow():
    """Create the complete workflow JSON"""

    workflow = {
        "name": "Google Form to AI Video Generator",
        "nodes": [],
        "connections": {},
        "active": False,
        "settings": {
            "executionOrder": "v1"
        },
        "meta": {
            "description": "Receives Google Form submissions, generates UGC script with OpenAI, creates video with D-ID"
        }
    }

    # Node 1: Google Sheets Trigger (watches for new form responses)
    sheets_trigger = {
        "parameters": {
            "operation": "appendOrUpdate",
            "documentId": {
                "__rl": True,
                "value": "",
                "mode": "list",
                "cachedResultName": ""
            },
            "sheetName": {
                "__rl": True,
                "value": "gid=0",
                "mode": "list",
                "cachedResultName": "Sheet1"
            },
            "columns": {
                "mappingMode": "autoMapInputData",
                "value": {},
                "matchingColumns": [],
                "schema": []
            },
            "options": {}
        },
        "id": str(uuid.uuid4()),
        "name": "Google Sheets Trigger",
        "type": "n8n-nodes-base.googleSheetsTrigger",
        "typeVersion": 1,
        "position": [240, 300],
        "credentials": {
            "googleSheetsOAuth2Api": {
                "id": "1",
                "name": "Google Sheets account"
            }
        },
        "notes": "Triggers when a new row is added to the Google Form responses sheet"
    }
    workflow["nodes"].append(sheets_trigger)

    # Node 2: Extract Form Data
    extract_data = {
        "parameters": {
            "jsCode": """// Extract data from Google Form response
const input = $input.first().json;

// Map Google Form columns to our fields
// Adjust these column names to match your actual Google Form
const data = {
  product_name: input['Product Name'] || input.product_name || '',
  product_photo: input['Product Photo URL'] || input.product_photo || '',
  avatar_description: input['Avatar Description'] || input.avatar_description || '',
  product_features: input['Product Features'] || input.product_features || '',
  video_setting: input['Video Setting'] || input.video_setting || '',
  timestamp: input.Timestamp || new Date().toISOString(),
  row_number: input.__rowNumber || 0
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
        "name": "Extract Form Data",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [460, 300]
    }
    workflow["nodes"].append(extract_data)

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
                "id": "2",
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

const formData = $('Extract Form Data').first().json;

return [{
  json: {
    generated_script: script.trim(),
    product_name: formData.product_name,
    product_photo: formData.product_photo,
    avatar_description: formData.avatar_description,
    video_setting: formData.video_setting,
    row_number: formData.row_number
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

    # Node 6: Extract Talk ID
    extract_talk_id = {
        "parameters": {
            "jsCode": """// Extract talk ID from D-ID response
const response = $input.first().json;
const talkId = response.id;

if (!talkId) {
  throw new Error('No talk ID returned from D-ID API');
}

return [{
  json: {
    talk_id: talkId,
    status: response.status || 'created',
    product_name: $('Extract Script').first().json.product_name,
    generated_script: $('Extract Script').first().json.generated_script,
    row_number: $('Extract Script').first().json.row_number
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
                "id": "3",
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

    # Node 10: Update Google Sheet with Video URL
    update_sheet = {
        "parameters": {
            "operation": "update",
            "documentId": {
                "__rl": True,
                "value": "",
                "mode": "list",
                "cachedResultName": ""
            },
            "sheetName": {
                "__rl": True,
                "value": "gid=0",
                "mode": "list",
                "cachedResultName": "Sheet1"
            },
            "columns": {
                "mappingMode": "defineBelow",
                "value": {
                    "Video URL": "={{ $json.result_url }}",
                    "Status": "=Completed",
                    "Completed At": "={{ new Date().toISOString() }}"
                },
                "matchingColumns": ["Row Number"],
                "schema": []
            },
            "options": {}
        },
        "id": str(uuid.uuid4()),
        "name": "Update Sheet with Video",
        "type": "n8n-nodes-base.googleSheets",
        "typeVersion": 4.4,
        "position": [2220, 200],
        "credentials": {
            "googleSheetsOAuth2Api": {
                "id": "1",
                "name": "Google Sheets account"
            }
        }
    }
    workflow["nodes"].append(update_sheet)

    # Node 11: Still Processing - Loop Back
    loop_back = {
        "parameters": {
            "jsCode": """// Check timeout (max 3 minutes for D-ID)
const startTime = $('Extract Talk ID').first().json.timestamp || Date.now();
const elapsed = Date.now() - new Date(startTime).getTime();
const maxWait = 3 * 60 * 1000; // 3 minutes

if (elapsed > maxWait) {
  throw new Error('Video generation timeout - exceeded 3 minutes');
}

// Pass data back
return [{
  json: {
    talk_id: $('Extract Talk ID').first().json.talk_id,
    status: 'processing',
    product_name: $('Extract Talk ID').first().json.product_name,
    generated_script: $('Extract Talk ID').first().json.generated_script,
    row_number: $('Extract Talk ID').first().json.row_number
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
        "Google Sheets Trigger": {
            "main": [[{"node": "Extract Form Data", "type": "main", "index": 0}]]
        },
        "Extract Form Data": {
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
                [{"node": "Update Sheet with Video", "type": "main", "index": 0}],
                [{"node": "Still Processing", "type": "main", "index": 0}]
            ]
        },
        "Still Processing": {
            "main": [[{"node": "Wait", "type": "main", "index": 0}]]
        }
    }

    return workflow

if __name__ == "__main__":
    workflow = create_google_form_video_workflow()

    output_path = ".tmp/google_form_video_workflow.json"
    with open(output_path, 'w') as f:
        json.dump(workflow, f, indent=2)

    print(f"Workflow created: {output_path}")
    print("\nThis workflow:")
    print("- Watches Google Form responses in Google Sheets")
    print("- Generates UGC script with OpenAI GPT-4o")
    print("- Creates video with D-ID API")
    print("- Updates the sheet with video URL when complete")
