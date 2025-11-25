'use client';

import ErrorBoundary from '@/components/ErrorBoundary';
import PartnershipDashboard from '@/components/partnership/PartnershipDashboard';

export default function PartnershipPage() {
  return (
    <ErrorBoundary>
      <PartnershipDashboard />
    </ErrorBoundary>
  );
}
