/**
 * Authentication & Role Navigation Logic
 */
document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('loginForm');
  const registerForm = document.getElementById('registerForm');

  if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const login_identifier = document.getElementById('username').value.trim();
      const password = document.getElementById('password').value.trim();
      const alertBox = document.getElementById('authAlert');

      const res = await API.post('/auth/login', { login_identifier, password });
      if (res.data && res.data.token) {
        API.setToken(res.data.token);
        localStorage.setItem('user_info', JSON.stringify(res.data.user));
        window.location.href = res.data.redirect_url + '.html';
      } else {
        alertBox.style.display = 'block';
        alertBox.textContent = res.error || 'Invalid credentials.';
      }
    });
  }

  if (registerForm) {
    registerForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const username = document.getElementById('regUsername').value.trim();
      const email = document.getElementById('regEmail').value.trim();
      const password = document.getElementById('regPassword').value.trim();
      const full_name = document.getElementById('regFullName').value.trim();
      const alertBox = document.getElementById('regAlert');

      const res = await API.post('/auth/register', { username, email, password, full_name, role: 'CITIZEN' });
      if (res.data && res.data.token) {
        API.setToken(res.data.token);
        localStorage.setItem('user_info', JSON.stringify(res.data.user));
        window.location.href = '/citizen/dashboard.html';
      } else {
        alertBox.style.display = 'block';
        alertBox.textContent = res.error || 'Registration failed.';
      }
    });
  }
});

function handleLogout() {
  API.post('/auth/logout', {}).then(() => {
    API.clearSession();
    window.location.href = '/auth/login.html';
  });
}
