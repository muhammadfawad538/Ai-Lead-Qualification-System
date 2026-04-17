# How to Create and Connect Google Form - Step by Step

## Part 1: Create the Google Form

### Step 1: Create New Form
1. Go to: https://forms.google.com
2. Click the **"+"** button (Blank form)
3. Click "Untitled form" at the top
4. Type: **AI Video Generator**
5. Add description: **Generate AI videos from your product information**

---

### Step 2: Add Question 1 - Product Name

1. Click on the first question box
2. **Question text**: `Product Name`
3. **Question type**: Short answer (should be selected by default)
4. Click **"Required"** toggle (bottom right of question)
5. The question should now have a red asterisk *

---

### Step 3: Add Question 2 - Product Photo URL

1. Click the **"+"** button on the right side to add new question
2. **Question text**: `Product Photo URL`
3. **Question type**: Short answer
4. Click the **three dots** (⋮) at bottom right
5. Click **"Description"**
6. Type: `Optional - leave blank to use default avatar`
7. **Do NOT** make this required (no red asterisk)

---

### Step 4: Add Question 3 - Avatar Description

1. Click **"+"** to add new question
2. **Question text**: `Avatar Description`
3. **Question type**: Short answer
4. Click the **three dots** (⋮)
5. Click **"Description"**
6. Type: `Example: Young adult male, Professional woman, Teenager`
7. Click **"Required"** toggle

---

### Step 5: Add Question 4 - Product Features

1. Click **"+"** to add new question
2. **Question text**: `Product Features`
3. **Question type**: Click dropdown → Select **"Paragraph"**
4. Click the **three dots** (⋮)
5. Click **"Description"**
6. Type: `Describe the key features and benefits of your product`
7. Click **"Required"** toggle

---

### Step 6: Add Question 5 - Video Setting

1. Click **"+"** to add new question
2. **Question text**: `Video Setting`
3. **Question type**: Click dropdown → Select **"Paragraph"**
4. Click the **three dots** (⋮)
5. Click **"Description"**
6. Type: `Where should the video take place? Example: In a kitchen, At a coffee shop, In an office`
7. Click **"Required"** toggle

---

### Step 7: Customize Form Appearance (Optional)

1. Click the **palette icon** at the top right
2. Choose a theme color
3. Choose a background style
4. Click **X** to close

---

### Step 8: Get Form Link

1. Click **"Send"** button (top right)
2. Click the **link icon** (chain link)
3. Click **"Shorten URL"** checkbox
4. Click **"Copy"**
5. **Save this link** - you'll share it with users later

---

## Part 2: Connect Form to n8n Workflow

### Step 1: Open Your n8n Workflow

1. Go to: https://pakfawad.app.n8n.cloud
2. Open the imported workflow: **"Simple Form to AI Video (Gemini Free)"**

---

### Step 2: Configure Google Form Trigger Node

1. Click on the **"Google Form Trigger"** node (first node on the left)
2. You'll see a panel open on the right side

---

### Step 3: Connect Google Account

1. In the right panel, find **"Credential to connect with"**
2. Click the dropdown that says **"Select Credential"**
3. Click **"Create New"**
4. A popup will appear
5. Click **"Connect my account"** (or "Sign in with Google")
6. A new window opens - sign in with your Google account
7. Click **"Allow"** to grant permissions
8. The window closes automatically
9. You should see your Google account email appear
10. Click **"Save"** at the bottom

---

### Step 4: Select Your Form

1. Still in the **"Google Form Trigger"** node panel
2. Find the field **"Form"**
3. Click the dropdown
4. You should see a list of your Google Forms
5. Find and click **"AI Video Generator"**
6. The form ID will populate automatically

---

### Step 5: Test the Connection

1. At the bottom of the node panel, click **"Listen for Test Event"**
2. The button will change to **"Waiting for test event..."**
3. Open your Google Form in a new tab (use the link from Part 1, Step 8)
4. Fill out the form with test data:
   - Product Name: `Test Product`
   - Product Photo URL: (leave blank)
   - Avatar Description: `Young adult male`
   - Product Features: `Amazing features, great quality`
   - Video Setting: `In a modern office`
5. Click **"Submit"**
6. Go back to n8n
7. You should see **"Test event received"** with green checkmark
8. Click **"Use test event"**

---

### Step 6: Save the Node

1. Click **"Save"** button at the bottom of the panel
2. The node should now have a green checkmark
3. Close the panel by clicking the **X** or clicking outside

---

## Part 3: Configure Other Credentials

### Gemini API Key

1. Click the **"Generate Script (Gemini FREE)"** node
2. Find **"Credential to connect with"**
3. Click **"Create New"**
4. Choose **"Query Auth"**
5. **Name**: `key`
6. **Value**: Paste your Gemini API key (from https://makersuite.google.com/app/apikey)
7. Click **"Save"**

---

### D-ID API Key

1. Click the **"Create Video (D-ID)"** node
2. Find **"Credential to connect with"**
3. Click **"Create New"**
4. Choose **"Header Auth"**
5. **Name**: `authorization`
6. **Value**: Type `Basic ` then paste your D-ID API key
   - Example: `Basic abc123xyz456`
   - Make sure there's a space after "Basic"
7. Click **"Save"**

8. Click the **"Get Video URL"** node
9. Find **"Credential to connect with"**
10. Click the dropdown
11. Select the D-ID credential you just created
12. Click **"Save"**

---

## Part 4: Activate Workflow

1. At the top right of the workflow, find the toggle switch
2. Click it to turn it **ON**
3. It should turn green/blue
4. You'll see **"Active"** status

---

## Part 5: Test End-to-End

1. Open your Google Form link
2. Fill it out with real test data:
   ```
   Product Name: Premium Coffee Maker
   Product Photo URL: (leave blank)
   Avatar Description: Professional woman in her 30s
   Product Features: Makes perfect coffee every time, easy to clean, programmable timer
   Video Setting: In a modern kitchen in the morning
   ```
3. Click **"Submit"**

4. Go to n8n
5. Click **"Executions"** tab (left sidebar)
6. You should see a new execution running
7. Wait 30-60 seconds
8. Click on the execution to see details
9. Click the **"Show Result"** node
10. Look for **"video_url"** in the output
11. Copy the URL and open it in your browser
12. **Your video is ready!**

---

## Troubleshooting

### "No forms found" in dropdown
- Make sure you're signed in with the correct Google account
- Try disconnecting and reconnecting your Google account
- Refresh the page and try again

### Form trigger not working
- Make sure workflow is **Active** (toggle ON)
- Check that the correct form is selected
- Try the "Listen for Test Event" again

### "Credential not found" errors
- Make sure you saved each credential
- Check that API keys are correct (no extra spaces)
- For D-ID, make sure you have "Basic " before the key

### Video not generating
- Check n8n execution logs for errors
- Verify Gemini API key: https://makersuite.google.com/app/apikey
- Verify D-ID credits: https://studio.d-id.com/account-settings

---

## Summary Checklist

- [ ] Created Google Form with 5 questions
- [ ] Got form link and saved it
- [ ] Connected Google account to n8n
- [ ] Selected form in Google Form Trigger node
- [ ] Added Gemini API key
- [ ] Added D-ID API key (with "Basic " prefix)
- [ ] Activated workflow
- [ ] Tested with form submission
- [ ] Got video URL in execution results

---

**You're done!** Share your form link and start generating AI videos automatically.
