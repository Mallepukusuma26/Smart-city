/**
 * Citizen Dashboard Portal Client Logic
 */
document.addEventListener('DOMContentLoaded', async () => {
  if (!window.location.pathname.includes('/citizen/')) return;

  const res = await API.get('/citizen/dashboard');
  if (res.error) return;

  // Render Citizen Name & Card ID
  const citizenNameEl = document.getElementById('citizenName');
  const citizenCardIdEl = document.getElementById('citizenCardId');
  if (citizenNameEl) citizenNameEl.textContent = res.citizen.name;
  if (citizenCardIdEl) citizenCardIdEl.textContent = res.citizen.citizen_id;

  // Render Stats
  const totalCompEl = document.getElementById('totalComplaintsCount');
  const pendingCompEl = document.getElementById('pendingComplaintsCount');
  const resolvedCompEl = document.getElementById('resolvedComplaintsCount');

  if (totalCompEl) totalCompEl.textContent = res.complaint_stats.total_my_complaints;
  if (pendingCompEl) pendingCompEl.textContent = res.complaint_stats.pending_count;
  if (resolvedCompEl) resolvedCompEl.textContent = res.complaint_stats.resolved_count;

  // Render Recent Complaints Table
  const complaintTableBody = document.getElementById('myComplaintsTableBody');
  if (complaintTableBody && res.recent_complaints) {
    complaintTableBody.innerHTML = res.recent_complaints.map(c => `
      <tr>
        <td><strong>${c.ticket_number}</strong></td>
        <td>${c.title}</td>
        <td>${c.category_name}</td>
        <td><span class="badge ${c.status === 'RESOLVED' ? 'badge-success' : 'badge-warning'}">${c.status}</span></td>
        <td>${c.created_at.split('T')[0]}</td>
      </tr>
    `).join('');
  }

  // Handle Create Complaint Form
  const newComplaintForm = document.getElementById('newComplaintForm');
  if (newComplaintForm) {
    newComplaintForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const title = document.getElementById('title').value;
      const description = document.getElementById('description').value;
      const location = document.getElementById('location').value;
      const priority = document.getElementById('priority').value;

      const result = await API.post('/citizen/complaints', { title, description, location, priority });
      if (result.complaint) {
        alert('Complaint submitted successfully! Ticket Number: ' + result.complaint.ticket_number);
        window.location.reload();
      } else {
        alert(result.error || 'Failed to submit complaint.');
      }
    });
  }
});
