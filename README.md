# AI Lead Qualification System

A professional Next.js frontend for the n8n Lead Enrichment & Qualification Pipeline.

## Features

- 🎯 AI-powered lead scoring and qualification
- 🤖 Automatic company data enrichment
- 🔧 Tech stack detection (Mailchimp, HubSpot, Salesforce, ActiveCampaign)
- ✨ Personalized email generation for hot leads
- 📊 Real-time processing and results display
- 🎨 Professional, corporate design with Tailwind CSS

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Backend**: n8n workflow automation
- **AI**: Google Gemini 2.5 Flash
- **Deployment**: Vercel

## Getting Started

### Prerequisites

- Node.js 18+ installed
- n8n instance running (https://pakfawad.app.n8n.cloud/)
- Git installed

### Installation

1. Clone the repository:
```bash
git clone https://github.com/muhammadfawad538/Ai-Lead-Qualification-System.git
cd Ai-Lead-Qualification-System/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create environment file:
```bash
cp .env.local.example .env.local
```

4. Update `.env.local` with your n8n webhook URL

5. Run development server:
```bash
npm run dev
```

6. Open [http://localhost:3000](http://localhost:3000)

## Project Structure

```
frontend/
├── src/
│   ├── app/              # Next.js app router pages
│   ├── components/       # React components
│   ├── lib/             # Utilities and API functions
│   └── config/          # Configuration files
├── public/              # Static assets
└── package.json
```

## Deployment

### Deploy to Vercel

1. Push code to GitHub
2. Import project in Vercel
3. Configure environment variables
4. Deploy!

Vercel will automatically deploy on every push to main branch.

## Environment Variables

Required variables in `.env.local`:

```bash
NEXT_PUBLIC_N8N_WEBHOOK_URL=your_webhook_url
NEXT_PUBLIC_N8N_INSTANCE_URL=your_n8n_instance
GOOGLE_SHEET_ID=your_sheet_id
```

## Workflow Integration

This frontend connects to the n8n Lead Enrichment workflow which:

1. Validates email and extracts domain
2. Scrapes company website
3. Detects tech stack
4. AI analyzes company data
5. Calculates lead score (0-100)
6. Generates personalized emails for hot leads (70+)
7. Saves to Google Sheets

## Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run lint` - Run ESLint

### Making Changes

1. Make changes to components or pages
2. Test locally with `npm run dev`
3. Commit and push to GitHub
4. Vercel auto-deploys

## License

MIT

## Support

For issues or questions, please open an issue on GitHub.
