'use client';

import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import MetricsCards from '@/components/dashboard/MetricsCards';
import QualityTrend from '@/components/dashboard/QualityTrend';
import TemplatePerformance from '@/components/dashboard/TemplatePerformance';
import RecentExtractions from '@/components/dashboard/RecentExtractions';

interface DashboardMetrics {
  total_extractions_7d: number;
  avg_completeness_7d: number;
  avg_user_rating_7d: number;
  flagged_rate_7d: number;
  trend_extractions: number;
  trend_completeness: number;
  trend_rating: number;
}

export default function Dashboard() {
  const [metrics, setMetrics] = useState<DashboardMetrics | null>(null);
  const [recentExtractions, setRecentExtractions] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDashboardData();

    // Subscribe to real-time updates
    const channel = supabase
      .channel('dashboard-updates')
      .on(
        'postgres_changes',
        { event: '*', schema: 'public', table: 'extractions' },
        (payload) => {
          console.log('Database change detected:', payload);
          fetchDashboardData();
        }
      )
      .subscribe();

    return () => {
      channel.unsubscribe();
    };
  }, []);

  async function fetchDashboardData() {
    try {
      // Fetch metrics using the database function
      const { data: metricsData, error: metricsError } = await supabase
        .rpc('get_dashboard_metrics');

      if (metricsError) {
        console.error('Error fetching metrics:', metricsError);
      } else {
        setMetrics(metricsData);
      }

      // Fetch recent extractions
      const { data: extractionsData, error: extractionsError } = await supabase
        .from('extractions')
        .select('*')
        .order('created_at', { ascending: false })
        .limit(10);

      if (extractionsError) {
        console.error('Error fetching extractions:', extractionsError);
      } else {
        setRecentExtractions(extractionsData || []);
      }

      setLoading(false);
    } catch (error) {
      console.error('Error in fetchDashboardData:', error);
      setLoading(false);
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gray-50">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading dashboard...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">
                Intelligence Quality Dashboard
              </h1>
              <p className="mt-1 text-sm text-gray-600">
                Real-time monitoring of partnership, funding, and stakeholder intelligence extraction
              </p>
            </div>
            <div className="flex items-center space-x-2">
              <div className="h-2 w-2 bg-green-500 rounded-full animate-pulse"></div>
              <span className="text-sm text-gray-600">Live</span>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Metrics Cards */}
        {metrics && <MetricsCards metrics={metrics} />}

        {/* Charts Row */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-6">
          <QualityTrend />
          <TemplatePerformance />
        </div>

        {/* Recent Activity */}
        <div className="mt-6">
          <RecentExtractions extractions={recentExtractions} />
        </div>
      </div>
    </div>
  );
}
