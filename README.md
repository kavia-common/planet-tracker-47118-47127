# planet-tracker-47118-47127

Planet Tracker Backend (Flask)

- Docs UI: /docs
- Health: GET /api/health
- NEOs: GET /api/neos?date=YYYY-MM-DD[&page=1&per_page=10]
- Planets: GET /api/planets?date=YYYY-MM-DD

NEO item schema:
- id, name, close_approach_date, relative_velocity_km_s, miss_distance_km, is_potentially_hazardous

Planet item schema:
- name, right_ascension, declination, distance_au

CORS is enabled broadly for /api/* and /docs*, and the server binds to 0.0.0.0 on port 3001 by default (configurable via HOST/PORT).

Preview notes:
- Ensure your frontend uses the exact HTTPS origin on port 3001 (e.g., https://<host>:3001). Set REACT_APP_API_BASE_URL in the frontend .env accordingly.
- Mixed content (https frontend -> http backend) will be blocked by the browser.