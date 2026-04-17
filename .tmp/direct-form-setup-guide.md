# Direct Google Form to n8n Webhook Setup Guide

## Overview
This workflow receives Google Form submissions directly via webhook (no Google Sheets needed!). When someone submits the form, it instantly triggers your n8n workflow.

---

## Step 1: Import Workflow to n8n

1. Go to https://pakfawad.app.n8n.cloud
2. Click **"Add workflow"** → **"Import from File"**
3. Select: `E:\manage-n8n\.tmp\direct_form_video_workflow.json`
4. Click **"Import"**

---

## Step 2: Get Your Webhook URL

1. In the imported workflow, click on the **"Form Webhook"** node
2. You'll see the webhook URL at the bottom:
   ```
   https://pakfawad.app.n8n.cloud/webhook/video-form-submit
   ```
3. **Copy this URL** - you'll need it for the form

---

## Step 3: Configure Credentials

### 3.1 OpenAI API
1. Click **"Generate Script (OpenAI)"** node
2. Click **"Select Credential"** → **"Create New"**
3. Enter your OpenAI API key
4. Click **"Save"**

### 3.2 D-ID API
1. Click **"Create Video (D-ID)"** node
2. Click **"Select Credential"** → **"Create New"**
3. Choose **"Header Auth"**
4. Set:
   - **Name**: `authorization`
   - **Value**: `Basic YOUR_D-ID_API_KEY`
5. Click **"Save"**
6. Repeat for **"Check Video Status"** node (use same credential)

### 3.3 Email (Optional)
If you want to send email notifications:
1. Click **"Send Email with Video"** node
2. Configure SMTP settings (Gmail, SendGrid, etc.)
3. Or delete this node if you don't need emails

---

## Step 4: Activate Workflow

1. Click the **toggle switch** at top right to activate
2. The workflow is now live and ready to receive form submissions!

---

## Step 5: Create Google Form with Apps Script

### 5.1 Create Your Form
1. Go to https://forms.google.com
2. Create a new form: **"AI Video Generator"**

### 5.2 Add These Questions

**Question 1: Product Name**
- Type: Short answer
- Required: Yes

**Question 2: Product Photo URL**
- Type: Short answer
- Required: No
- Help text: "Optional - leave blank to use default avatar"

**Question 3: Avatar Description**
- Type: Short answer
- Required: Yes
- Help text: "e.g., Young adult male, Professional woman, etc."

**Question 4: Product Features**
- Type: Paragraph
- Required: Yes
- Help text: "Describe the key features of your product"

**Question 5: Video Setting**
- Type: Paragraph
- Required: Yes
- Help text: "Where should the video take place? e.g., In a kitchen, At a coffee shop"

**Question 6: Email Address**
- Type: Short answer
- Required: Yes
- Validation: Email
- Help text: "We'll send your video here when it's ready"

### 5.3 Add Apps Script to Send to Webhook

1. In your Google Form, click the **three dots** (⋮) → **"Script editor"**
2. Delete any existing code
3. Paste this code:

```javascript
function onFormSubmit(e) {
  // Your n8n webhook URL
  var webhookUrl = "https://pakfawad.app.n8n.cloud/webhook/video-form-submit";
  
  // Get form responses
  var formResponse = e.response;
  var itemResponses = formResponse.getItemResponses();
  
  // Build payload
  var payload = {
    timestamp: new Date().toISOString()
  };
  
  // Map form responses to field names
  for (var i = 0; i < itemResponses.length; i++) {
    var itemResponse = itemResponses[i];
    var question = itemResponse.getItem().getTitle();
    var answer = itemResponse.getResponse();
    
    // Map questions to field names
    if (question.toLowerCase().includes('product name')) {
      payload.product_name = answer;
    } else if (question.toLowerCase().includes('photo')) {
      payload.product_photo = answer;
    } else if (question.toLowerCase().includes('avatar')) {
      payload.avatar_description = answer;
    } else if (question.toLowerCase().includes('features')) {
      payload.product_features = answer;
    } else if (question.toLowerCase().includes('setting')) {
      payload.video_setting = answer;
    } else if (question.toLowerCase().includes('email')) {
      payload.email = answer;
    }
  }
  
  // Send to n8n webhook
  var options = {
    'method': 'post',
    'contentType': 'application/json',
    'payload': JSON.stringify(payload),
    'muteHttpExceptions': true
  };
  
  try {
    var response = UrlFetchApp.fetch(webhookUrl, options);
    Logger.log('Webhook response: ' + response.getContentText());
  } catch (error) {
    Logger.log('Error sending to webhook: ' + error);
  }
}
```

4. Click **"Save"** (disk icon)
5. Name it: "Send to n8n"

### 5.4 Set Up Trigger

1. Click the **clock icon** (Triggers) on the left
2. Click **"+ Add Trigger"** (bottom right)
3. Choose:
   - **Function**: `onFormSubmit`
   - **Event source**: From form
   - **Event type**: On form submit
4. Click **"Save"**

### 5.5 Authorize the Script

1. Click **"Run"** → **"onFormSubmit"**
2. Click **"Review permissions"**
3. Choose your Google account
4. Click **"Advanced"** → **"Go to Send to n8n (unsafe)"**
5. Click **"Allow"**

---

## Step 6: Test It!

### 6.1 Submit Test Form
1. Open your Google Form
2. Fill it out with test data:
   - Product Name: "Test Product"
   - Product Photo URL: (leave blank)
   - Avatar Description: "Young adult male"
   - Product Features: "Amazing features, great quality"
   - Video Setting: "In a modern office"
   - Email: your-email@example.com
3. Click **"Submit"**

### 6.2 Check n8n
1. Go to your n8n workflow
2. Click **"Executions"** tab
3. You should see a new execution running
4. Watch it progress through the nodes

### 6.3 Wait for Email
- In 2-3 minutes, you'll receive an email with your video URL!
- Click the link to view your AI-generated video

---

## How It Works

```
User submits form → 
Apps Script sends data to webhook → 
n8n receives data → 
OpenAI generates script → 
D-ID creates video → 
Email sent with video URL
```

**Total time**: ~2-3 minutes per video

---

## Troubleshooting

### Form not triggering workflow
- Check Apps Script trigger is set up correctly
- View Apps Script logs: **Extensions** → **Apps Script** → **Executions**
- Verify webhook URL is correct in the script

### Webhook errors
- Make sure workflow is **Active** in n8n
- Check n8n execution logs for errors
- Test webhook directly with curl:
```bash
curl -X POST https://pakfawad.app.n8n.cloud/webhook/video-form-submit \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "Test",
    "avatar_description": "Young adult",
    "product_features": "Great features",
    "video_setting": "Modern office",
    "email": "test@example.com"
  }'
```

### No email received
- Check spam folder
- Verify SMTP credentials in n8n
- Check n8n execution logs for email errors
- Or remove email node and check video URL in n8n execution output

---

## Cost Per Video

- **OpenAI (script)**: ~$0.01
- **D-ID (video)**: 2-3 credits (~$0.30-0.45 on paid plans)
- **Total**: ~$0.31-0.46 per video

**Free tier**: D-ID gives 20 credits/month = ~10 free videos/month

---

## Files Created

- **Workflow JSON**: `.tmp/direct_form_video_workflow.json`
- **Setup Guide**: `.tmp/direct-form-setup-guide.md`

---

**Ready to go!** Share your Google Form link and start generating AI videos automatically.
