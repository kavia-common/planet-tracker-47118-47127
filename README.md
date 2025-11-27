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

CORS is enabled broadly for /api/*.