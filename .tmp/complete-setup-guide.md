# Complete Setup Guide: Google Form to AI Video Generator

## Overview
This workflow automatically generates AI videos from Google Form submissions. When someone fills out your form, n8n will:
1. Detect the new response
2. Generate a UGC script with OpenAI
3. Create a talking head video with D-ID
4. Update the Google Sheet with the video URL

---

## Step 1: Create Your Google Form

### 1.1 Create the Form
1. Go to https://forms.google.com
2. Click **"+ Blank"** to create a new form
3. Name it: **"AI Video Ad Generator"**

### 1.2 Add These Questions (Required)

**Question 1: Product Name**
- Type: Short answer
- Required: Yes
- Example: "Cologne"

**Question 2: Product Photo URL**
- Type: Short answer
- Required: No (D-ID has default avatars)
- Example: "https://example.com/product.jpg"

**Question 3: Avatar Description**
- Type: Short answer
- Required: Yes
- Example: "Young adult male"

**Question 4: Product Features**
- Type: Paragraph
- Required: Yes
- Example: "clean scent, not too strong, long-lasting"

**Question 5: Video Setting**
- Type: Paragraph
- Required: Yes
- Example: "In a kitchen, getting ready to head out"

### 1.3 Link to Google Sheets
1. Click the **"Responses"** tab in your form
2. Click the **Google Sheets icon** (green)
3. Choose **"Create a new spreadsheet"**
4. Name it: **"Video Ad Responses"**
5. Click **"Create"**

---

## Step 2: Get D-ID API Key

### 2.1 Sign Up
1. Go to https://studio.d-id.com/
2. Click **"Sign Up"**
3. Use email, Google, or GitHub

### 2.2 Get API Key
1. After login, go to https://studio.d-id.com/account-settings
2. Click **"API"** tab
3. Copy your **API Key**
4. Save it securely

**Free Tier**: 20 credits/month (enough for ~10 videos)

---

## Step 3: Import Workflow to n8n

### 3.1 Import the JSON
1. Go to https://pakfawad.app.n8n.cloud
2. Click **"Add workflow"** → **"Import from File"**
3. Select: `E:\manage-n8n\.tmp\google_form_video_workflow.json`
4. Click **"Import"**

### 3.2 Configure Google Sheets Connection
1. Click on **"Google Sheets Trigger"** node
2. Click **"Select Credential"** → **"Create New"**
3. Click **"Connect my account"**
4. Sign in with your Google account
5. Grant permissions
6. Select your **"Video Ad Responses"** spreadsheet
7. Select **"Sheet1"**

### 3.3 Configure OpenAI
1. Click on **"Generate Script (OpenAI)"** node
2. Click **"Select Credential"** → **"Create New"**
3. Enter your **OpenAI API Key**
4. Click **"Save"**

### 3.4 Configure D-ID
1. Click on **"Create Video (D-ID)"** node
2. Click **"Select Credential"** → **"Create New"**
3. Choose **"Header Auth"**
4. Set:
   - **Name**: `authorization`
   - **Value**: `Basic YOUR_D-ID_API_KEY`
   - Replace `YOUR_D-ID_API_KEY` with your actual key
5. Click **"Save"**

6. Repeat for **"Check Video Status"** node (use same credential)

### 3.5 Update Sheet Configuration
1. Click on **"Update Sheet with Video"** node
2. Select the same Google Sheets credential
3. Select your **"Video Ad Responses"** spreadsheet
4. Select **"Sheet1"**

---

## Step 4: Prepare Your Google Sheet

### 4.1 Add Output Columns
Open your Google Sheet and add these column headers (after the form columns):

- **Video URL**
- **Status**
- **Completed At**

Your sheet should look like:
```
| Timestamp | Product Name | Product Photo URL | Avatar Description | Product Features | Video Setting | Video URL | Status | Completed At |
```

---

## Step 5: Activate the Workflow

1. In n8n, click the **toggle switch** at the top right
2. The workflow is now **Active**
3. It will automatically process new form submissions

---

## Step 6: Test It

### 6.1 Submit a Test Form
1. Open your Google Form
2. Fill it out with test data:
   - Product Name: "Test Cologne"
   - Product Photo URL: (leave blank or use a URL)
   - Avatar Description: "Young adult male"
   - Product Features: "Fresh scent, long-lasting"
   - Video Setting: "In a modern kitchen"
3. Click **"Submit"**

### 6.2 Watch the Magic
1. Go to your Google Sheet
2. You'll see the new row appear
3. Wait 2-3 minutes
4. The **Video URL**, **Status**, and **Completed At** columns will update automatically
5. Click the video URL to view your generated video!

---

## Troubleshooting

### Form not triggering workflow
- Make sure the workflow is **Active** (toggle on)
- Check that Google Sheets credential is connected
- Try clicking **"Test workflow"** in n8n

### OpenAI errors
- Verify your API key is correct
- Check you have credits: https://platform.openai.com/usage
- Each script generation costs ~$0.01

### D-ID errors
- Verify your API key format: `Basic YOUR_KEY`
- Check credits: https://studio.d-id.com/account-settings
- Free tier: 20 credits/month

### Video not appearing in sheet
- Check n8n execution logs for errors
- Verify the "Update Sheet with Video" node has correct sheet selected
- Make sure column headers match exactly

---

## Cost Breakdown

**Per Video:**
- OpenAI (script): ~$0.01
- D-ID (video): ~2-3 credits (~$0.30-0.45 on paid plans)
- **Total**: ~$0.31-0.46 per video

**Free Tier:**
- D-ID: 20 credits/month = ~10 videos/month free
- OpenAI: $5 free credit for new accounts

---

## Next Steps

1. Share your Google Form with users
2. Videos will generate automatically
3. Check your Google Sheet for results
4. Download videos from the URLs provided

---

## Files Created

- **Workflow JSON**: `.tmp/google_form_video_workflow.json`
- **D-ID Setup Guide**: `.tmp/d-id-setup-guide.md`
- **This Guide**: `.tmp/complete-setup-guide.md`

---

**Questions?** Check the n8n execution logs for detailed error messages.
