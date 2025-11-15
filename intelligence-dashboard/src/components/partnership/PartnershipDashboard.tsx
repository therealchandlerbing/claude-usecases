'use client';

import React, { useState } from 'react';
import { Search, BarChart3 } from 'lucide-react';
import { partnerTypes } from './data/partnerTypes';
import PartnerTypeSelector from './PartnerTypeSelector';
import OverviewMetrics from './OverviewMetrics';
import PatternDetection from './PatternDetection';
import TabbedContent from './TabbedContent';
import Sidebar from './Sidebar';
import ComparisonView from './ComparisonView';

export type PartnerTypeKey = 'jv' | 'brazil' | 'uscorp' | 'foundation';

const PartnershipDashboard = () => {
  const [selectedPartner, setSelectedPartner] = useState<PartnerTypeKey>('jv');
  const [activeTab, setActiveTab] = useState('opportunities');
  const [viewMode, setViewMode] = useState<'detail' | 'compare'>('detail');
  const [searchTerm, setSearchTerm] = useState('');

  const currentPartner = partnerTypes[selectedPartner];

  return (
    <div className="w-full min-h-screen bg-gradient-to-br from-gray-50 via-blue-50/30 to-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="mb-8">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-4xl font-bold text-gray-900 tracking-tight">
                Partnership Intelligence
              </h1>
              <p className="mt-2 text-base text-gray-600">
                360 Social Impact Studios - Strategic Partnership Navigator
              </p>
            </div>
            <div className="hidden lg:flex items-center gap-2 px-4 py-2 bg-white rounded-full shadow-sm border border-gray-200">
              <div className="h-2 w-2 bg-green-500 rounded-full animate-pulse"></div>
              <span className="text-sm font-medium text-gray-700">Live Intelligence</span>
            </div>
          </div>
        </div>

        {/* View Mode Toggle & Search */}
        <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-4 mb-6">
          <div className="inline-flex rounded-lg border border-gray-200 bg-white p-1 shadow-sm">
            <button
              onClick={() => setViewMode('detail')}
              className={`px-4 py-2 rounded-md text-sm font-medium transition-all duration-200 ${
                viewMode === 'detail'
                  ? 'bg-blue-600 text-white shadow-sm'
                  : 'text-gray-700 hover:text-gray-900 hover:bg-gray-50'
              }`}
            >
              Detailed View
            </button>
            <button
              onClick={() => setViewMode('compare')}
              className={`px-4 py-2 rounded-md text-sm font-medium transition-all duration-200 flex items-center gap-2 ${
                viewMode === 'compare'
                  ? 'bg-blue-600 text-white shadow-sm'
                  : 'text-gray-700 hover:text-gray-900 hover:bg-gray-50'
              }`}
            >
              <BarChart3 className="w-4 h-4" />
              Compare All
            </button>
          </div>

          {/* Search */}
          <div className="flex items-center gap-2 bg-white border border-gray-200 rounded-lg px-4 py-2.5 shadow-sm hover:shadow-md transition-shadow sm:w-80 ml-auto">
            <Search className="w-4 h-4 text-gray-400" />
            <input
              type="text"
              placeholder="Search patterns, questions, hesitations..."
              className="flex-1 text-sm outline-none placeholder-gray-400"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>
        </div>

        {/* Partner Type Selector */}
        <PartnerTypeSelector
          selectedPartner={selectedPartner}
          setSelectedPartner={setSelectedPartner}
          partnerTypes={partnerTypes}
        />

        {/* Detailed View */}
        {viewMode === 'detail' && (
          <>
            {/* Overview Metrics */}
            <OverviewMetrics metrics={currentPartner.metrics} />

            {/* Pattern Detection */}
            <PatternDetection patterns={currentPartner.patterns} />

            {/* Main Content Area with Tabs */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
              {/* Left Column - Tabbed Content */}
              <div className="lg:col-span-2">
                <TabbedContent
                  activeTab={activeTab}
                  setActiveTab={setActiveTab}
                  currentPartner={currentPartner}
                />
              </div>

              {/* Right Sidebar */}
              <div className="lg:col-span-1">
                <Sidebar currentPartner={currentPartner} />
              </div>
            </div>
          </>
        )}

        {/* Comparison View */}
        {viewMode === 'compare' && (
          <ComparisonView partnerTypes={partnerTypes} />
        )}
      </div>
    </div>
  );
};

export default PartnershipDashboard;
