import React from 'react';
import { Target, Users, FileText, AlertCircle, ChevronRight, CheckCircle } from 'lucide-react';
import { PartnerType } from './data/partnerTypes';

interface TabbedContentProps {
  activeTab: string;
  setActiveTab: (tab: string) => void;
  currentPartner: PartnerType;
}

const TabbedContent: React.FC<TabbedContentProps> = ({
  activeTab,
  setActiveTab,
  currentPartner,
}) => {
  const tabs = [
    { id: 'opportunities', label: 'Opening Opportunities', icon: Target },
    { id: 'language', label: 'Value Alignment', icon: Users },
    { id: 'questions', label: 'Qualification Questions', icon: FileText },
    { id: 'hesitations', label: 'Common Hesitations', icon: AlertCircle }
  ];

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-md transition-shadow duration-300">
      {/* Tab Navigation */}
      <div className="flex border-b border-gray-200 bg-gray-50/50">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`relative flex-1 px-4 py-4 text-sm font-medium transition-all duration-200 ${
              activeTab === tab.id
                ? 'text-blue-700 bg-white'
                : 'text-gray-600 hover:text-gray-900 hover:bg-gray-100/50'
            }`}
          >
            <div className="flex flex-col items-center justify-center gap-2">
              <tab.icon className={`w-5 h-5 ${
                activeTab === tab.id ? 'text-blue-600' : 'text-gray-400'
              }`} />
              <span className="hidden lg:inline text-xs">{tab.label}</span>
            </div>
            {activeTab === tab.id && (
              <div className="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 to-indigo-600 rounded-t" />
            )}
          </button>
        ))}
      </div>

      {/* Tab Content */}
      <div className="p-6">
        {activeTab === 'opportunities' && (
          <div className="space-y-6 animate-fadeIn">
            <div>
              <h3 className="text-sm font-bold text-gray-900 mb-4 flex items-center gap-2">
                <Target className="w-4 h-4 text-blue-600" />
                What They&apos;re Solving For
              </h3>
              <div className="space-y-4">
                {currentPartner.opportunities.map((opp, idx) => (
                  <div key={idx} className="group border border-gray-200 rounded-xl p-5 hover:border-blue-300 hover:shadow-md transition-all duration-200 bg-gradient-to-br from-white to-gray-50/30">
                    <div className="flex items-start gap-3 mb-3">
                      <div className="flex-shrink-0 w-6 h-6 rounded-full bg-blue-600 text-white text-xs font-bold flex items-center justify-center shadow-sm">
                        {idx + 1}
                      </div>
                      <h4 className="font-semibold text-gray-900 flex-1">{opp.title}</h4>
                    </div>
                    <p className="text-sm text-gray-700 mb-4 pl-9">{opp.description}</p>
                    <div className="space-y-2 pl-9">
                      <div className="text-xs font-semibold text-gray-600 mb-2 flex items-center gap-1">
                        <div className="w-1 h-1 bg-blue-500 rounded-full" />
                        Signals to Watch For:
                      </div>
                      {opp.signals.map((signal, sidx) => (
                        <div key={sidx} className="flex items-start gap-2 text-xs text-gray-600 pl-3">
                          <ChevronRight className="w-3 h-3 text-blue-500 mt-0.5 flex-shrink-0" />
                          <span className="leading-relaxed">{signal}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {activeTab === 'language' && (
          <div className="space-y-6 animate-fadeIn">
            <div>
              <h3 className="text-sm font-bold text-gray-900 mb-4">How to Frame 360&apos;s Work</h3>
              <div className="space-y-2">
                {currentPartner.valueAlignment.frame.map((frame, idx) => (
                  <div key={idx} className="bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-lg p-4 text-sm text-gray-900 shadow-sm hover:shadow-md transition-shadow">
                    <div className="flex items-start gap-2">
                      <div className="text-blue-600 font-bold text-lg">&quot;</div>
                      <div className="flex-1">{frame.replace(/^"|"$/g, '')}</div>
                      <div className="text-blue-600 font-bold text-lg">&quot;</div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            <div>
              <h3 className="text-sm font-bold text-gray-900 mb-4">Cultural Communication</h3>
              <div className="space-y-2">
                {currentPartner.valueAlignment.cultural.map((item, idx) => (
                  <div key={idx} className="flex items-start gap-3 text-sm text-gray-700 p-3 rounded-lg hover:bg-gray-50 transition-colors">
                    <ChevronRight className="w-4 h-4 text-blue-500 mt-0.5 flex-shrink-0" />
                    <span className="leading-relaxed">{item}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pt-4">
              <div className="bg-green-50/50 border border-green-200 rounded-xl p-4">
                <h3 className="text-sm font-bold text-green-800 mb-3 flex items-center gap-2">
                  <CheckCircle className="w-4 h-4" />
                  Signals of Alignment
                </h3>
                <div className="space-y-2">
                  {currentPartner.valueAlignment.alignment.map((item, idx) => (
                    <div key={idx} className="flex items-start gap-2 text-xs text-gray-700">
                      <div className="w-1.5 h-1.5 rounded-full bg-green-500 mt-1.5 flex-shrink-0" />
                      <span className="leading-relaxed">{item}</span>
                    </div>
                  ))}
                </div>
              </div>
              <div className="bg-red-50/50 border border-red-200 rounded-xl p-4">
                <h3 className="text-sm font-bold text-red-800 mb-3 flex items-center gap-2">
                  <AlertCircle className="w-4 h-4" />
                  Signals of Misalignment
                </h3>
                <div className="space-y-2">
                  {currentPartner.valueAlignment.misalignment.map((item, idx) => (
                    <div key={idx} className="flex items-start gap-2 text-xs text-gray-700">
                      <div className="w-1.5 h-1.5 rounded-full bg-red-500 mt-1.5 flex-shrink-0" />
                      <span className="leading-relaxed">{item}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'questions' && (
          <div className="space-y-6 animate-fadeIn">
            {currentPartner.qualificationQuestions.map((section, idx) => (
              <div key={idx}>
                <h3 className="text-sm font-bold text-gray-900 mb-4 flex items-center gap-2">
                  <div className="w-2 h-2 rounded-full bg-blue-600" />
                  {section.category}
                </h3>
                <div className="space-y-3">
                  {section.questions.map((q, qidx) => (
                    <div key={qidx} className="group flex items-start gap-3 p-4 bg-gradient-to-r from-gray-50 to-blue-50/20 rounded-lg border border-gray-200 hover:border-blue-300 hover:shadow-md transition-all duration-200">
                      <div className="flex-shrink-0 w-7 h-7 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 text-white text-xs font-bold flex items-center justify-center shadow-sm">
                        {qidx + 1}
                      </div>
                      <p className="text-sm text-gray-900 leading-relaxed pt-0.5">{q}</p>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        )}

        {activeTab === 'hesitations' && (
          <div className="space-y-4 animate-fadeIn">
            {currentPartner.hesitations.map((item, idx) => (
              <div key={idx} className="border border-gray-200 rounded-xl overflow-hidden hover:shadow-md transition-all duration-200">
                <div className="bg-gradient-to-r from-orange-50 to-amber-50 border-b border-orange-200 p-4">
                  <div className="flex items-start gap-3">
                    <AlertCircle className="w-5 h-5 text-orange-600 flex-shrink-0 mt-0.5" />
                    <div className="font-semibold text-gray-900 text-sm leading-relaxed">&quot;{item.hesitation}&quot;</div>
                  </div>
                </div>
                <div className="p-5 space-y-4 bg-white">
                  <div>
                    <div className="text-xs font-bold text-gray-600 mb-2 uppercase tracking-wide">Response:</div>
                    <p className="text-sm text-gray-900 leading-relaxed">{item.response}</p>
                  </div>
                  <div>
                    <div className="text-xs font-bold text-gray-600 mb-2 uppercase tracking-wide">Follow-up Action:</div>
                    <div className="text-xs text-blue-900 bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-lg p-3 shadow-sm">
                      <div className="flex items-start gap-2">
                        <div className="text-blue-600 font-bold">→</div>
                        <span className="leading-relaxed">{item.action}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default TabbedContent;
