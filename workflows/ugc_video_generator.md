# AI UGC Video Ad Generator Workflow

## Overview
This workflow generates UGC-style video ads using AI. It receives product information via webhook, generates a script with OpenAI, and creates a video using an AI video API.

## Workflow File
- **Location**: `.tmp/ugc_video_workflow.json`
- **Created**: 2026-04-14

## How to Import

1. Go to https://pakfawad.app.n8n.cloud
2. Click **"Add workflow"** → **"Import from File"**
3. Upload `.tmp/ugc_video_workflow.json`
4. Configure credentials (see below)
5. Activate the workflow

## Workflow Structure

### Nodes:
1. **Webhook** - Receives POST requests at `/ugc-video-generator`
2. **Validate Input** - Checks required fields
3. **Generate Script (OpenAI)** - Creates 15-second UGC script using GPT-4o
4. **Extract Script** - Parses OpenAI response
5. **Generate Video (HeyGen)** - Calls AI video API
6. **Extract Video Job ID** - Gets job ID from API response
7. **Wait** - Waits 30 seconds for processing
8. **Check Video Status** - Polls video generation status
9. **Is Complete?** - Checks if video is ready
10. **Return Video URL** - Returns completed video (true branch)
11. **Still Processing** - Loops back to wait (false branch, max 5 min)

## Required Credentials

### OpenAI API
- Get key from: https://platform.openai.com/api-keys
- Add in n8n: Credentials → OpenAI API

### HeyGen API (or alternative)
- **HeyGen**: https://app.heygen.com/settings/api
- **D-ID**: https://studio.d-id.com/account-settings
- **Tavus**: https://platform.tavus.io/api-keys

If using D-ID or Tavus, update the HTTP Request nodes with their API endpoints.

## Input Format

Send POST request to webhook with:

```json
{
  "product_name": "Cologne",
  "product_photo": "https://example.com/product.jpg",
  "avatar_description": "Young adult male",
  "product_features": "clean scent, not too strong",
  "video_setting": "In a kitchen, getting ready to head out"
}
```

## Output Format

```json
{
  "success": true,
  "video_url": "https://...",
  "video_id": "...",
  "product_name": "Cologne",
  "script": "Generated script text...",
  "status": "completed",
  "completed_at": "2026-04-14T16:36:00.000Z"
}
```

## Customization Options

### Change Video API
Replace the "Generate Video (HeyGen)" node with your preferred provider:
- Update the URL
- Modify the request body format
- Update credentials

### Adjust Script Length
Modify the OpenAI prompt in "Generate Script (OpenAI)" node to change duration.

### Change Wait Time
Adjust the "Wait" node duration (default: 30 seconds).

### Timeout Settings
Maximum wait time is 5 minutes. Modify in "Still Processing" node.

## Testing

1. Use a tool like Postman or curl:
```bash
curl -X POST https://pakfawad.app.n8n.cloud/webhook/ugc-video-generator \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "Test Product",
    "product_photo": "https://example.com/photo.jpg",
    "avatar_description": "Young adult",
    "product_features": "amazing features",
    "video_setting": "Modern office"
  }'
```

2. Check n8n execution logs for any errors
3. Verify credentials are properly configured

## Troubleshooting

- **"Missing required fields"**: Ensure all 5 input fields are provided
- **OpenAI errors**: Check API key and quota
- **Video API errors**: Verify API key and endpoint URL
- **Timeout**: Video generation may take 3-5 minutes depending on API

## Notes

- The workflow uses async polling with a loop-back mechanism
- Maximum processing time: 5 minutes
- Script generation uses GPT-4o with temperature 0.8 for creativity
- Video dimensions: 1080x1920 (vertical/portrait for social media)
