'use client';

import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';

interface TemplateData {
  template_name: string;
  extraction_count: number;
  avg_completeness: number;
  avg_user_rating: number;
  avg_edit_count: number;
  flagged_rate: number;
  performance_grade: string;
}

export default function TemplatePerformance() {
  const [templates, setTemplates] = useState<TemplateData[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchTemplateData();
  }, []);

  async function fetchTemplateData() {
    try {
      const { data, error } = await supabase.rpc('get_template_performance');

      if (error) {
        console.error('Error fetching template performance:', error);
      } else {
        setTemplates(data || []);
      }
      setLoading(false);
    } catch (error) {
      console.error('Error in fetchTemplateData:', error);
      setLoading(false);
    }
  }

  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Template Performance</h3>
        <div className="flex items-center justify-center h-[300px]">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="text-lg font-semibold text-gray-900 mb-4">
        Template Performance (30 Days)
      </h3>
      {templates.length === 0 ? (
        <div className="flex items-center justify-center h-[300px] text-gray-500">
          No template data available yet
        </div>
      ) : (
        <div className="space-y-4">
          {templates.map((template) => (
            <div
              key={template.template_name}
              className="border border-gray-200 rounded-lg p-4 hover:border-gray-300 transition-colors"
            >
              <div className="flex items-center justify-between mb-2">
                <h4 className="font-medium text-gray-900">{template.template_name}</h4>
                <PerformanceBadge grade={template.performance_grade} />
              </div>
              <div className="grid grid-cols-4 gap-4 text-sm">
                <div>
                  <p className="text-gray-500">Count</p>
                  <p className="font-semibold">{template.extraction_count}</p>
                </div>
                <div>
                  <p className="text-gray-500">Completeness</p>
                  <p className="font-semibold">{template.avg_completeness}%</p>
                </div>
                <div>
                  <p className="text-gray-500">Rating</p>
                  <p className="font-semibold">
                    {template.avg_user_rating ? template.avg_user_rating.toFixed(1) : '—'}/5
                  </p>
                </div>
                <div>
                  <p className="text-gray-500">Avg Edits</p>
                  <p className="font-semibold">{template.avg_edit_count.toFixed(1)}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function PerformanceBadge({ grade }: { grade: string }) {
  const colors = {
    excellent: 'bg-green-100 text-green-800',
    good: 'bg-blue-100 text-blue-800',
    needs_work: 'bg-yellow-100 text-yellow-800',
    poor: 'bg-red-100 text-red-800',
  };

  const labels = {
    excellent: '✅ Excellent',
    good: '✓ Good',
    needs_work: '⚠️ Needs Work',
    poor: '❌ Poor',
  };

  return (
    <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${colors[grade as keyof typeof colors] || 'bg-gray-100 text-gray-800'}`}>
      {labels[grade as keyof typeof labels] || grade}
    </span>
  );
}
