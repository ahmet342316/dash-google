import React, { useState } from 'react';
import { Search, TrendingUp, Globe2, LineChart } from 'lucide-react';
import { FeatureCard } from './components/FeatureCard';
import { AnalysisForm } from './components/AnalysisForm';
import { TrendGraph } from './components/TrendGraph';
import { fetchTrendsData } from './services/trendsApi';

function App() {
  const [loading, setLoading] = useState(false);
  const [trendData, setTrendData] = useState(null);
  const [error, setError] = useState<string | null>(null);

  const handleAnalysis = async (formData: { keywords: string; startDate: string; endDate: string }) => {
    setLoading(true);
    setError(null);
    try {
      const data = await fetchTrendsData(formData.keywords, formData.startDate, formData.endDate);
      setTrendData(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8 flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <TrendingUp className="h-6 w-6 text-blue-600" />
            <h1 className="text-xl font-semibold text-gray-900">Google Trends Analysis</h1>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-12 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">
            Analyze Search Trends Worldwide
          </h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Discover what the world is searching for with our powerful Google Trends analysis tool
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
          <FeatureCard 
            icon={<Search className="h-8 w-8 text-blue-600" />}
            title="Search Analysis"
            description="Compare multiple search terms and analyze their popularity over time"
          />
          <FeatureCard 
            icon={<Globe2 className="h-8 w-8 text-blue-600" />}
            title="Global Insights"
            description="Get insights from different regions and understand geographical trends"
          />
          <FeatureCard 
            icon={<LineChart className="h-8 w-8 text-blue-600" />}
            title="Visual Reports"
            description="View beautiful, interactive charts and export detailed reports"
          />
        </div>

        <div className="space-y-8">
          <div className="bg-white rounded-lg shadow-lg p-6 max-w-3xl mx-auto">
            <h3 className="text-2xl font-semibold text-gray-900 mb-6">Start Your Analysis</h3>
            <AnalysisForm onSubmit={handleAnalysis} loading={loading} />
            {error && (
              <div className="mt-4 p-4 bg-red-50 text-red-700 rounded-md">
                {error}
              </div>
            )}
          </div>

          <TrendGraph data={trendData} loading={loading} />
        </div>
      </main>
    </div>
  );
}

export default App;