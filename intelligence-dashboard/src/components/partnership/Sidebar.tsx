import React from 'react';
import { Target, AlertCircle, CheckCircle, Clock, DollarSign, TrendingUp } from 'lucide-react';
import { PartnerType } from './data/partnerTypes';

interface SidebarProps {
  currentPartner: PartnerType;
}

const Sidebar: React.FC<SidebarProps> = ({ currentPartner }) => {
  return (
    <div className="space-y-4">
      {/* Strategic Framing */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5 hover:shadow-md transition-shadow duration-300">
        <div className="flex items-center gap-3 mb-4">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center shadow-sm">
            <Target className="w-4 h-4 text-white" />
          </div>
          <h3 className="text-sm font-bold text-gray-900">Strategic Framing</h3>
        </div>
        <div className="space-y-4 text-xs">
          <div className="p-3 bg-gray-50 rounded-lg border border-gray-200">
            <div className="font-semibold text-gray-700 mb-1.5">Their Past Experience:</div>
            <p className="text-gray-600 leading-relaxed">{currentPartner.framing.past}</p>
          </div>
          <div className="p-3 bg-blue-50 rounded-lg border border-blue-200">
            <div className="font-semibold text-blue-700 mb-1.5">360 Approach:</div>
            <p className="text-blue-900 leading-relaxed">{currentPartner.framing.new}</p>
          </div>
          <div className="p-3 bg-gradient-to-br from-indigo-50 to-blue-50 rounded-lg border-2 border-indigo-300 shadow-sm">
            <div className="font-semibold text-indigo-900 mb-1.5 flex items-center gap-1">
              <TrendingUp className="w-3 h-3" />
              Key Message:
            </div>
            <p className="text-indigo-800 font-medium leading-relaxed">{currentPartner.framing.key}</p>
          </div>
        </div>
      </div>

      {/* Walk-Away Signals */}
      <div className="bg-white rounded-xl shadow-sm border border-red-100 p-5 hover:shadow-md transition-shadow duration-300">
        <div className="flex items-center gap-3 mb-4">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-red-500 to-orange-600 flex items-center justify-center shadow-sm">
            <AlertCircle className="w-4 h-4 text-white" />
          </div>
          <h3 className="text-sm font-bold text-red-800">Walk-Away Signals</h3>
        </div>
        <div className="space-y-2 max-h-80 overflow-y-auto pr-2 custom-scrollbar">
          {currentPartner.walkAway.map((signal, idx) => (
            <div key={idx} className="group flex items-start gap-2 text-xs p-2.5 rounded-lg hover:bg-red-50 transition-colors">
              <div className="w-1.5 h-1.5 rounded-full bg-red-500 mt-1.5 flex-shrink-0 group-hover:scale-125 transition-transform" />
              <span className="text-gray-700 leading-relaxed">{signal}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Success Patterns */}
      <div className="bg-white rounded-xl shadow-sm border border-green-100 p-5 hover:shadow-md transition-shadow duration-300">
        <div className="flex items-center gap-3 mb-4">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-green-500 to-emerald-600 flex items-center justify-center shadow-sm">
            <CheckCircle className="w-4 h-4 text-white" />
          </div>
          <h3 className="text-sm font-bold text-green-800">Success Patterns</h3>
        </div>
        <div className="space-y-4 text-xs">
          <div className="p-3 bg-green-50/50 rounded-lg border border-green-200">
            <div className="font-semibold text-green-700 mb-2 flex items-center gap-1.5">
              <Clock className="w-3 h-3" />
              Timeline
            </div>
            <p className="text-gray-700 leading-relaxed">{currentPartner.successPatterns.timeline}</p>
            <p className="text-gray-600 mt-1.5 text-xs">{currentPartner.successPatterns.touchpoints}</p>
          </div>

          <div>
            <div className="font-semibold text-gray-700 mb-2">Stages</div>
            <div className="space-y-1.5">
              {currentPartner.successPatterns.stages.map((stage, idx) => (
                <div key={idx} className="flex items-start gap-2 text-xs text-gray-600 p-2 bg-gray-50 rounded border border-gray-200">
                  <div className="flex-shrink-0 w-5 h-5 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 text-white text-[10px] font-bold flex items-center justify-center shadow-sm">
                    {idx + 1}
                  </div>
                  <span className="leading-relaxed pt-0.5">{stage}</span>
                </div>
              ))}
            </div>
          </div>

          <div>
            <div className="font-semibold text-gray-700 mb-2">Predictors of Success</div>
            <div className="space-y-1.5">
              {currentPartner.successPatterns.predictors.map((predictor, idx) => (
                <div key={idx} className="flex items-start gap-2 text-xs text-gray-700 p-2 hover:bg-green-50 rounded transition-colors">
                  <CheckCircle className="w-3 h-3 text-green-600 mt-0.5 flex-shrink-0" />
                  <span className="leading-relaxed">{predictor}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="p-3 bg-gradient-to-br from-blue-50 to-indigo-50 rounded-lg border border-blue-200">
            <div className="font-semibold text-blue-700 mb-2 flex items-center gap-1.5">
              <DollarSign className="w-3 h-3" />
              Typical Scope
            </div>
            <div className="space-y-1">
              {currentPartner.successPatterns.scope.map((item, idx) => (
                <div key={idx} className="text-gray-700 leading-relaxed">{item}</div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
