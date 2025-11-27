from flask_smorest import Blueprint
from flask.views import MethodView

# Health endpoint under /api/health with proper tag/description
blp = Blueprint("Health", "health", url_prefix="/api/health", description="Health check route for Planet Tracker API")

@blp.route("")
class HealthCheck(MethodView):
    """
    Simple health check endpoint.

    Returns:
      JSON: {"status": "ok"}
    """

    # PUBLIC_INTERFACE
    def get(self):
        """Return basic service health status."""
        return {"status": "ok"}
