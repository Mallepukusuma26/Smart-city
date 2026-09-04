"""
Simple In-Memory Rate Limiting Middleware.
"""
import time
from flask import request, jsonify

_request_counts = {}

def init_rate_limiter(app, max_requests=300, window_sec=60):
    @app.before_request
    def check_rate_limit():
        if not request.path.startswith("/api/"):
            return
        
        client_ip = request.remote_addr or "127.0.0.1"
        now = time.time()
        
        # Clean old entries
        timestamps = _request_counts.get(client_ip, [])
        timestamps = [t for t in timestamps if now - t < window_sec]
        
        if len(timestamps) >= max_requests:
            return jsonify({"error": "Rate limit exceeded. Please slow down.", "code": 429}), 429
        
        timestamps.append(now)
        _request_counts[client_ip] = timestamps
