# Lead Enrichment Workflow - Frontend Showcase

A professional Next.js frontend for showcasing and interacting with the n8n Lead Enrichment & Qualification Pipeline workflow.

## Project Overview

This project provides a corporate, professional web interface for the Lead Enrichment workflow that:
- Displays workflow information and capabilities
- Allows users to submit leads via an embedded form
- Shows real-time processing status
- Displays results and lead scores
- Syncs automatically with n8n workflow changes

**Tech Stack**: Next.js 14, React, Tailwind CSS, TypeScript

---

## n8n Integration

### n8n Instance Details
- **URL**: https://pakfawad.app.n8n.cloud/
- **Tier**: Free tier
- **Workflow**: Lead Enrichment & Qualification Pipeline

### Workflow Capabilities
The workflow automatically:
1. Validates email and extracts company domain
2. Scrapes company website
3. Detects tech stack (Mailchimp, ActiveCampaign, Salesforce, HubSpot)
4. AI analyzes company data (size, industry, revenue, pain points)
5. Calculates lead score (0-100) based on ICP fit
6. Generates personalized email for hot leads (70+)
7. Saves all data to Google Sheets

---

## Project Structure

```
lead-enrichment-frontend/
├── src/
│   ├── app/
│   │   ├── page.tsx              # Home page
│   │   ├── layout.tsx            # Root layout
│   │   └── globals.css           # Global styles
│   ├── components/
│   │   ├── LeadForm.tsx          # Lead submission form
│   │   ├── WorkflowDiagram.tsx   # Visual workflow representation
│   │   ├── ResultsDisplay.tsx    # Show lead scoring results
│   │   └── Hero.tsx              # Landing section
│   ├── lib/
│   │   ├── n8n.ts                # n8n API integration
│   │   └── types.ts              # TypeScript types
│   └── config/
│       └── workflow.ts           # Workflow configuration
├── public/
│   └── images/                   # Static assets
├── .env.local                    # Environment variables
├── next.config.js
├── tailwind.config.ts
├── tsconfig.json
└── package.json
```

---

## Development Workflow

### Making Changes

1. **Update n8n Workflow**:
   - Make changes in n8n cloud instance
   - Test the workflow
   - Export updated JSON if needed

2. **Update Frontend**:
   - Modify components in `src/components/`
   - Update workflow config in `src/config/workflow.ts`
   - Test locally with `npm run dev`

3. **Push to GitHub**:
   - Commit changes: `git add . && git commit -m "description"`
   - Push: `git push origin main`

4. **Auto-Deploy**:
   - Vercel automatically detects push
   - Builds and deploys new version
   - Live in ~2 minutes

### Using MCP Servers

This project uses these MCP servers:

**n8n MCP** (`https://pakfawad.app.n8n.cloud/mcp-server/http`):
- View workflows in your n8n instance
- Read node configurations
- Update workflow settings
- Test workflow executions

**GitHub MCP**:
- Create/update repository
- Commit and push changes
- Manage branches
- View commit history

**Frontend Designer Skill**:
- Design React components
- Create Tailwind layouts
- Build responsive UI

---

## Environment Variables

Create `.env.local` with:

```bash
# n8n Configuration
NEXT_PUBLIC_N8N_WEBHOOK_URL=https://pakfawad.app.n8n.cloud/webhook/lead-enrichment-form
NEXT_PUBLIC_N8N_INSTANCE_URL=https://pakfawad.app.n8n.cloud

# Optional: n8n API (if you enable API access)
N8N_API_KEY=your_api_key_here

# Google Sheets (for displaying results)
GOOGLE_SHEET_ID=1NSTsnCxlUqeyj_l873BYOLAYOeVz1xjG-F6s5H5uE64
```

---

## Design Guidelines

### Visual Style
- **Corporate/Professional**: Clean, trustworthy, business-focused
- **Color Palette**: Blues, grays, white (professional SaaS aesthetic)
- **Typography**: Clear, readable, hierarchical
- **Layout**: Spacious, organized, easy to scan

### Component Principles
- Keep components small and focused
- Use TypeScript for type safety
- Follow Next.js 14 App Router conventions
- Responsive design (mobile-first)
- Accessible (WCAG AA minimum)

