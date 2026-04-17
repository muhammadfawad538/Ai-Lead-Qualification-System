# SIMPLE Setup Guide - Google Form to AI Video (100% FREE)

## What You Get
- Google Form → Gemini (FREE) → D-ID Video (FREE 10/month)
- **NO Apps Script needed!**
- **NO coding required!**
- Just 3 API keys and you're done

---

## Step 1: Get Your API Keys (5 minutes)

### 1.1 Get Gemini API Key (FREE)
1. Go to: https://makersuite.google.com/app/apikey
2. Click **"Create API Key"**
3. Copy the key
4. Save it somewhere safe

**Cost**: FREE forever (generous limits)

### 1.2 Get D-ID API Key (FREE)
1. Go to: https://studio.d-id.com/
2. Sign up (email/Google/GitHub)
3. Go to: https://studio.d-id.com/account-settings
4. Click **"API"** tab
5. Copy your API key
6. Save it

**Cost**: FREE - 20 credits/month = ~10 videos/month

---

## Step 2: Create Your Google Form (2 minutes)

1. Go to: https://forms.google.com
2. Click **"+ Blank"**
3. Title: **"AI Video Generator"**

### Add These 5 Questions:

**Question 1:**
- Title: `Product Name`
- Type: Short answer
- Required: ✓

**Question 2:**
- Title: `Product Photo URL`
- Type: Short answer
- Required: ✗
- Help text: "Optional - leave blank for default avatar"

**Question 3:**
- Title: `Avatar Description`
- Type: Short answer
- Required: ✓
- Help text: "e.g., Young adult male, Professional woman"

**Question 4:**
- Title: `Product Features`
- Type: Paragraph
- Required: ✓

**Question 5:**
- Title: `Video Setting`
- Type: Paragraph
- Required: ✓
- Help text: "e.g., In a kitchen, At a coffee shop"

4. Click **"Send"** to get the form link (you'll need this later)

---

## Step 3: Import Workflow to n8n (3 minutes)

### 3.1 Import
1. Go to: https://pakfawad.app.n8n.cloud
2. Click **"Add workflow"** → **"Import from File"**
3. Select: `E:\manage-n8n\.tmp\simple_form_video_workflow.json`
4. Click **"Import"**

### 3.2 Connect Google Form
1. Click the **"Google Form Trigger"** node
2. Click **"Connect my account"**
3. Sign in with Google
4. Grant permissions
5. Select your **"AI Video Generator"** form from the dropdown
6. Click **"Save"**

### 3.3 Add Gemini API Key
1. Click **"Generate Script (Gemini FREE)"** node
2. Click **"Select Credential"** → **"Create New"**
3. Choose **"Query Auth"**
4. Set:
   - **Name**: `key`
   - **Value**: `YOUR_GEMINI_API_KEY` (paste your key)
5. Click **"Save"**

### 3.4 Add D-ID API Key
1. Click **"Create Video (D-ID)"** node
2. Click **"Select Credential"** → **"Create New"**
3. Choose **"Header Auth"**
4. Set:
   - **Name**: `authorization`
   - **Value**: `Basic YOUR_D-ID_API_KEY` (paste your key after "Basic ")
5. Click **"Save"**

6. Click **"Get Video URL"** node
7. Select the same D-ID credential you just created
8. Click **"Save"**

---

## Step 4: Activate! (1 second)

1. Click the **toggle switch** at the top right
2. It should turn green/blue
3. Done! Your workflow is LIVE!

---

## Step 5: Test It! (2 minutes)

1. Open your Google Form (the link from Step 2)
2. Fill it out:
   - Product Name: `Test Cologne`
   - Product Photo URL: (leave blank)
   - Avatar Description: `Young adult male`
   - Product Features: `Fresh scent, long-lasting, perfect for daily use`
   - Video Setting: `In a modern kitchen, getting ready for work`
3. Click **"Submit"**

4. Go back to n8n
5. Click **"Executions"** tab
6. Watch your workflow run!
7. After ~30-60 seconds, click on the execution
8. Look at the **"Show Result"** node
9. Copy the `video_url` and open it in your browser
10. **Your AI video is ready!** 🎉

---

## How to Find Your Videos

After each form submission:
1. Go to n8n → **"Executions"** tab
2. Click on the latest execution
3. Click the **"Show Result"** node
4. Copy the `video_url`
5. Open in browser to view/download

**Note**: Videos take 30-90 seconds to generate. If status shows "processing", wait 1 minute and check the D-ID dashboard: https://studio.d-id.com/

---

## Troubleshooting

### Form submission doesn't trigger workflow
- Make sure workflow is **Active** (toggle on)
- Check Google Form connection in the trigger node
- Try disconnecting and reconnecting Google account

### Gemini errors
- Verify API key is correct
- Check quota: https://makersuite.google.com/app/apikey
- Gemini is free but has rate limits (60 requests/minute)

### D-ID errors
- Check API key format: `Basic YOUR_KEY` (with "Basic " prefix)
- Verify credits: https://studio.d-id.com/account-settings
- Free tier: 20 credits/month

### Video shows "processing"
- D-ID takes 30-90 seconds to generate video
- Wait 1 minute and check: https://studio.d-id.com/
- Or add more "Wait" nodes in the workflow

---

## Cost Breakdown

**100% FREE for first 10 videos/month:**
- Gemini: FREE (unlimited for personal use)
- D-ID: FREE (20 credits = ~10 videos)
- n8n: FREE (on your cloud plan)

**After free tier:**
- D-ID Lite: $5.90/month for 100 credits (~50 videos)

---

## What's Next?

### Share Your Form
1. Get the form link from Google Forms
2. Share it with anyone
3. Videos generate automatically!

### View All Videos
- Check n8n executions for video URLs
- Or log into D-ID dashboard to see all generated videos

### Upgrade (Optional)
- Add email notifications
- Save videos to Google Drive
- Add more form fields
- Use different AI voices

---

## Files You Have

- **Workflow JSON**: `.tmp/simple_form_video_workflow.json` ✓
- **This Guide**: `.tmp/simple-setup-guide.md` ✓

---

**That's it! You now have a fully automated AI video generator!** 🚀

Total setup time: ~10 minutes
Cost: FREE (10 videos/month)
