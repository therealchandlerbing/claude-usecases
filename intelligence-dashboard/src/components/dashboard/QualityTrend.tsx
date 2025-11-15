'use client';

import { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { supabase } from '@/lib/supabase';

export default function QualityTrend() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchTrendData();
  }, []);

  async function fetchTrendData() {
    try {
      const { data: trendData, error } = await supabase.rpc('get_quality_trend_30d');

      if (error) {
        console.error('Error fetching trend data:', error);
      } else {
        setData(trendData || []);
      }
      setLoading(false);
    } catch (error) {
      console.error('Error in fetchTrendData:', error);
      setLoading(false);
    }
  }

  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Quality Trend (30 Days)</h3>
        <div className="flex items-center justify-center h-[300px]">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="text-lg font-semibold text-gray-900 mb-4">
        Quality Trend (30 Days)
      </h3>
      {data.length === 0 ? (
        <div className="flex items-center justify-center h-[300px] text-gray-500">
          No data available yet
        </div>
      ) : (
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
            <XAxis
              dataKey="date"
              stroke="#9ca3af"
              style={{ fontSize: 12 }}
            />
            <YAxis stroke="#9ca3af" style={{ fontSize: 12 }} />
            <Tooltip
              contentStyle={{
                backgroundColor: 'white',
                border: '1px solid #e5e7eb',
                borderRadius: '0.5rem',
              }}
            />
            <Legend />
            <Line
              type="monotone"
              dataKey="completeness"
              stroke="#3b82f6"
              strokeWidth={2}
              name="Completeness %"
              dot={{ r: 3 }}
            />
            <Line
              type="monotone"
              dataKey="user_rating"
              stroke="#10b981"
              strokeWidth={2}
              name="User Rating"
              dot={{ r: 3 }}
            />
          </LineChart>
        </ResponsiveContainer>
      )}
    </div>
  );
}
