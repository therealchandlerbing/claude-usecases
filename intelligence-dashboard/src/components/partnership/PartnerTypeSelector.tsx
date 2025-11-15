import React from 'react';
import { PartnerType } from './data/partnerTypes';
import { PartnerTypeKey } from './PartnershipDashboard';

interface PartnerTypeSelectorProps {
  selectedPartner: PartnerTypeKey;
  setSelectedPartner: (key: PartnerTypeKey) => void;
  partnerTypes: Record<string, PartnerType>;
}

const PartnerTypeSelector: React.FC<PartnerTypeSelectorProps> = ({
  selectedPartner,
  setSelectedPartner,
  partnerTypes,
}) => {
  const partnerKeys: PartnerTypeKey[] = ['jv', 'brazil', 'uscorp', 'foundation'];

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
      {partnerKeys.map((key) => {
        const partner = partnerTypes[key];
        const isSelected = selectedPartner === key;

        return (
          <button
            key={key}
            onClick={() => setSelectedPartner(key)}
            className={`group relative p-5 rounded-xl border-2 transition-all duration-300 text-left overflow-hidden ${
              isSelected
                ? 'border-blue-500 bg-gradient-to-br from-blue-50 to-indigo-50 shadow-lg shadow-blue-100'
                : 'border-gray-200 bg-white hover:border-blue-300 hover:shadow-md'
            }`}
          >
            {/* Selected indicator */}
            {isSelected && (
              <div className="absolute top-0 right-0 w-16 h-16">
                <div className="absolute transform rotate-45 bg-blue-600 text-white text-xs font-bold py-1 right-[-35px] top-[10px] w-[100px] text-center shadow-sm">
                  Active
                </div>
              </div>
            )}

            <div className="space-y-3">
              <div>
                <h3 className={`font-bold text-base mb-1 transition-colors ${
                  isSelected ? 'text-blue-900' : 'text-gray-900 group-hover:text-blue-900'
                }`}>
                  {partner.name}
                </h3>
                <p className={`text-xs leading-relaxed ${
                  isSelected ? 'text-blue-700' : 'text-gray-600 group-hover:text-gray-700'
                }`}>
                  {partner.subtitle}
                </p>
              </div>

              <div className="flex items-center gap-3 pt-2 border-t border-gray-200">
                <div className="flex items-center gap-1.5">
                  <div className={`w-2 h-2 rounded-full ${
                    partner.metrics.successRate >= 50 ? 'bg-green-500' :
                    partner.metrics.successRate >= 30 ? 'bg-yellow-500' : 'bg-orange-500'
                  }`} />
                  <span className={`text-xs font-semibold ${
                    isSelected ? 'text-blue-700' : 'text-gray-700'
                  }`}>
                    {partner.metrics.successRate}%
                  </span>
                </div>
                <span className="text-gray-400">•</span>
                <span className={`text-xs ${
                  isSelected ? 'text-blue-600' : 'text-gray-500'
                }`}>
                  {partner.metrics.avgTimeline}mo avg
                </span>
              </div>
            </div>

            {/* Hover effect overlay */}
            <div className={`absolute inset-0 bg-gradient-to-br from-blue-500/0 to-indigo-500/0 ${
              !isSelected && 'group-hover:from-blue-500/5 group-hover:to-indigo-500/5'
            } transition-all duration-300 pointer-events-none rounded-xl`} />
          </button>
        );
      })}
    </div>
  );
};

export default PartnerTypeSelector;
