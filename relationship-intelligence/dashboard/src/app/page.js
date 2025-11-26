'use client';

import { useState, useEffect } from 'react';
import RelationshipIntelligenceDashboard from '../components/RelationshipIntelligenceDashboard';
import { fetchActionData, fetchIntelligenceData, updatePushStatus, pushToAsana } from '../lib/supabase';

export default function Home() {
  const [actionData, setActionData] = useState({
    pendingReview: [],
    attentionQueue: [],
    portfolioHealth: {}
  });
  const [intelligenceData, setIntelligenceData] = useState({
    personas: [],
    services: [],
    competitors: []
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadData();
  }, []);

  async function loadData() {
    try {
      setLoading(true);
      const [action, intelligence] = await Promise.all([
        fetchActionData(),
        fetchIntelligenceData()
      ]);
      setActionData(action);
      setIntelligenceData(intelligence);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  async function handleAction(action, item) {
    try {
      switch (action) {
        case 'approve':
          await updatePushStatus(item.table, item.id, 'approved');
          break;
        case 'reject':
          await updatePushStatus(item.table, item.id, 'rejected');
          break;
        case 'push_to_asana':
          await pushToAsana(item);
          break;
        default:
          console.log('Unknown action:', action);
      }
      // Reload data after action
      await loadData();
    } catch (err) {
      console.error('Action failed:', err);
      alert('Action failed: ' + err.message);
    }
  }

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading intelligence data...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center text-red-600">
          <p className="text-xl font-semibold">Error loading data</p>
          <p className="mt-2">{error}</p>
          <button
            onClick={loadData}
            className="mt-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
          >
            Retry
          </button>
        </div>
      </div>
    );
  }

  return (
    <main>
      <RelationshipIntelligenceDashboard
        actionData={actionData}
        intelligenceData={intelligenceData}
        onAction={handleAction}
      />
    </main>
  );
}
