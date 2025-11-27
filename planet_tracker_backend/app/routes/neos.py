from datetime import datetime
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from webargs import fields
from webargs.flaskparser import use_kwargs

from ..providers.data_providers import get_neos_for_date
from ..schemas import NeoListResponseSchema


blp = Blueprint(
    "NEOs",
    "neos",
    url_prefix="/api/neos",
    description="Endpoints to retrieve Near-Earth Objects (NEOs) data",
)


def _validate_date(date_str: str) -> None:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except Exception:
        abort(400, message="Invalid 'date' parameter. Expected format YYYY-MM-DD.")


@blp.route("")
class NeosList(MethodView):
    """
    Get a paginated list of Near-Earth Objects (NEOs) for a specific date.

    Query Parameters:
      - date (required): YYYY-MM-DD
      - page (optional): integer >= 1
      - per_page (optional): integer between 1 and 100

    Returns:
      JSON with keys:
        items: list of NEOs
        pagination: pagination metadata
    """

    # PUBLIC_INTERFACE
    @blp.response(200, NeoListResponseSchema)
    @blp.doc(
        summary="List NEOs by date",
        description="Returns a paginated list of near-earth objects for the given date.",
        parameters=[
            {"in": "query", "name": "date", "schema": {"type": "string"}, "required": True},
            {"in": "query", "name": "page", "schema": {"type": "integer"}, "required": False},
            {"in": "query", "name": "per_page", "schema": {"type": "integer"}, "required": False},
        ],
        operationId="listNeosByDate",
        tags=["NEOs"],
    )
    @use_kwargs(
        {
            "date": fields.Str(required=True),
            "page": fields.Int(load_default=1),
            "per_page": fields.Int(load_default=10),
        },
        location="query",
    )
    def get(self, date: str, page: int, per_page: int):
        """List NEOs for a date with pagination."""
        _validate_date(date)
        if page < 1:
            abort(400, message="'page' must be >= 1")
        if per_page < 1 or per_page > 100:
            abort(400, message="'per_page' must be between 1 and 100")

        items, pagination = get_neos_for_date(date=date, page=page, per_page=per_page)
        return {"items": items, "pagination": pagination}
