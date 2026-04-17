export default function WorkflowDiagram() {
  const steps = [
    {
      number: 1,
      title: 'Form Submission',
      description: 'Lead submits contact information',
      icon: '📝',
    },
    {
      number: 2,
      title: 'Email Validation',
      description: 'Extract domain and validate business email',
      icon: '✉️',
    },
    {
      number: 3,
      title: 'Website Scraping',
      description: 'Fetch and analyze company website',
      icon: '🌐',
    },
    {
      number: 4,
      title: 'Tech Stack Detection',
      description: 'Identify Mailchimp, HubSpot, Salesforce, ActiveCampaign',
      icon: '🔧',
    },
    {
      number: 5,
      title: 'AI Analysis',
      description: 'Extract company size, industry, revenue, pain points',
      icon: '🤖',
    },
    {
      number: 6,
      title: 'Lead Scoring',
      description: 'Calculate ICP fit score (0-100)',
      icon: '📊',
    },
    {
      number: 7,
      title: 'Smart Routing',
      description: 'Hot (70+), Warm (40-69), Cold (<40)',
      icon: '🎯',
    },
    {
      number: 8,
      title: 'Email Generation',
      description: 'AI creates personalized outreach for hot leads',
      icon: '✨',
    },
  ]

  return (
    <div className="relative">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {steps.map((step, index) => (
          <div
            key={step.number}
            className="relative bg-white rounded-lg shadow-md p-6 border-2 border-gray-100 hover:border-primary-300 transition-all hover:shadow-lg"
          >
            <div className="flex items-start space-x-4">
              <div className="flex-shrink-0">
                <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center text-2xl">
                  {step.icon}
                </div>
              </div>
              <div className="flex-1 min-w-0">
                <div className="text-sm font-semibold text-primary-600 mb-1">
                  Step {step.number}
                </div>
                <h3 className="text-base font-bold text-gray-900 mb-2">
                  {step.title}
                </h3>
                <p className="text-sm text-gray-600">
                  {step.description}
                </p>
              </div>
            </div>

            {index < steps.length - 1 && (
              <div className="hidden lg:block absolute top-1/2 -right-3 transform -translate-y-1/2">
                <svg
                  className="w-6 h-6 text-primary-300"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M9 5l7 7-7 7"
                  />
                </svg>
              </div>
            )}
          </div>
        ))}
      </div>

      <div className="mt-12 bg-gradient-to-r from-primary-50 to-blue-50 rounded-lg p-8">
        <h3 className="text-xl font-bold text-gray-900 mb-4">
          Scoring Criteria
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
          <div className="bg-white rounded-lg p-4 shadow-sm">
            <div className="text-2xl font-bold text-primary-600">30pts</div>
            <div className="text-sm text-gray-600 mt-1">Tech Stack Match</div>
          </div>
          <div className="bg-white rounded-lg p-4 shadow-sm">
            <div className="text-2xl font-bold text-primary-600">25pts</div>
            <div className="text-sm text-gray-600 mt-1">Company Size (50-500)</div>
          </div>
          <div className="bg-white rounded-lg p-4 shadow-sm">
            <div className="text-2xl font-bold text-primary-600">20pts</div>
            <div className="text-sm text-gray-600 mt-1">SaaS/Tech Industry</div>
          </div>
          <div className="bg-white rounded-lg p-4 shadow-sm">
            <div className="text-2xl font-bold text-primary-600">15pts</div>
            <div className="text-sm text-gray-600 mt-1">Revenue ($5M-$50M)</div>
          </div>
          <div className="bg-white rounded-lg p-4 shadow-sm">
            <div className="text-2xl font-bold text-primary-600">10pts</div>
            <div className="text-sm text-gray-600 mt-1">Growth Signals</div>
          </div>
        </div>
      </div>
    </div>
  )
}
