import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { LineChart as LineChartIcon, Loader2 } from 'lucide-react';

interface TrendGraphProps {
  data: any;
  loading: boolean;
}

export function TrendGraph({ data, loading }: TrendGraphProps) {
  if (loading) {
    return (
      <div className="flex items-center justify-center h-96 bg-white rounded-lg shadow-lg">
        <Loader2 className="h-8 w-8 text-blue-600 animate-spin" />
      </div>
    );
  }

  if (!data) {
    return (
      <div className="flex flex-col items-center justify-center h-96 bg-white rounded-lg shadow-lg">
        <LineChartIcon className="h-12 w-12 text-gray-400 mb-4" />
        <p className="text-gray-600">Submit keywords to see trend analysis</p>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <div className="h-[600px]">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis 
              dataKey="date" 
              tickFormatter={(date) => new Date(date).toLocaleDateString()}
            />
            <YAxis 
              scale="log"
              domain={['auto', 'auto']}
              tickFormatter={(value) => Math.round(value)}
            />
            <Tooltip
              labelFormatter={(date) => new Date(date).toLocaleDateString()}
              formatter={(value) => [Math.round(Number(value)), '']}
            />
            <Legend />
            {Object.keys(data[0] || {}).filter(key => key !== 'date').map((key, index) => (
              <Line
                key={key}
                type="monotone"
                dataKey={key}
                stroke={`hsl(${index * 137.5 % 360}, 70%, 50%)`}
                strokeWidth={2}
                dot={false}
              />
            ))}
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}