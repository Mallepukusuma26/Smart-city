/**
 * Unified Smart City API Client & Request Handler
 */
const API = {
  baseUrl: '/api',

  getToken() {
    return localStorage.getItem('smart_city_jwt');
  },

  setToken(token) {
    localStorage.setItem('smart_city_jwt', token);
  },

  clearSession() {
    localStorage.removeItem('smart_city_jwt');
    localStorage.removeItem('user_info');
  },

  async request(endpoint, options = {}) {
    const headers = {
      'Content-Type': 'application/json',
      ...options.headers,
    };

    const token = this.getToken();
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    const config = {
      ...options,
      headers,
    };

    try {
      const response = await fetch(`${this.baseUrl}${endpoint}`, config);
      const data = await response.json().catch(() => ({}));

      if (response.status === 401) {
        this.clearSession();
        if (!window.location.pathname.includes('/auth/')) {
          window.location.href = '/auth/login.html';
        }
        return { error: 'Unauthorized', code: 401 };
      }

      if (response.status === 403) {
        alert(data.error || 'Access Denied: You do not have permissions for this dashboard.');
        return { error: data.error || 'Forbidden', code: 403 };
      }

      if (!response.ok) {
        return { error: data.error || 'API Request Failed', code: response.status, data };
      }

      return data;
    } catch (err) {
      console.error('API Fetch Error:', err);
      return { error: 'Network Connection Error', code: 500 };
    }
  },

  get(endpoint) {
    return this.request(endpoint, { method: 'GET' });
  },

  post(endpoint, body) {
    return this.request(endpoint, { method: 'POST', body: JSON.stringify(body) });
  },

  put(endpoint, body) {
    return this.request(endpoint, { method: 'PUT', body: JSON.stringify(body) });
  },

  delete(endpoint) {
    return this.request(endpoint, { method: 'DELETE' });
  }
};
