import React from 'react';
import { TrendingUp, TrendingDown, Clock, Target } from 'lucide-react';
import { PartnerMetrics } from './data/partnerTypes';

interface OverviewMetricsProps {
  metrics: PartnerMetrics;
}

const OverviewMetrics: React.FC<OverviewMetricsProps> = ({ metrics }) => {
  return (
    <div className="grid grid-cols-2 lg:grid-cols-6 gap-4 mb-6">
      {/* Explored */}
      <div className="bg-white rounded-xl shadow-sm hover:shadow-md transition-all duration-300 p-5 border border-gray-100 group">
        <div className="flex items-center justify-between mb-2">
          <div className="text-sm font-medium text-gray-600">Explored</div>
          <Target className="w-4 h-4 text-blue-500 group-hover:scale-110 transition-transform" />
        </div>
        <div className="text-3xl font-bold text-gray-900 mb-1">{metrics.explored}</div>
        <div className="text-xs text-gray-500">Last 18-24 months</div>
      </div>

      {/* Closed */}
      <div className="bg-white rounded-xl shadow-sm hover:shadow-md transition-all duration-300 p-5 border border-gray-100 group">
        <div className="flex items-center justify-between mb-2">
          <div className="text-sm font-medium text-gray-600">Closed</div>
          <TrendingUp className="w-4 h-4 text-green-500 group-hover:scale-110 transition-transform" />
        </div>
        <div className="text-3xl font-bold text-gray-900">{metrics.closed}</div>
      </div>

      {/* Success Rate */}
      <div className="bg-gradient-to-br from-green-50 to-emerald-50 rounded-xl shadow-sm hover:shadow-md transition-all duration-300 p-5 border border-green-100 group">
        <div className="flex items-center justify-between mb-2">
          <div className="text-sm font-medium text-green-700">Success Rate</div>
          <div className={`w-8 h-8 rounded-full flex items-center justify-center ${
            metrics.successRate >= 50 ? 'bg-green-500' :
            metrics.successRate >= 30 ? 'bg-yellow-500' : 'bg-orange-500'
          } group-hover:scale-110 transition-transform`}>
            <div className="text-white text-xs font-bold">✓</div>
          </div>
        </div>
        <div className="text-3xl font-bold text-green-900">{metrics.successRate}%</div>
      </div>

      {/* Avg Timeline */}
      <div className="bg-white rounded-xl shadow-sm hover:shadow-md transition-all duration-300 p-5 border border-gray-100 group">
        <div className="flex items-center justify-between mb-2">
          <div className="text-sm font-medium text-gray-600">Avg Timeline</div>
          <Clock className="w-4 h-4 text-blue-500 group-hover:scale-110 transition-transform" />
        </div>
        <div className="text-3xl font-bold text-gray-900 mb-1">{metrics.avgTimeline}mo</div>
        <div className="text-xs text-gray-500">First contact to launch</div>
      </div>

      {/* Approach */}
      <div className="col-span-2 bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl shadow-sm hover:shadow-md transition-all duration-300 p-5 border border-blue-100">
        <div className="text-sm font-medium text-blue-700 mb-2">Approach & Style</div>
        <div className="text-sm font-semibold text-blue-900 mb-1">{metrics.approach}</div>
        <div className="text-xs text-blue-700 flex items-center gap-1">
          <div className="w-1 h-1 bg-blue-500 rounded-full" />
          {metrics.decisionStyle}
        </div>
      </div>
    </div>
  );
};

export default OverviewMetrics;
