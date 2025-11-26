import React, { useState } from 'react';
import {
  Users, Briefcase, Shield, TrendingUp, Target, AlertTriangle, Zap,
  ChevronRight, ChevronDown, ChevronUp, ExternalLink, Filter, BarChart3,
  Activity, Lightbulb, MessageSquare, Award, Globe, Clock, DollarSign,
  UserCheck, Building, BookOpen, CheckCircle, XCircle, ArrowRight,
  Calendar, RefreshCw, Inbox, Eye, Settings, Bell, Search, LayoutDashboard,
  TrendingDown, Minus, FileText, Send, Archive
} from 'lucide-react';

// ============================================================
// UI COMPONENTS
// ============================================================

const Badge = ({ children, variant = 'default', size = 'md' }) => {
  const variants = {
    default: 'bg-gray-100 text-gray-700',
    success: 'bg-emerald-100 text-emerald-700',
    warning: 'bg-amber-100 text-amber-700',
    danger: 'bg-red-100 text-red-700',
    info: 'bg-blue-100 text-blue-700',
    purple: 'bg-purple-100 text-purple-700'
  };
  const sizes = { sm: 'px-1.5 py-0.5 text-xs', md: 'px-2 py-0.5 text-xs', lg: 'px-3 py-1 text-sm' };
  return <span className={`rounded-full font-medium ${variants[variant]} ${sizes[size]}`}>{children}</span>;
};

const Card = ({ children, className = '' }) => (
  <div className={`bg-white rounded-xl border border-gray-200 shadow-sm ${className}`}>{children}</div>
);

const Button = ({ children, variant = 'default', size = 'md', onClick, className = '' }) => {
  const variants = {
    default: 'bg-gray-100 hover:bg-gray-200 text-gray-700',
    primary: 'bg-blue-600 hover:bg-blue-700 text-white',
    success: 'bg-emerald-600 hover:bg-emerald-700 text-white',
    ghost: 'bg-transparent hover:bg-gray-100 text-gray-600',
    danger: 'bg-red-50 hover:bg-red-100 text-red-600'
  };
  const sizes = { sm: 'px-2 py-1 text-xs', md: 'px-3 py-1.5 text-sm', lg: 'px-4 py-2 text-base' };
  return (
    <button onClick={onClick} className={`rounded-md font-medium transition-colors ${variants[variant]} ${sizes[size]} ${className}`}>
      {children}
    </button>
  );
};

const MetricCard = ({ label, value, subvalue, trend, icon: Icon }) => (
  <div className="bg-white rounded-lg border border-gray-200 p-4">
    <div className="flex items-center justify-between mb-2">
      <span className="text-sm text-gray-500">{label}</span>
      {Icon && <Icon size={16} className="text-gray-400" />}
    </div>
    <div className="text-2xl font-semibold text-gray-900">{value}</div>
    {subvalue && (
      <div className="flex items-center gap-1 mt-1">
        {trend === 'up' && <TrendingUp size={14} className="text-emerald-500" />}
        {trend === 'down' && <TrendingDown size={14} className="text-red-500" />}
        <span className={`text-sm ${trend === 'up' ? 'text-emerald-600' : trend === 'down' ? 'text-red-600' : 'text-gray-500'}`}>{subvalue}</span>
      </div>
    )}
  </div>
);

const ProgressBar = ({ value, max, color = 'blue' }) => {
  const colors = { blue: 'bg-blue-500', emerald: 'bg-emerald-500', amber: 'bg-amber-500', red: 'bg-red-500', purple: 'bg-purple-500' };
  return (
    <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
      <div className={`h-full rounded-full ${colors[color]}`} style={{ width: `${Math.min((value / max) * 100, 100)}%` }} />
    </div>
  );
};

const TemperatureBar = ({ dist, total }) => {
  const colors = { hot: 'bg-red-500', warm: 'bg-amber-400', cool: 'bg-blue-400', cold: 'bg-blue-700' };
  return (
    <div className="flex h-3 rounded-full overflow-hidden">
      {Object.entries(dist).map(([temp, count]) => (
        <div key={temp} className={colors[temp]} style={{ width: `${(count / total) * 100}%` }} title={`${temp}: ${count}`} />
      ))}
    </div>
  );
};

const TemperatureIndicator = ({ temp }) => {
  const config = { hot: '🔥', warm: '🌡', cool: '❄️', cold: '🧊' };
  return <span className="text-sm">{config[temp]} <span className="capitalize text-xs text-gray-500">{temp}</span></span>;
};

const GeoBadge = ({ geo }) => {
  const flags = { brazil: '🇧🇷', north_america: '🇺🇸', europe: '🇪🇺', latin_america: '🌎', asia_pacific: '🌏', global: '🌐' };
  return <span className="text-xs text-gray-500">{flags[geo] || '🌐'} {geo?.replace('_', ' ')}</span>;
};

