'use client'

export default function LeadForm() {
  const formUrl = process.env.NEXT_PUBLIC_N8N_FORM_URL || 'https://pakfawad.app.n8n.cloud/form/ee6a5882-b7a0-4f8a-9f38-b86aec1ec9e3'

  return (
    <div className="bg-white rounded-lg shadow-lg p-8">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-900 mb-2">Submit Your Lead</h2>
        <p className="text-gray-600">Fill out the form below and our AI will analyze your company fit in real-time.</p>
      </div>

      <iframe
        src={formUrl}
        width="100%"
        height="800"
        style={{ border: 'none' }}
        title="Lead Enrichment Form"
      />

      <div className="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
        <p className="text-sm text-blue-800">
          <strong>What happens next?</strong> Our AI workflow will validate your email, analyze your company website,
          detect your tech stack, calculate a lead score, and generate a personalized outreach email if you're a good fit.
        </p>
      </div>
    </div>
  )
}
