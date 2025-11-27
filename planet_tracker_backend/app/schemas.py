"""Marshmallow schemas for API request/response validation and OpenAPI docs."""
from marshmallow import Schema, fields


class PaginationSchema(Schema):
    total = fields.Int(description="Total number of items")
    total_pages = fields.Int(description="Total number of pages")
    first_page = fields.Int(description="First page number")
    last_page = fields.Int(description="Last page number")
    page = fields.Int(description="Current page number")
    previous_page = fields.Int(allow_none=True, description="Previous page number")
    next_page = fields.Int(allow_none=True, description="Next page number")
    per_page = fields.Int(description="Items per page")


class NeoSchema(Schema):
    id = fields.Str(required=True, description="Unique identifier")
    name = fields.Str(required=True, description="Designation or name")
    close_approach_date = fields.Str(required=True, description="YYYY-MM-DD")
    relative_velocity_km_s = fields.Float(required=True, description="Relative velocity in km/s")
    miss_distance_km = fields.Float(required=True, description="Miss distance in km")
    is_potentially_hazardous = fields.Bool(required=True, description="Potentially hazardous flag")


class NeoListResponseSchema(Schema):
    items = fields.List(fields.Nested(NeoSchema), required=True, description="List of NEOs")
    pagination = fields.Nested(PaginationSchema, required=True)


class PlanetSchema(Schema):
    name = fields.Str(required=True, description="Planet name")
    right_ascension = fields.Float(required=True, description="Right ascension in hours")
    declination = fields.Float(required=True, description="Declination in degrees")
    distance_au = fields.Float(required=True, description="Distance in astronomical units")


class PlanetListResponseSchema(Schema):
    items = fields.List(fields.Nested(PlanetSchema), required=True, description="List of planetary positions")
