export default function Hero() {
  return (
    <div className="relative overflow-hidden bg-white">
      <div className="mx-auto max-w-7xl px-6 py-24 sm:py-32 lg:px-8">
        <div className="mx-auto max-w-2xl text-center">
          <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">
            AI-Powered Lead Enrichment & Qualification
          </h1>
          <p className="mt-6 text-lg leading-8 text-gray-600">
            Automatically enrich, score, and qualify your leads in seconds.
            Our intelligent workflow analyzes company data, detects tech stack,
            and generates personalized outreach emails for hot prospects.
          </p>
          <div className="mt-10 flex items-center justify-center gap-x-6">
            <a
              href="#try-now"
              className="rounded-md bg-primary-600 px-6 py-3 text-base font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600 transition-colors"
            >
              Try Demo
            </a>
            <a
              href="#how-it-works"
              className="text-base font-semibold leading-7 text-gray-900 hover:text-primary-600 transition-colors"
            >
              Learn more <span aria-hidden="true">→</span>
            </a>
          </div>
        </div>

        <div className="mt-16 flow-root sm:mt-24">
          <div className="rounded-xl bg-gray-900/5 p-2 ring-1 ring-inset ring-gray-900/10 lg:rounded-2xl lg:p-4">
            <div className="grid grid-cols-1 gap-8 sm:grid-cols-3">
              <div className="text-center">
                <div className="text-4xl font-bold text-primary-600">70+</div>
                <div className="mt-2 text-sm text-gray-600">Hot Lead Score</div>
              </div>
              <div className="text-center">
                <div className="text-4xl font-bold text-primary-600">30s</div>
                <div className="mt-2 text-sm text-gray-600">Processing Time</div>
              </div>
              <div className="text-center">
                <div className="text-4xl font-bold text-primary-600">100%</div>
                <div className="mt-2 text-sm text-gray-600">Automated</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