const ConfidenceDot = ({ level }) => {
  const colors = { high: 'bg-emerald-500', medium: 'bg-amber-500', low: 'bg-red-500' };
  return <span className="inline-flex items-center gap-1 text-xs text-gray-500"><span className={`w-2 h-2 rounded-full ${colors[level]}`}></span>{level}</span>;
};

const PersonaBadge = ({ persona }) => {
  const labels = {
    government_innovation: 'Gov Innovation',
    university_tto: 'University TTO',
    vc_partner: 'VC Partner',
    corporate_innovation: 'Corporate',
    startup_founder: 'Startup',
    foundation_program: 'Foundation',
    research_director: 'Research',
    c_suite_executive: 'C-Suite'
  };
  return <Badge variant="purple" size="sm">{labels[persona] || persona}</Badge>;
};

const SignalTypeBadge = ({ type }) => {
  const config = {
    partnership_interest: { label: 'Partnership', variant: 'success' },
    funding_interest: { label: 'Funding', variant: 'purple' },
    client_interest: { label: 'Client Interest', variant: 'info' },
    budget_signal: { label: 'Budget', variant: 'purple' },
    risk_concern: { label: 'Risk', variant: 'danger' },
    decision_maker_identified: { label: 'Decision Maker', variant: 'info' },
    timeline_shift: { label: 'Timeline', variant: 'warning' }
  };
  const c = config[type] || { label: type.replace('_', ' '), variant: 'default' };
  return <Badge variant={c.variant} size="sm">{c.label}</Badge>;
};

// ============================================================
// ACTION CENTER COMPONENTS
// ============================================================

