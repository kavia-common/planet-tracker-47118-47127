# Planet Tracker Backend (Flask)

CORS configuration for previews:

- If `PREVIEW_ORIGIN` is set (e.g., `https://vscode-internal-....cloud.kavia.ai:3000`), the backend will:
  - Allow that specific origin for `/api/*`
  - Enable `supports_credentials=True`

- If `PREVIEW_ORIGIN` is NOT set:
  - Backend allows wildcard `*` origin for `/api/*`
  - `supports_credentials=False` (required by CORS spec when using `*`)
  - Allowed methods: `GET, OPTIONS`
  - Allowed headers: `Content-Type, Authorization`

This aims to eliminate Network/CORS errors in preview environments.

Required endpoints:
- GET `/api/health`
- GET `/api/neos`
- GET `/api/planets`

Ensure your app initialization (e.g., `create_app`) applies the above CORS settings. If you already have an app factory, merge the CORS block accordingly.
