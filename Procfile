frontend: cd server/frontend && npm run build && serve -s build -p 3000
backend: gunicorn server.app:app --bind 0.0.0.0:8000
proxy: cd server/frontend && node server.js