const RelationshipReviewCard = ({ item, onAction }) => {
  const [expanded, setExpanded] = useState(false);
  return (
    <Card className="p-4">
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <div className="flex items-center gap-2 mb-1">
            <Users size={16} className="text-gray-400" />
            <span className="font-medium text-gray-900">{item.name}</span>
            <ConfidenceDot level={item.confidence} />
          </div>
          <div className="flex items-center gap-2 text-sm text-gray-600 mb-2">
            <span>{item.organization}</span>
            <span className="text-gray-300">•</span>
            <GeoBadge geo={item.geography} />
          </div>
          <div className="flex flex-wrap gap-1.5 mb-2">
            <PersonaBadge persona={item.persona_type} />
            <Badge variant="info">{item.stage}</Badge>
            <Badge>{item.source?.replace('_', ' ')}</Badge>
            {item.strategic_fit_score && <Badge variant="success">Fit: {item.strategic_fit_score}/10</Badge>}
          </div>
          {item.introducer_name && <div className="text-xs text-gray-500 mb-1">Introduced by: <span className="font-medium">{item.introducer_name}</span></div>}
          <div className="text-xs text-gray-400">From: {item.from_meeting}</div>
        </div>
        <button onClick={() => setExpanded(!expanded)} className="text-gray-400 hover:text-gray-600">
          {expanded ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
        </button>
      </div>
      {expanded && item.notes && <div className="mt-3 pt-3 border-t border-gray-100"><p className="text-sm text-gray-600">{item.notes}</p></div>}
      <div className="flex items-center gap-2 mt-4 pt-3 border-t border-gray-100">
        <Button variant="success" size="sm" onClick={() => onAction('push', item)}>
          <span className="flex items-center gap-1"><ArrowRight size={14} />Push to Asana</span>
        </Button>
        <Button variant="default" size="sm" onClick={() => onAction('keep', item)}>Keep in Supabase</Button>
        <Button variant="ghost" size="sm" onClick={() => onAction('decline', item)}>Decline</Button>
      </div>
    </Card>
  );
};

const ServiceInterestCard = ({ item, onAction }) => (
  <Card className="p-4">
    <div className="flex items-start justify-between mb-3">
      <div>
        <div className="flex items-center gap-2 mb-1">
          <Briefcase size={16} className="text-purple-500" />
          <span className="font-medium text-gray-900">{item.service}</span>
          <Badge variant={item.interest_level === 'evaluating' ? 'success' : item.interest_level === 'curious' ? 'info' : 'default'}>
            {item.interest_level}
          </Badge>
        </div>
        <div className="text-sm text-gray-600">{item.relationship_name}</div>
      </div>
      {item.estimated_value && <div className="text-right"><div className="text-lg font-semibold text-emerald-600">${(item.estimated_value / 1000).toFixed(0)}K</div><div className="text-xs text-gray-400">est. value</div></div>}
    </div>
    <p className="text-sm text-gray-600 mb-2">{item.context}</p>
    <div className="flex items-center gap-3 text-xs text-gray-500 mb-3">
      {item.budget_confirmed && <span className="text-emerald-600">✓ Budget confirmed</span>}
      {item.timeline_confirmed && <span className="text-emerald-600">✓ Timeline confirmed</span>}
      <ConfidenceDot level={item.confidence} />
    </div>
    <div className="flex items-center gap-2 pt-3 border-t border-gray-100">
      <Button variant="success" size="sm" onClick={() => onAction('push', item)}>Add to Pipeline</Button>
      <Button variant="default" size="sm" onClick={() => onAction('keep', item)}>Track Only</Button>
    </div>
  </Card>
);

const CommitmentCard = ({ item, isOurs, onAction }) => (
  <Card className={`p-4 border-l-4 ${isOurs ? 'border-l-blue-500' : 'border-l-purple-500'}`}>
    <div className="flex items-start gap-3">
      <div className={`p-2 rounded-lg ${isOurs ? 'bg-blue-100' : 'bg-purple-100'}`}>
        {isOurs ? <ArrowRight size={16} className="text-blue-600" /> : <Clock size={16} className="text-purple-600" />}
      </div>
      <div className="flex-1">
        <p className="text-gray-900 font-medium mb-1">{item.description}</p>
        <div className="flex items-center gap-2 text-sm text-gray-500 mb-2">
          <span>{item.relationship_name}</span>
          {item.service_context && <><span className="text-gray-300">•</span><Badge size="sm">{item.service_context}</Badge></>}
        </div>
        <div className="flex items-center gap-2 text-xs text-gray-400">
          {item.due_date ? <span className="flex items-center gap-1"><Calendar size={12} />Due: {new Date(item.due_date).toLocaleDateString()}</span> : <span className="italic">No due date ({item.due_date_type})</span>}
        </div>
      </div>
    </div>
    <div className="flex items-center gap-2 mt-3 pt-3 border-t border-gray-100">
      {isOurs ? (
        <><Button variant="success" size="sm" onClick={() => onAction('push', item)}>Create Asana Task</Button><Button variant="default" size="sm" onClick={() => onAction('keep', item)}>Track Only</Button></>
      ) : (
        <><Button variant="primary" size="sm" onClick={() => onAction('push', item)}>Create Reminder</Button><Button variant="default" size="sm" onClick={() => onAction('keep', item)}>Track Only</Button></>
      )}
    </div>
  </Card>
);

const ObjectionCard = ({ item, onAction }) => (
  <Card className="p-4 border-l-4 border-l-amber-500">
    <div className="flex items-start gap-3">
      <div className="p-2 rounded-lg bg-amber-100"><MessageSquare size={16} className="text-amber-600" /></div>
      <div className="flex-1">
        <div className="flex items-center gap-2 mb-1">
          <Badge variant="warning">{item.objection_type}</Badge>
          {item.objection_overcome && <Badge variant="success">Overcome ✓</Badge>}
        </div>
        <p className="text-gray-900 mb-1">"{item.objection_text}"</p>
        <div className="text-sm text-gray-500 mb-2">{item.relationship_name} {item.service_context && `• ${item.service_context}`}</div>
        {item.response_given && <div className="bg-emerald-50 rounded p-2 text-sm text-emerald-800"><span className="font-medium">Response: </span>{item.response_given}</div>}
        {item.what_worked && <div className="text-xs text-emerald-600 mt-1">What worked: {item.what_worked}</div>}
      </div>
    </div>
    <div className="flex items-center gap-2 mt-3 pt-3 border-t border-gray-100">
      <Button variant="success" size="sm" onClick={() => onAction('save', item)}>Save to Playbook</Button>
      <Button variant="ghost" size="sm" onClick={() => onAction('dismiss', item)}>Dismiss</Button>
    </div>
  </Card>
);

const SignalCard = ({ item, onAction }) => (
  <Card className={`p-4 border-l-4 ${item.significance === 'critical' ? 'border-l-red-500' : 'border-l-amber-500'}`}>
    <div className="flex items-start gap-3">
      <div className={`p-2 rounded-lg ${item.significance === 'critical' ? 'bg-red-100' : 'bg-amber-100'}`}>
        <Zap size={16} className={item.significance === 'critical' ? 'text-red-600' : 'text-amber-600'} />
      </div>
      <div className="flex-1">
        <div className="flex items-center gap-2 mb-1">
          <SignalTypeBadge type={item.signal_type} />
          {item.significance === 'critical' && <Badge variant="danger">Critical</Badge>}
        </div>
        <p className="text-gray-900 mb-1">{item.description}</p>
        <div className="text-sm text-gray-500">{item.relationship_name} {item.service_context && `• ${item.service_context}`}</div>
        {item.amount && <div className="text-lg font-semibold text-emerald-600 mt-1">${item.amount.toLocaleString()}</div>}
        {item.action_required && <div className="mt-2 p-2 bg-amber-50 rounded text-sm text-amber-800"><span className="font-medium">Action: </span>{item.action_required}</div>}
      </div>
    </div>
    <div className="flex items-center gap-2 mt-3 pt-3 border-t border-gray-100">
      <Button variant="success" size="sm" onClick={() => onAction('action', item)}>Create Action</Button>
      <Button variant="default" size="sm" onClick={() => onAction('note', item)}>Note Only</Button>
    </div>
  </Card>
);

const CoolingCard = ({ item, onAction }) => (
  <Card className="p-3">
    <div className="flex items-center justify-between">
      <div>
        <div className="flex items-center gap-2 mb-1">
          <span className="font-medium text-gray-900">{item.name}</span>
          <TemperatureIndicator temp={item.temperature} />
        </div>
        <div className="text-sm text-gray-600">{item.organization}</div>
        <div className="flex items-center gap-2 text-xs text-gray-400 mt-1">
          <GeoBadge geo={item.geography} />
          <Badge size="sm">{item.stage}</Badge>
          <span className="text-amber-600 font-medium">{item.days_since_contact} days ago</span>
        </div>
      </div>
      <Button variant="primary" size="sm" onClick={() => onAction('reach_out', item)}>Reach Out</Button>
    </div>
  </Card>
);

const OverdueCard = ({ item, isOurs, onAction }) => (
  <Card className={`p-3 border-l-4 ${isOurs ? 'border-l-red-500' : 'border-l-amber-500'}`}>
    <div className="flex items-center justify-between">
      <div>
        <p className="font-medium text-gray-900">{item.description}</p>
        <div className="flex items-center gap-2 text-sm text-gray-500">
          <span>{item.relationship_name}</span>
          <span className={`font-medium ${isOurs ? 'text-red-600' : 'text-amber-600'}`}>{item.days_overdue} days overdue</span>
        </div>
      </div>
      <Button variant={isOurs ? 'danger' : 'warning'} size="sm" onClick={() => onAction('resolve', item)}>
        {isOurs ? 'Resolve' : 'Follow Up'}
      </Button>
    </div>
  </Card>
);

// ============================================================
// INTELLIGENCE COMPONENTS
// ============================================================

const PersonaCard = ({ persona, expanded, onToggle }) => (
  <Card className="overflow-hidden">
    <div className="p-4 cursor-pointer hover:bg-gray-50 transition-colors" onClick={onToggle}>
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <div className="flex items-center gap-2 mb-1">
            <Users size={18} className="text-blue-600" />
            <h3 className="font-semibold text-gray-900">{persona.display_name}</h3>
            <Badge variant={persona.overdue_count > 3 ? 'danger' : persona.overdue_count > 0 ? 'warning' : 'success'}>{persona.overdue_count} overdue</Badge>
          </div>
          <p className="text-sm text-gray-500 mb-3">{persona.description}</p>
          <div className="grid grid-cols-4 gap-4 mb-3">
            <div><div className="text-xs text-gray-400">Relationships</div><div className="text-lg font-semibold">{persona.total_relationships}</div></div>
            <div><div className="text-xs text-gray-400">Pipeline</div><div className="text-lg font-semibold">{persona.active_pipeline}</div></div>
            <div><div className="text-xs text-gray-400">Value</div><div className="text-lg font-semibold text-emerald-600">${(persona.pipeline_value / 1000).toFixed(0)}K</div></div>
            <div><div className="text-xs text-gray-400">Win Rate</div><div className="text-lg font-semibold">{persona.conversion_rate}%</div></div>
          </div>
          <div className="mb-2"><div className="text-xs text-gray-400 mb-1">Temperature</div><TemperatureBar dist={persona.temperature_dist} total={persona.total_relationships} /></div>
        </div>
        <ChevronDown size={20} className={`text-gray-400 transition-transform ${expanded ? 'rotate-180' : ''}`} />
      </div>
    </div>
    {expanded && (
      <div className="border-t border-gray-100 p-4 bg-gray-50">
        <div className="grid grid-cols-2 gap-6">
          <div>
            <h4 className="text-sm font-semibold text-emerald-700 mb-2 flex items-center gap-1"><Lightbulb size={14} />What Works</h4>
            <div className="space-y-2">
              <div><div className="text-xs text-gray-500 mb-1">Proof Points</div><div className="flex flex-wrap gap-1">{persona.effective_proof_points.map((p, i) => <Badge key={i} variant="success" size="sm">{p}</Badge>)}</div></div>
              <div><div className="text-xs text-gray-500 mb-1">Language</div><div className="flex flex-wrap gap-1">{persona.effective_language.map((l, i) => <Badge key={i} variant="info" size="sm">{l}</Badge>)}</div></div>
            </div>
          </div>
          <div>
            <h4 className="text-sm font-semibold text-red-700 mb-2 flex items-center gap-1"><AlertTriangle size={14} />Watch Out</h4>
            <div className="space-y-2">
              <div><div className="text-xs text-gray-500 mb-1">Objections</div><div className="flex flex-wrap gap-1">{persona.top_objections.map((o, i) => <Badge key={i} variant="warning" size="sm">{o}</Badge>)}</div></div>
              <div><div className="text-xs text-gray-500 mb-1">Avoid</div><div className="flex flex-wrap gap-1">{persona.ineffective_approaches.map((a, i) => <Badge key={i} variant="danger" size="sm">{a}</Badge>)}</div></div>
            </div>
          </div>
        </div>
        <div className="mt-4 pt-4 border-t border-gray-200">
          <h4 className="text-sm font-semibold text-gray-700 mb-2 flex items-center gap-1"><Globe size={14} />Cultural Notes</h4>
          <div className="grid grid-cols-2 gap-4">
            {Object.entries(persona.cultural_notes).map(([geo, note]) => (
              <div key={geo} className="bg-white rounded-lg p-3 border border-gray-200">
                <div className="text-xs font-medium text-gray-500 mb-1">{geo === 'brazil' ? '🇧🇷' : '🇺🇸'} {geo.replace('_', ' ')}</div>
                <div className="text-sm text-gray-700">{note}</div>
              </div>
            ))}
          </div>
        </div>
        <div className="mt-4 pt-4 border-t border-gray-200 flex items-center gap-4">
          <div className="flex items-center gap-2"><Clock size={14} className="text-gray-400" /><span className="text-sm text-gray-600">Touch every <strong>{persona.recommended_touch_days} days</strong></span></div>
          <div className="flex items-center gap-2"><Target size={14} className="text-gray-400" /><span className="text-sm text-gray-600">Avg <strong>{persona.avg_days_to_convert} days</strong> to convert</span></div>
        </div>
      </div>
    )}
  </Card>
);

const ServiceCard = ({ service }) => {
  const [expanded, setExpanded] = useState(false);
  return (
    <Card className="overflow-hidden">
      <div className="p-4 cursor-pointer hover:bg-gray-50 transition-colors" onClick={() => setExpanded(!expanded)}>
        <div className="flex items-start justify-between mb-3">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <Briefcase size={16} className="text-purple-600" />
              <h3 className="font-semibold text-gray-900">{service.display_name}</h3>
              <Badge variant="info">{service.category}</Badge>
            </div>
          </div>
          <div className="text-right"><div className="text-lg font-semibold text-emerald-600">${(service.pipeline_value / 1000).toFixed(0)}K</div><div className="text-xs text-gray-400">pipeline</div></div>
        </div>
        <div className="mb-3">
          <div className="text-xs text-gray-400 mb-2">Interest Funnel</div>
          <div className="flex items-center gap-1">
            {Object.entries(service.pipeline_stages).map(([stage, count], i) => (
              <React.Fragment key={stage}>
                <div className="flex-1 text-center">
                  <div className={`h-8 rounded flex items-center justify-center text-sm font-medium ${stage === 'ready_to_buy' ? 'bg-emerald-100 text-emerald-700' : stage === 'evaluating' ? 'bg-blue-100 text-blue-700' : stage === 'curious' ? 'bg-amber-100 text-amber-700' : 'bg-gray-100 text-gray-600'}`}>{count}</div>
                  <div className="text-xs text-gray-400 mt-1 capitalize">{stage.replace('_', ' ')}</div>
                </div>
                {i < Object.entries(service.pipeline_stages).length - 1 && <ChevronRight size={14} className="text-gray-300 flex-shrink-0" />}
              </React.Fragment>
            ))}
          </div>
        </div>
        <div className="flex items-center gap-4 text-sm">
          <span className="text-gray-600"><Award size={14} className="inline text-emerald-500" /> {service.win_rate}% win</span>
          <span className="text-gray-600"><DollarSign size={14} className="inline text-blue-500" /> ${(service.avg_deal_size / 1000).toFixed(0)}K avg</span>
        </div>
      </div>
      {expanded && (
        <div className="border-t border-gray-100 p-4 bg-gray-50">
          <div className="grid grid-cols-2 gap-4">
            <div><div className="text-xs font-medium text-gray-500 mb-2">Best Fit Personas</div><div className="flex flex-wrap gap-1">{service.best_personas.map((p, i) => <PersonaBadge key={i} persona={p} />)}</div></div>
            <div><div className="text-xs font-medium text-gray-500 mb-2">Differentiators</div><div className="flex flex-wrap gap-1">{service.winning_differentiators.map((d, i) => <Badge key={i} variant="success" size="sm">{d}</Badge>)}</div></div>
          </div>
          <div className="grid grid-cols-2 gap-4 mt-4">
            <div><div className="text-xs font-medium text-gray-500 mb-2">Objections</div><ul className="text-sm text-gray-600 space-y-1">{service.top_objections.map((o, i) => <li key={i} className="flex items-start gap-2"><AlertTriangle size={12} className="text-amber-500 mt-0.5" />{o}</li>)}</ul></div>
            <div><div className="text-xs font-medium text-gray-500 mb-2">Proof Points</div><ul className="text-sm text-gray-600 space-y-1">{service.key_proof_points.map((p, i) => <li key={i} className="flex items-start gap-2"><Award size={12} className="text-emerald-500 mt-0.5" />{p}</li>)}</ul></div>
          </div>
        </div>
      )}
    </Card>
  );
};

const CompetitorCard = ({ competitor }) => (
  <Card className="p-4">
    <div className="flex items-start justify-between mb-3">
      <div>
        <div className="flex items-center gap-2 mb-1">
          <Shield size={16} className="text-gray-500" />
          <h4 className="font-medium text-gray-900">{competitor.name}</h4>
          <Badge variant={competitor.type === 'direct' ? 'danger' : competitor.type === 'do_nothing' ? 'warning' : 'default'}>{competitor.type.replace('_', ' ')}</Badge>
        </div>
        <div className="text-sm text-gray-500">{competitor.mentions} mentions</div>
      </div>
      <div className="text-right"><div className={`text-lg font-semibold ${competitor.win_rate_against >= 60 ? 'text-emerald-600' : 'text-amber-600'}`}>{competitor.win_rate_against}%</div><div className="text-xs text-gray-400">win rate</div></div>
    </div>
    <div className="grid grid-cols-2 gap-3 mb-3">
      <div><div className="text-xs text-gray-500 mb-1">Their Strengths</div><div className="flex flex-wrap gap-1">{competitor.perceived_strengths.map((s, i) => <Badge key={i} variant="danger" size="sm">{s}</Badge>)}</div></div>
      <div><div className="text-xs text-gray-500 mb-1">Their Weaknesses</div><div className="flex flex-wrap gap-1">{competitor.perceived_weaknesses.map((w, i) => <Badge key={i} variant="success" size="sm">{w}</Badge>)}</div></div>
    </div>
    <div className="bg-emerald-50 rounded-lg p-3 border border-emerald-100">
      <div className="text-xs font-medium text-emerald-700 mb-1">Winning Differentiator</div>
      <div className="text-sm text-emerald-900">{competitor.winning_differentiator}</div>
    </div>
  </Card>
);

const ObjectionPatternCard = ({ objection }) => (
  <Card className="p-4">
    <div className="flex items-start justify-between mb-2">
      <div className="flex items-center gap-2">
        <MessageSquare size={16} className="text-amber-500" />
        <h4 className="font-medium text-gray-900 capitalize">{objection.type}</h4>
        <Badge>{objection.count}x</Badge>
      </div>
      <div className={`text-sm font-medium ${objection.overcome_rate >= 60 ? 'text-emerald-600' : 'text-amber-600'}`}>{objection.overcome_rate}% overcome</div>
    </div>
    <div className="bg-amber-50 rounded-lg p-2 mb-3 border border-amber-100"><div className="text-sm text-amber-900 italic">"{objection.common_text}"</div></div>
    <div className="text-xs font-medium text-gray-500 mb-2">Winning Responses</div>
    <ul className="space-y-1">{objection.winning_responses.map((r, i) => <li key={i} className="text-sm text-gray-600 flex items-start gap-2"><Lightbulb size={12} className="text-emerald-500 mt-0.5" />{r}</li>)}</ul>
  </Card>
);

// ============================================================
// MAIN DASHBOARD - Export this component
// ============================================================

export default function RelationshipIntelligenceDashboard({
  actionData = null,
  intelligenceData = null,
  onAction = () => {}
}) {
  const [activeSection, setActiveSection] = useState('action');
  const [expandedPersona, setExpandedPersona] = useState(null);
  const [actionLog, setActionLog] = useState([]);

  const handleAction = (action, item) => {
    setActionLog(prev => [...prev, { action, item, timestamp: new Date() }]);
    onAction(action, item);
  };

  // Calculate totals from data or use defaults
  const totalPending = actionData ? (
    (actionData.pending?.relationships?.length || 0) +
    (actionData.pending?.service_interests?.length || 0) +
    (actionData.pending?.commitments_ours?.length || 0) +
    (actionData.pending?.commitments_theirs?.length || 0) +
    (actionData.pending?.objections?.length || 0) +
    (actionData.pending?.signals?.length || 0)
  ) : 0;

  const totalAttention = actionData ? (
    (actionData.attention?.cooling?.length || 0) +
    (actionData.attention?.overdue_ours?.length || 0) +
    (actionData.attention?.overdue_theirs?.length || 0)
  ) : 0;

  const sections = [
    { id: 'action', label: 'Action Center', icon: Inbox, badge: totalPending + totalAttention },
    { id: 'personas', label: 'Persona Playbooks', icon: Users },
    { id: 'services', label: 'Service Traction', icon: Briefcase },
    { id: 'battle', label: 'Battle Intelligence', icon: Shield }
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white border-b border-gray-200">
        <div className="px-6 py-4">
          <div className="flex items-center justify-between mb-4">
            <div>
              <h1 className="text-xl font-semibold text-gray-900">360 Relationship Intelligence</h1>
              <p className="text-sm text-gray-500">Action center and strategic insights</p>
            </div>
            <div className="flex items-center gap-3">
              <Badge variant="success">62 relationships</Badge>
              <Badge variant="purple">$890K pipeline</Badge>
              <Button variant="ghost" size="sm"><RefreshCw size={14} className="mr-1" />Sync</Button>
            </div>
          </div>
          <div className="flex gap-1">
            {sections.map(s => (
              <button key={s.id} onClick={() => setActiveSection(s.id)}
                className={`flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-lg transition-colors ${activeSection === s.id ? 'bg-blue-100 text-blue-700' : 'text-gray-600 hover:bg-gray-100'}`}>
                <s.icon size={16} />{s.label}
                {s.badge > 0 && <span className="px-2 py-0.5 bg-blue-600 text-white text-xs rounded-full">{s.badge}</span>}
              </button>
            ))}
          </div>
        </div>
      </div>

      <div className="p-6">
        {/* ACTION CENTER */}
        {activeSection === 'action' && (
          <div className="space-y-8">
            {/* Quick Stats */}
            <div className="grid grid-cols-4 gap-4">
              <MetricCard label="Pending Review" value={totalPending} subvalue="items to process" icon={Inbox} />
              <MetricCard label="Attention Needed" value={totalAttention} subvalue="cooling + overdue" icon={AlertTriangle} />
              <MetricCard label="This Week" value="8" subvalue="meetings processed" trend="up" icon={Calendar} />
              <MetricCard label="Pipeline Added" value="$120K" subvalue="+3 opportunities" trend="up" icon={DollarSign} />
            </div>

            {/* Pending Review */}
            {totalPending > 0 && actionData?.pending && (
              <div>
                <div className="flex items-center justify-between mb-4">
                  <h2 className="text-lg font-semibold text-gray-900">Pending Review</h2>
                  <div className="flex items-center gap-2">
                    <Button variant="success" size="sm">Push All Selected</Button>
                    <Button variant="default" size="sm">Mark All Reviewed</Button>
                  </div>
                </div>

                <div className="space-y-6">
                  {actionData.pending.relationships?.length > 0 && (
                    <div>
                      <h3 className="text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2"><Users size={16} />New Relationships ({actionData.pending.relationships.length})</h3>
                      <div className="grid gap-4">{actionData.pending.relationships.map(item => <RelationshipReviewCard key={item.id} item={item} onAction={handleAction} />)}</div>
                    </div>
                  )}

                  {actionData.pending.service_interests?.length > 0 && (
                    <div>
                      <h3 className="text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2"><Briefcase size={16} />Service Interests ({actionData.pending.service_interests.length})</h3>
                      <div className="grid gap-4 md:grid-cols-2">{actionData.pending.service_interests.map(item => <ServiceInterestCard key={item.id} item={item} onAction={handleAction} />)}</div>
                    </div>
                  )}

                  {actionData.pending.commitments_ours?.length > 0 && (
                    <div>
                      <h3 className="text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2"><ArrowRight size={16} />Our Commitments ({actionData.pending.commitments_ours.length})</h3>
                      <div className="grid gap-4 md:grid-cols-2">{actionData.pending.commitments_ours.map(item => <CommitmentCard key={item.id} item={item} isOurs={true} onAction={handleAction} />)}</div>
                    </div>
                  )}

                  {actionData.pending.commitments_theirs?.length > 0 && (
                    <div>
                      <h3 className="text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2"><Clock size={16} />Their Commitments ({actionData.pending.commitments_theirs.length})</h3>
                      <div className="grid gap-4 md:grid-cols-2">{actionData.pending.commitments_theirs.map(item => <CommitmentCard key={item.id} item={item} isOurs={false} onAction={handleAction} />)}</div>
                    </div>
                  )}

                  {actionData.pending.objections?.length > 0 && (
                    <div>
                      <h3 className="text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2"><MessageSquare size={16} />Objections Captured ({actionData.pending.objections.length})</h3>
                      <div className="grid gap-4">{actionData.pending.objections.map(item => <ObjectionCard key={item.id} item={item} onAction={handleAction} />)}</div>
                    </div>
                  )}

                  {actionData.pending.signals?.length > 0 && (
                    <div>
                      <h3 className="text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2"><Zap size={16} />Signals ({actionData.pending.signals.length})</h3>
                      <div className="grid gap-4">{actionData.pending.signals.map(item => <SignalCard key={item.id} item={item} onAction={handleAction} />)}</div>
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* Attention Queue */}
            {totalAttention > 0 && actionData?.attention && (
              <div>
                <h2 className="text-lg font-semibold text-gray-900 mb-4">Attention Queue</h2>
                <div className="space-y-6">
                  {actionData.attention.cooling?.length > 0 && (
                    <div>
                      <h3 className="text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2"><TrendingDown size={16} className="text-blue-500" />Cooling Relationships</h3>
                      <div className="grid gap-3">{actionData.attention.cooling.map(item => <CoolingCard key={item.id} item={item} onAction={handleAction} />)}</div>
                    </div>
                  )}
                  {actionData.attention.overdue_ours?.length > 0 && (
                    <div>
                      <h3 className="text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2"><AlertTriangle size={16} className="text-red-500" />Our Overdue</h3>
                      <div className="grid gap-3">{actionData.attention.overdue_ours.map(item => <OverdueCard key={item.id} item={item} isOurs={true} onAction={handleAction} />)}</div>
                    </div>
                  )}
                  {actionData.attention.overdue_theirs?.length > 0 && (
                    <div>
                      <h3 className="text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2"><Clock size={16} className="text-amber-500" />Their Overdue</h3>
                      <div className="grid gap-3">{actionData.attention.overdue_theirs.map(item => <OverdueCard key={item.id} item={item} isOurs={false} onAction={handleAction} />)}</div>
                    </div>
                  )}
                </div>
              </div>
            )}

            {totalPending === 0 && totalAttention === 0 && (
              <div className="text-center py-12 text-gray-500">
                <CheckCircle size={48} className="mx-auto mb-4 text-emerald-500" />
                <p className="text-lg font-medium">All caught up!</p>
                <p className="text-sm">No items pending review or attention</p>
              </div>
            )}
          </div>
        )}

        {/* PERSONAS */}
        {activeSection === 'personas' && intelligenceData?.personas && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold text-gray-900">Persona Engagement Playbooks</h2>
            {intelligenceData.personas.map(p => <PersonaCard key={p.id} persona={p} expanded={expandedPersona === p.id} onToggle={() => setExpandedPersona(expandedPersona === p.id ? null : p.id)} />)}
          </div>
        )}

        {/* SERVICES */}
        {activeSection === 'services' && intelligenceData?.services && (
          <div className="space-y-6">
            <div className="grid grid-cols-4 gap-4">
              <MetricCard label="Total Pipeline" value="$890K" subvalue="+12% this month" trend="up" icon={DollarSign} />
              <MetricCard label="Active Opportunities" value="42" subvalue="8 ready to buy" icon={Target} />
              <MetricCard label="Avg Win Rate" value="56%" subvalue="+3% vs benchmark" trend="up" icon={Award} />
              <MetricCard label="Avg Days to Close" value="94" icon={Clock} />
            </div>
            <h2 className="text-lg font-semibold text-gray-900">Service Interest Funnel</h2>
            <div className="grid gap-4">{intelligenceData.services.map(s => <ServiceCard key={s.id} service={s} />)}</div>
          </div>
        )}

        {/* BATTLE */}
        {activeSection === 'battle' && intelligenceData && (
          <div className="space-y-6">
            {intelligenceData.competitors && (
              <div>
                <h2 className="text-lg font-semibold text-gray-900 mb-4">Competitor Battle Cards</h2>
                <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">{intelligenceData.competitors.map((c, i) => <CompetitorCard key={i} competitor={c} />)}</div>
              </div>
            )}
            {intelligenceData.objection_patterns && (
              <div>
                <h2 className="text-lg font-semibold text-gray-900 mb-4">Objection Playbook</h2>
                <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">{intelligenceData.objection_patterns.map((o, i) => <ObjectionPatternCard key={i} objection={o} />)}</div>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Toast */}
      {actionLog.length > 0 && (
        <div className="fixed bottom-4 right-4 bg-gray-900 text-white px-4 py-3 rounded-lg shadow-lg">
          <div className="flex items-center gap-2">
            <CheckCircle size={16} className="text-emerald-400" />
            <span className="text-sm">Action recorded</span>
          </div>
        </div>
      )}
    </div>
  );
}
