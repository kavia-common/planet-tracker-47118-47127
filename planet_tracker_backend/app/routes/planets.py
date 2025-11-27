from datetime import datetime
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from webargs import fields
from webargs.flaskparser import use_kwargs

from ..providers.data_providers import get_planets_for_date
from ..schemas import PlanetListResponseSchema


blp = Blueprint(
    "Planets",
    "planets",
    url_prefix="/api/planets",
    description="Endpoints to retrieve planetary positions",
)


def _validate_date(date_str: str) -> None:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except Exception:
        abort(400, message="Invalid 'date' parameter. Expected format YYYY-MM-DD.")


@blp.route("")
class PlanetPositions(MethodView):
    """
    Get planetary positions for a specific date.

    Query Parameters:
      - date (required): YYYY-MM-DD

    Returns:
      JSON with key:
        items: list of planetary positions
    """

    # PUBLIC_INTERFACE
    @blp.response(200, PlanetListResponseSchema)
    @blp.doc(
        summary="Get planetary positions by date",
        description="Returns a list of planetary positions for the given date.",
        parameters=[
            {"in": "query", "name": "date", "schema": {"type": "string"}, "required": True},
        ],
        operationId="getPlanetPositionsByDate",
        tags=["Planets"],
    )
    @use_kwargs({"date": fields.Str(required=True)}, location="query")
    def get(self, date: str):
        """List planetary positions for a date."""
        _validate_date(date)
        items = get_planets_for_date(date=date)
        return {"items": items}
