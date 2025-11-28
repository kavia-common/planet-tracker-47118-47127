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

CORS:
- Enabled for /api/* and /docs*.
- Default origin is "*" for preview/local development.
- To restrict to a specific preview origin, set PREVIEW_ORIGIN in the environment (see .env.example), e.g.:
  PREVIEW_ORIGIN=https://<your-preview-host>:3000

Local development:
- Backend runs on port 3001, frontend on 3000.
- Verify the API is healthy at: http://localhost:3001/api/health (or the preview URL)
- OpenAPI/Docs: http://localhost:3001/docs