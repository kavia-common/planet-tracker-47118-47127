from flask import Flask
from flask_cors import CORS
from flask_smorest import Api
import os

from .routes.health import blp as health_blp
from .routes.neos import blp as neos_blp
from .routes.planets import blp as planets_blp


app = Flask(__name__)
app.url_map.strict_slashes = False

# Enable CORS for frontend integration.
# If PREVIEW_ORIGIN (e.g., https://<preview-host>:3000) is provided, restrict to that.
# Otherwise default to "*" which is acceptable for our preview workspace.
preview_origin = os.getenv("PREVIEW_ORIGIN")
cors_origins = preview_origin if preview_origin else "*"
CORS(
    app,
    resources={
        r"/api/*": {
            "origins": cors_origins,
            "supports_credentials": True,
            "allow_headers": ["Content-Type", "Authorization"],
            "methods": ["GET", "OPTIONS"],
        },
        r"/docs*": {
            "origins": cors_origins,
            "supports_credentials": True,
            "allow_headers": ["Content-Type", "Authorization"],
            "methods": ["GET", "OPTIONS"],
        },
    },
)

# API/Docs metadata
app.config["API_TITLE"] = "Planet Tracker API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_PATH"] = ""
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(health_blp)
api.register_blueprint(neos_blp)
api.register_blueprint(planets_blp)
