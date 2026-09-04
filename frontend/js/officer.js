/**
 * Officer Dashboard Portal Client Logic
 */
document.addEventListener('DOMContentLoaded', async () => {
  if (!window.location.pathname.includes('/officer/')) return;

  const res = await API.get('/officer/dashboard');
  if (res.error) return;

  // Render Officer Info
  const offNameEl = document.getElementById('officerName');
  const offBadgeEl = document.getElementById('officerBadge');
  const offDeptEl = document.getElementById('officerDepartment');

  if (offNameEl) offNameEl.textContent = res.officer.name;
  if (offBadgeEl) offBadgeEl.textContent = res.officer.badge_number;
  if (offDeptEl) offDeptEl.textContent = res.officer.department_name;

  // Render Stats
  const assignedCnt = document.getElementById('assignedToMeCount');
  const pendingCnt = document.getElementById('deptPendingCount');
  const highPrioCnt = document.getElementById('highPriorityCount');

  if (assignedCnt) assignedCnt.textContent = res.stats.assigned_to_me;
  if (pendingCnt) pendingCnt.textContent = res.stats.pending_count;
  if (highPrioCnt) highPrioCnt.textContent = res.stats.high_priority_count;

  // Render Officer Assigned Complaints
  const tbody = document.getElementById('officerTasksTableBody');
  if (tbody && res.assigned_complaints) {
    tbody.innerHTML = res.assigned_complaints.map(c => `
      <tr>
        <td><strong>${c.ticket_number}</strong></td>
        <td>${c.title}</td>
        <td>${c.location}</td>
        <td><span class="badge ${c.priority === 'CRITICAL' ? 'badge-danger' : 'badge-warning'}">${c.priority}</span></td>
        <td><span class="badge badge-info">${c.status}</span></td>
        <td>
          <button onclick="updateStatusModal(${c.id}, 'IN_PROGRESS')" class="btn btn-warning" style="padding: 0.25rem 0.5rem; font-size: 0.75rem;">In Progress</button>
          <button onclick="updateStatusModal(${c.id}, 'RESOLVED')" class="btn btn-success" style="padding: 0.25rem 0.5rem; font-size: 0.75rem;">Resolve</button>
        </td>
      </tr>
    `).join('');
  }
});

async function updateStatusModal(complaintId, newStatus) {
  const remarks = prompt(`Enter remarks for changing status to ${newStatus}:`, 'Issue investigated and resolved by officer.');
  if (remarks === null) return;

  const res = await API.post(`/officer/complaints/${complaintId}/update`, { status: newStatus, remarks });
  if (res.message) {
    alert(res.message);
    window.location.reload();
  } else {
    alert(res.error || 'Update failed.');
  }
}