### Code Style
- Use functional components with hooks
- Prefer server components when possible
- Client components only when needed (interactivity)
- Tailwind for all styling (no custom CSS unless necessary)
- Clear, descriptive variable names

---

## Key Features to Implement

### 1. Landing Page
- Hero section explaining the workflow
- Visual workflow diagram
- Key benefits and features
- CTA to try the demo

### 2. Lead Submission Form
- Embedded n8n form or custom form
- Real-time validation
- Loading states during processing
- Success/error feedback

### 3. Results Display
- Show lead score with visual indicator
- Display detected tech stack
- Show ICP fit breakdown
- Display generated email (for hot leads)
- Archive reason (for cold leads)

### 4. Workflow Visualization
- Interactive diagram showing workflow steps
- Highlight current processing step
- Show what data is collected at each stage

---

## Deployment

### GitHub Setup
1. Repository created at: `github.com/[username]/lead-enrichment-frontend`
2. Main branch: `main`
3. Auto-sync enabled

### Vercel Setup
1. Connect GitHub repository
2. Import project to Vercel
3. Configure environment variables
4. Enable auto-deployments on push
5. Custom domain (optional)

### Continuous Deployment
- Push to `main` → Auto-deploy to production
- Pull requests → Preview deployments
- Rollback available via Vercel dashboard

---

## Working with Claude

### When Making Changes

**Tell Claude**:
- "Update the lead form to include a company size field"
- "Change the color scheme to use green instead of blue"
- "Add a loading spinner while the workflow processes"
- "Push changes to GitHub"

**Claude Will**:
1. Read current code structure
2. Make necessary changes
3. Test locally if needed
4. Commit and push to GitHub
5. Verify Vercel deployment

### Accessing n8n Workflows

**Claude can**:
- View your n8n workflows via MCP
- Read node configurations
- Understand workflow logic
- Suggest improvements
- Update workflow documentation

**Example**: "Show me the current Lead Enrichment workflow configuration"

---

## Common Tasks

### Update Workflow Display
```bash
# Claude will:
# 1. Read workflow from n8n MCP
# 2. Update src/config/workflow.ts
# 3. Regenerate workflow diagram
# 4. Push to GitHub
```

### Change Form Fields
```bash
# Claude will:
# 1. Update LeadForm.tsx component
# 2. Update TypeScript types
# 3. Test form validation
# 4. Push to GitHub
```

### Modify Styling
```bash
# Claude will:
# 1. Update Tailwind classes
# 2. Ensure responsive design
# 3. Check accessibility
# 4. Push to GitHub
```

---

## Troubleshooting

### n8n Webhook Not Working
- Verify webhook URL in `.env.local`
- Check workflow is activated in n8n
- Test webhook directly in browser

### Vercel Build Failing
- Check environment variables are set
- Review build logs in Vercel dashboard
- Ensure all dependencies are in package.json

### Styling Issues
- Clear Next.js cache: `rm -rf .next`
- Rebuild: `npm run build`
- Check Tailwind config

---

## Resources

- **n8n Instance**: https://pakfawad.app.n8n.cloud/
- **n8n Docs**: https://docs.n8n.io/
- **Next.js Docs**: https://nextjs.org/docs
- **Tailwind Docs**: https://tailwindcss.com/docs
- **Vercel Docs**: https://vercel.com/docs

---

## Maintenance

### Regular Updates
- Keep dependencies updated: `npm update`
- Review n8n workflow changes monthly
- Monitor Vercel analytics
- Check Google Sheets data quality

### Performance
- Optimize images (use Next.js Image component)
- Lazy load components when appropriate
- Monitor Core Web Vitals in Vercel
- Cache static assets

---

## Notes for Claude

- Always check n8n MCP before making workflow-related changes
- Use GitHub MCP for all git operations
- Test changes locally before pushing when possible
- Keep code clean and well-documented
- Follow Next.js and React best practices
- Maintain TypeScript strict mode
- Ensure mobile responsiveness
- Keep bundle size small

---

**Last Updated**: 2026-04-17
**Version**: 1.0.0
**Status**: Initial Setup
