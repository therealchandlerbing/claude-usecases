import React from 'react';
import { Target, TrendingUp } from 'lucide-react';
import { Pattern } from './data/partnerTypes';

interface PatternDetectionProps {
  patterns: Pattern[];
}

const PatternDetection: React.FC<PatternDetectionProps> = ({ patterns }) => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-6 mb-6 hover:shadow-md transition-shadow duration-300">
      <div className="flex items-center gap-3 mb-5">
        <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center shadow-sm">
          <Target className="w-5 h-5 text-white" />
        </div>
        <div>
          <h2 className="text-lg font-bold text-gray-900">Key Patterns</h2>
          <p className="text-xs text-gray-500">Insights from historical partnerships</p>
        </div>
      </div>

      <div className="space-y-3">
        {patterns.map((pattern, idx) => (
          <div
            key={idx}
            className="group flex items-start gap-4 p-4 bg-gradient-to-r from-gray-50 to-blue-50/30 rounded-lg border border-gray-200 hover:border-blue-300 hover:shadow-sm transition-all duration-200"
          >
            <div className="flex-shrink-0 w-8 h-8 rounded-full bg-white border-2 border-blue-200 flex items-center justify-center shadow-sm group-hover:border-blue-400 transition-colors">
              <TrendingUp className="w-4 h-4 text-blue-600" />
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-sm text-gray-900 leading-relaxed">{pattern.text}</p>
            </div>
            <div className="flex-shrink-0">
              <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-gradient-to-r from-blue-600 to-indigo-600 text-white shadow-sm">
                {pattern.frequency}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PatternDetection;
