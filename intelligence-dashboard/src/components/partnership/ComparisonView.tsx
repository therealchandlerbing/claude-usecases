import React from 'react';
import { TrendingUp, Clock, ChevronRight, Target } from 'lucide-react';
import { PartnerType } from './data/partnerTypes';

interface ComparisonViewProps {
  partnerTypes: Record<string, PartnerType>;
}

const ComparisonView: React.FC<ComparisonViewProps> = ({ partnerTypes }) => {
  const partners = ['jv', 'brazil', 'uscorp', 'foundation'];

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Metrics Comparison */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-6 hover:shadow-md transition-shadow duration-300">
        <h2 className="text-lg font-bold text-gray-900 mb-6 flex items-center gap-2">
          <Target className="w-5 h-5 text-blue-600" />
          Partnership Metrics Comparison
        </h2>
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b-2 border-gray-200">
                <th className="text-left py-4 px-4 font-bold text-gray-700 bg-gray-50 rounded-tl-lg">Metric</th>
                <th className="text-center py-4 px-4 font-bold text-gray-700 bg-gray-50">JV Partners</th>
                <th className="text-center py-4 px-4 font-bold text-gray-700 bg-gray-50">Brazil Tech</th>
                <th className="text-center py-4 px-4 font-bold text-gray-700 bg-gray-50">US Corporate/VC</th>
                <th className="text-center py-4 px-4 font-bold text-gray-700 bg-gray-50 rounded-tr-lg">Foundations</th>
              </tr>
            </thead>
            <tbody>
              <tr className="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                <td className="py-4 px-4 text-gray-600 font-medium">Partnerships Explored</td>
                <td className="py-4 px-4 text-center font-semibold">{partnerTypes.jv.metrics.explored}</td>
                <td className="py-4 px-4 text-center font-semibold">{partnerTypes.brazil.metrics.explored}</td>
                <td className="py-4 px-4 text-center font-semibold">{partnerTypes.uscorp.metrics.explored}</td>
                <td className="py-4 px-4 text-center font-semibold">{partnerTypes.foundation.metrics.explored}</td>
              </tr>
              <tr className="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                <td className="py-4 px-4 text-gray-600 font-medium">Partnerships Closed</td>
                <td className="py-4 px-4 text-center font-semibold">{partnerTypes.jv.metrics.closed}</td>
                <td className="py-4 px-4 text-center font-semibold">{partnerTypes.brazil.metrics.closed}</td>
                <td className="py-4 px-4 text-center font-semibold">{partnerTypes.uscorp.metrics.closed}</td>
                <td className="py-4 px-4 text-center font-semibold">{partnerTypes.foundation.metrics.closed}</td>
              </tr>
              <tr className="border-b border-gray-100 bg-gradient-to-r from-blue-50/50 via-green-50/30 to-blue-50/50">
                <td className="py-4 px-4 text-gray-700 font-bold">Success Rate</td>
                <td className="py-4 px-4 text-center">
                  <span className="inline-flex items-center px-3 py-1 rounded-full bg-orange-100 text-orange-800 font-bold text-sm">
                    {partnerTypes.jv.metrics.successRate}%
                  </span>
                </td>
                <td className="py-4 px-4 text-center">
                  <span className="inline-flex items-center px-3 py-1 rounded-full bg-green-100 text-green-800 font-bold text-sm">
                    {partnerTypes.brazil.metrics.successRate}%
                  </span>
                </td>
                <td className="py-4 px-4 text-center">
                  <span className="inline-flex items-center px-3 py-1 rounded-full bg-orange-100 text-orange-800 font-bold text-sm">
                    {partnerTypes.uscorp.metrics.successRate}%
                  </span>
                </td>
                <td className="py-4 px-4 text-center">
                  <span className="inline-flex items-center px-3 py-1 rounded-full bg-orange-100 text-orange-800 font-bold text-sm">
                    {partnerTypes.foundation.metrics.successRate}%
                  </span>
                </td>
              </tr>
              <tr className="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                <td className="py-4 px-4 text-gray-600 font-medium">Avg Timeline (months)</td>
                <td className="py-4 px-4 text-center font-semibold">{partnerTypes.jv.metrics.avgTimeline}</td>
                <td className="py-4 px-4 text-center font-semibold">{partnerTypes.brazil.metrics.avgTimeline}</td>
                <td className="py-4 px-4 text-center">
                  <span className="inline-flex items-center gap-1 text-green-700 font-bold">
                    {partnerTypes.uscorp.metrics.avgTimeline}
                    <TrendingUp className="w-3 h-3" />
                  </span>
                </td>
                <td className="py-4 px-4 text-center font-semibold">{partnerTypes.foundation.metrics.avgTimeline}</td>
              </tr>
              <tr className="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                <td className="py-4 px-4 text-gray-600 font-medium">Approach</td>
                <td className="py-4 px-4 text-center text-xs text-gray-600">{partnerTypes.jv.metrics.approach}</td>
                <td className="py-4 px-4 text-center text-xs text-gray-600">{partnerTypes.brazil.metrics.approach}</td>
                <td className="py-4 px-4 text-center text-xs text-gray-600">{partnerTypes.uscorp.metrics.approach}</td>
                <td className="py-4 px-4 text-center text-xs text-gray-600">{partnerTypes.foundation.metrics.approach}</td>
              </tr>
              <tr className="hover:bg-gray-50 transition-colors">
                <td className="py-4 px-4 text-gray-600 font-medium">Decision Style</td>
                <td className="py-4 px-4 text-center text-xs text-gray-600">{partnerTypes.jv.metrics.decisionStyle}</td>
                <td className="py-4 px-4 text-center text-xs text-gray-600">{partnerTypes.brazil.metrics.decisionStyle}</td>
                <td className="py-4 px-4 text-center text-xs text-gray-600">{partnerTypes.uscorp.metrics.decisionStyle}</td>
                <td className="py-4 px-4 text-center text-xs text-gray-600">{partnerTypes.foundation.metrics.decisionStyle}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      {/* Key Insights */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white rounded-xl shadow-sm border border-green-100 p-6 hover:shadow-md transition-shadow duration-300">
          <h3 className="text-sm font-bold text-green-800 mb-5 flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-green-500 to-emerald-600 flex items-center justify-center shadow-sm">
              <TrendingUp className="w-4 h-4 text-white" />
            </div>
            Highest Success Rates
          </h3>
          <div className="space-y-4">
            <div className="p-4 bg-gradient-to-br from-green-50 to-emerald-50 border-2 border-green-300 rounded-xl shadow-sm">
              <div className="flex justify-between items-start mb-3">
                <div>
                  <div className="font-bold text-gray-900">Brazilian Tech Transfer</div>
                  <div className="text-xs text-gray-600 mt-1">Relationship-first approach pays off</div>
                </div>
                <div className="text-3xl font-bold text-green-700">60%</div>
              </div>
            </div>
            <div className="space-y-2 text-xs text-gray-700">
              <div className="flex items-start gap-2">
                <ChevronRight className="w-3 h-3 text-green-600 mt-0.5 flex-shrink-0" />
                <span className="leading-relaxed">Strong cultural fit and mission alignment</span>
              </div>
              <div className="flex items-start gap-2">
                <ChevronRight className="w-3 h-3 text-green-600 mt-0.5 flex-shrink-0" />
                <span className="leading-relaxed">Clear institutional needs with urgent mandates</span>
              </div>
              <div className="flex items-start gap-2">
                <ChevronRight className="w-3 h-3 text-green-600 mt-0.5 flex-shrink-0" />
                <span className="leading-relaxed">360's unique positioning in Brazil ecosystem</span>
              </div>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-sm border border-blue-100 p-6 hover:shadow-md transition-shadow duration-300">
          <h3 className="text-sm font-bold text-blue-800 mb-5 flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center shadow-sm">
              <Clock className="w-4 h-4 text-white" />
            </div>
            Fastest Timelines
          </h3>
          <div className="space-y-4">
            <div className="p-4 bg-gradient-to-br from-blue-50 to-indigo-50 border-2 border-blue-300 rounded-xl shadow-sm">
              <div className="flex justify-between items-start mb-3">
                <div>
                  <div className="font-bold text-gray-900">US Corporate/VC</div>
                  <div className="text-xs text-gray-600 mt-1">Fast decisions when pain point is clear</div>
                </div>
                <div className="text-3xl font-bold text-blue-700">4.2mo</div>
              </div>
            </div>
            <div className="space-y-2 text-xs text-gray-700">
              <div className="flex items-start gap-2">
                <ChevronRight className="w-3 h-3 text-blue-600 mt-0.5 flex-shrink-0" />
                <span className="leading-relaxed">Efficiency-driven decision culture</span>
              </div>
              <div className="flex items-start gap-2">
                <ChevronRight className="w-3 h-3 text-blue-600 mt-0.5 flex-shrink-0" />
                <span className="leading-relaxed">Clear budget authority and ROI focus</span>
              </div>
              <div className="flex items-start gap-2">
                <ChevronRight className="w-3 h-3 text-blue-600 mt-0.5 flex-shrink-0" />
                <span className="leading-relaxed">Internal champions can move quickly</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Strategic Recommendations */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-6 hover:shadow-md transition-shadow duration-300">
        <h3 className="text-sm font-bold text-gray-900 mb-6 flex items-center gap-2">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center shadow-sm">
            <Target className="w-4 h-4 text-white" />
          </div>
          Strategic Recommendations by Partner Type
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {partners.map((key) => {
            const partner = partnerTypes[key];
            const recommendations = [
              {
                jv: 'Invest 6-9 months in relationship before structure discussions',
                brazil: 'Lead with relationship building and cultural competence',
                uscorp: 'Lead with clear ROI and efficiency gains',
                foundation: 'Build program officer champion relationships early'
              },
              {
                jv: 'Test working relationship through pilots before formalizing JV',
                brazil: 'Use Portuguese capability and local partnerships for credibility',
                uscorp: 'Structure phased pilots that demonstrate value quickly',
                foundation: 'Emphasize capacity building and participatory approaches'
              },
              {
                jv: 'Budget $25K-$50K for legal/operational complexity',
                brazil: 'Expect 3-4 relationship meetings before contract talks',
                uscorp: 'Identify clear internal champion with budget authority',
                foundation: 'Align timing with Q1/Q3 funding cycles'
              }
            ];

            return (
              <div key={key} className="group border border-gray-200 rounded-xl p-5 hover:border-blue-300 hover:shadow-md transition-all duration-200 bg-gradient-to-br from-white to-gray-50/30">
                <div className="font-bold text-gray-900 mb-3 pb-2 border-b border-gray-200">{partner.name}</div>
                <div className="space-y-2.5 text-xs text-gray-700">
                  {recommendations.map((rec, idx) => (
                    <div key={idx} className="flex items-start gap-2 p-2 rounded-lg hover:bg-blue-50 transition-colors">
                      <div className="w-1.5 h-1.5 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 mt-1.5 flex-shrink-0" />
                      <span className="leading-relaxed">{rec[key as keyof typeof rec]}</span>
                    </div>
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default ComparisonView;
