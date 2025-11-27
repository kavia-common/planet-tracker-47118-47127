"""
Data providers (stubbed) for Near-Earth Objects (NEOs) and planetary positions.

These providers return deterministic stub data and can be replaced later with real
connectors to external services such as NASA APIs or astronomy libraries.

Environment/configuration: do not hardcode any secrets or URLs here.
"""

from datetime import datetime
from typing import Dict, List, Tuple


def _parse_date(date_str: str) -> datetime:
    """Parse date in YYYY-MM-DD format, raising ValueError for invalid inputs."""
    return datetime.strptime(date_str, "%Y-%m-%d")


# PUBLIC_INTERFACE
def get_neos_for_date(date: str, page: int = 1, per_page: int = 10) -> Tuple[List[Dict], Dict]:
    """Return a paginated list of stub NEO data for the given date.

    Args:
        date: ISO date string YYYY-MM-DD.
        page: 1-based page number.
        per_page: items per page (max 100).

    Returns:
        A tuple of (items, pagination) where:
          - items: list of NEO dicts with keys:
              id, name, close_approach_date, relative_velocity_km_s,
              miss_distance_km, is_potentially_hazardous
          - pagination: dict with total, total_pages, page, per_page,
              previous_page, next_page, first_page, last_page
    """
    _parse_date(date)  # Validate date
    # Generate deterministic stub data based on the date seed
    seed = sum(ord(c) for c in date)
    total_items = 37 + (seed % 13)  # a small varying total
    # Build full dataset
    full: List[Dict] = []
    for i in range(total_items):
        hazard = ((i + seed) % 7) == 0
        rel_vel = 5.0 + ((i + seed) % 120) / 3.7  # km/s
        miss_km = 150000.0 + ((i * 931) % 2_000_000)
        full.append(
            {
                "id": f"neo-{date}-{i}",
                "name": f"Stub NEO {i}",
                "close_approach_date": date,
                "relative_velocity_km_s": round(rel_vel, 3),
                "miss_distance_km": round(miss_km, 2),
                "is_potentially_hazardous": hazard,
            }
        )

    # Pagination
    per_page = max(1, min(int(per_page), 100))
    page = max(1, int(page))
    start = (page - 1) * per_page
    end = start + per_page
    items = full[start:end]
    total_pages = (total_items + per_page - 1) // per_page

    pagination = {
        "total": total_items,
        "total_pages": total_pages,
        "first_page": 1,
        "last_page": max(1, total_pages),
        "page": page,
        "previous_page": page - 1 if page > 1 else None,
        "next_page": page + 1 if page < total_pages else None,
        "per_page": per_page,
    }
    return items, pagination


# PUBLIC_INTERFACE
def get_planets_for_date(date: str) -> List[Dict]:
    """Return a list of stub planetary positions for the given date.

    Args:
        date: ISO date string YYYY-MM-DD.

    Returns:
        List of planet dicts with keys:
          - name
          - right_ascension (hours, float)
          - declination (degrees, float)
          - distance_au (astronomical units, float)
    """
    _parse_date(date)  # Validate date
    # Planet names (exclude Earth for demo)
    planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    seed = sum(ord(c) for c in date)
    results: List[Dict] = []
    for idx, name in enumerate(planets):
        phase = (seed + idx * 37) % 360
        ra_hours = (phase / 15.0) % 24.0
        dec_deg = -23.4 + (phase % 47) - 23.5  # roughly within [-47, +0] for stub
        dist = 0.3 + ((idx + 1) * 0.7) + ((seed % 10) / 100.0)
        results.append(
            {
                "name": name,
                "right_ascension": round(ra_hours, 3),
                "declination": round(dec_deg, 3),
                "distance_au": round(dist, 3),
            }
        )
    return results
