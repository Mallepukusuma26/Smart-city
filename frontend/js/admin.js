/**
 * Admin Master Portal Client Logic
 */
document.addEventListener('DOMContentLoaded', async () => {
  if (!window.location.pathname.includes('/admin/')) return;

  const res = await API.get('/admin/dashboard');
  if (res.error) return;

  // Render Master Admin Stats
  const setEl = (id, val) => {
    const el = document.getElementById(id);
    if (el) el.textContent = val;
  };

  setEl('totalUsersCount', res.admin_stats.total_users);
  setEl('totalCitizensCount', res.admin_stats.total_citizens);
  setEl('totalOfficersCount', res.admin_stats.total_officers);
  setEl('totalDepartmentsCount', res.admin_stats.total_departments);
  setEl('totalComplaintsCount', res.admin_stats.total_complaints);
  setEl('activeEmergenciesCount', res.admin_stats.active_emergencies);
  setEl('activeAlertsCount', res.admin_stats.active_alerts);
  setEl('trainedModelsCount', res.admin_stats.trained_ml_models);

  setEl('resolutionRateValue', res.city_kpis.resolution_rate + '%');
  setEl('avgTrafficIdxValue', res.city_kpis.avg_traffic_index);
  setEl('cityHealthScoreValue', res.city_kpis.overall_health_score + ' / 100');

  // Render Recent Audit Logs
  const auditTbody = document.getElementById('recentAuditLogsTbody');
  if (auditTbody && res.recent_audit_logs) {
    auditTbody.innerHTML = res.recent_audit_logs.map(log => `
      <tr>
        <td>${log.timestamp ? log.timestamp.replace('T', ' ').split('.')[0] : ''}</td>
        <td><strong>${log.username}</strong> (${log.role})</td>
        <td><span class="badge badge-info">${log.action}</span></td>
        <td>${log.ip_address}</td>
        <td>${log.details}</td>
      </tr>
    `).join('');
  }
});

// AI Prediction Tester Modal Handler
async function runAiInferenceTest(modelType) {
  let payload = {};
  if (modelType === 'traffic') payload = { vehicle_count: 550, avg_speed_kmh: 22.5, is_peak_hour: 1 };
  if (modelType === 'waste') payload = { fill_level: 88.5, weight_kg: 920.0 };
  if (modelType === 'water') payload = { flow_rate_lps: 65.0 };
  if (modelType === 'pollution') payload = { pm2_5: 85.0, pm10: 160.0 };

  const res = await API.post('/services/ai/predict', { model_type: modelType, ...payload });
  alert(`AI Model Model [${modelType.toUpperCase()}] Prediction Result:\n` + JSON.stringify(res.prediction, null, 2));
}
