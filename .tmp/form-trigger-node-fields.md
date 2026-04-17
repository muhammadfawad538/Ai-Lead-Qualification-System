# Google Form Trigger Node - Manual Configuration

## What to Put in Each Field

When you click on the **"Google Form Trigger"** node in n8n, you'll see these fields:

---

## Field 1: Credential to connect with

**What to select**: Your Google account credential

**How to set it up**:
1. Click the dropdown
2. Click **"Create New"**
3. Click **"Connect my account"**
4. Sign in with Google
5. Click **"Allow"**
6. Click **"Save"**

**What it looks like after setup**:
```
Credential: Google Forms OAuth2 API (your-email@gmail.com)
```

---

## Field 2: Form

**What to select**: Your Google Form

**How to get it**:
1. After connecting your Google account, this dropdown will populate
2. Click the dropdown
3. Select **"AI Video Generator"** (or whatever you named your form)

**Alternative - Manual Entry**:
If the dropdown doesn't work, you can enter the Form ID manually:

1. Open your Google Form
2. Look at the URL: `https://docs.google.com/forms/d/FORM_ID_HERE/edit`
3. Copy the `FORM_ID_HERE` part
4. Paste it in the Form field

**Example Form ID**:
```
1FAIpQLSdXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXx
```

---

## Field 3: Trigger On

**What to select**: `Form Submit`

**Options**:
- Form Submit (recommended) - triggers when someone submits the form
- Form Response Edit - triggers when someone edits their response

**What to put**:
```
Trigger On: Form Submit
```

---

## Complete Configuration Example

After filling everything out, your node should look like this:

```
┌─────────────────────────────────────────┐
│ Google Form Trigger                     │
├─────────────────────────────────────────┤
│ Credential to connect with:             │
│ ✓ Google Forms OAuth2 API               │
│   (your-email@gmail.com)                │
│                                         │
│ Form:                                   │
│ ✓ AI Video Generator                    │
│   (or Form ID: 1FAIpQLSd...)           │
│                                         │
│ Trigger On:                             │
│ ✓ Form Submit                           │
└─────────────────────────────────────────┘
```

---

## How to Test It Works

1. At the bottom of the node panel, click **"Listen for Test Event"**
2. Open your Google Form
3. Fill it out and submit
4. Go back to n8n
5. You should see **"Test event received"** ✓
6. Click **"Use test event"**

---

## What the Node Receives

When someone submits your form, the node receives this data:

```json
{
  "responses": {
    "Product Name": "Test Product",
    "Product Photo URL": "",
    "Avatar Description": "Young adult male",
    "Product Features": "Amazing features",
    "Video Setting": "In a modern office"
  },
  "respondentEmail": "user@example.com",
  "timestamp": "2026-04-14T18:00:00.000Z"
}
```

The next node (**"Extract Data"**) will parse this and pass it to Gemini.

---

## Common Issues

### Issue: "No forms found" in dropdown
**Solution**: 
- Make sure you created the Google Form first
- Try disconnecting and reconnecting your Google account
- Refresh the n8n page

### Issue: Form ID not working
**Solution**:
- Make sure you copied the correct part of the URL
- The Form ID is between `/d/` and `/edit`
- Don't include any slashes

### Issue: Trigger not firing
**Solution**:
- Make sure workflow is **Active** (toggle ON)
- Check that you selected "Form Submit" not "Form Response Edit"
- Try the "Listen for Test Event" test

---

## That's It!

Just these 3 fields:
1. **Credential**: Your Google account
2. **Form**: Your form name or ID
3. **Trigger On**: Form Submit

The node will automatically receive form submissions and pass the data to the next node.
