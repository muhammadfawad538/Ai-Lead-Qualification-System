import Hero from '@/components/Hero'
import LeadForm from '@/components/LeadForm'
import WorkflowDiagram from '@/components/WorkflowDiagram'

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-gray-50 to-white">
      <Hero />

      <section className="py-16 px-4 max-w-7xl mx-auto">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">
            How It Works
          </h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Our AI-powered workflow automatically enriches and qualifies your leads in seconds
          </p>
        </div>
        <WorkflowDiagram />
      </section>

      <section className="py-16 px-4 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">
              Try It Now
            </h2>
            <p className="text-lg text-gray-600">
              Submit a lead and see the enrichment process in action
            </p>
          </div>
          <LeadForm />
        </div>
      </section>

      <footer className="py-8 px-4 border-t border-gray-200">
        <div className="max-w-7xl mx-auto text-center text-gray-600">
          <p>© 2026 Lead Enrichment Pipeline. Powered by n8n & AI.</p>
        </div>
      </footer>
    </main>
  )
}
