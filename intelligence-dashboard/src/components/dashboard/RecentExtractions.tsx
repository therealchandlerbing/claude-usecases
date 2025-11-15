import { formatDistanceToNow } from 'date-fns';

interface Extraction {
  id: string;
  created_at: string;
  meeting_type: string;
  source_file_name: string;
  completeness_score: number;
  auto_quality_rating: string;
  flagged_for_review: boolean;
  entities_created: number;
  user_quality_rating?: string;
}

export default function RecentExtractions({ extractions }: { extractions: Extraction[] }) {
  if (extractions.length === 0) {
    return (
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Recent Extractions</h3>
        <div className="flex items-center justify-center h-32 text-gray-500">
          No extractions yet. Start extracting intelligence from meetings!
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg shadow">
      <div className="p-6 border-b border-gray-200">
        <h3 className="text-lg font-semibold text-gray-900">Recent Extractions</h3>
      </div>
      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Meeting
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Type
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Quality
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Completeness
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Entities
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Time
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {extractions.map((extraction) => (
              <tr key={extraction.id} className="hover:bg-gray-50">
                <td className="px-6 py-4">
                  <div className="flex items-center">
                    <div className="text-sm font-medium text-gray-900 truncate max-w-xs">
                      {extraction.source_file_name || 'Unnamed meeting'}
                    </div>
                    {extraction.flagged_for_review && (
                      <span className="ml-2 inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-red-100 text-red-800">
                        Flagged
                      </span>
                    )}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <span className="text-sm text-gray-500">{extraction.meeting_type || '—'}</span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <QualityBadge rating={extraction.user_quality_rating || extraction.auto_quality_rating} />
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="flex items-center">
                    <div className="w-24 bg-gray-200 rounded-full h-2 mr-2">
                      <div
                        className={`h-2 rounded-full ${getCompletenessColor(extraction.completeness_score)}`}
                        style={{ width: `${extraction.completeness_score}%` }}
                      />
                    </div>
                    <span className="text-sm text-gray-600">{extraction.completeness_score || 0}%</span>
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {extraction.entities_created}
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {formatDistanceToNow(new Date(extraction.created_at), { addSuffix: true })}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function QualityBadge({ rating }: { rating: string }) {
  const colors = {
    excellent: 'bg-green-100 text-green-800',
    good: 'bg-blue-100 text-blue-800',
    fair: 'bg-yellow-100 text-yellow-800',
    poor: 'bg-red-100 text-red-800',
  };

  return (
    <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${colors[rating as keyof typeof colors] || 'bg-gray-100 text-gray-800'}`}>
      {rating || 'pending'}
    </span>
  );
}

function getCompletenessColor(score: number): string {
  if (!score) return 'bg-gray-300';
  if (score >= 85) return 'bg-green-500';
  if (score >= 70) return 'bg-blue-500';
  if (score >= 55) return 'bg-yellow-500';
  return 'bg-red-500';
}
