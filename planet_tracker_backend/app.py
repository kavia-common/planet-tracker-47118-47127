import os
from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    """
    PUBLIC_INTERFACE
    create_app
    Factory to create the Flask app with permissive CORS for previews.

    CORS behavior:
    - If PREVIEW_ORIGIN is set (single origin), use that origin with supports_credentials=True.
    - If PREVIEW_ORIGIN is NOT set, allow wildcard '*' for /api/* with supports_credentials=False.
    - Allowed methods: GET, OPTIONS
    - Allowed headers: Content-Type, Authorization
    """
    app = Flask(__name__)

    preview_origin = os.environ.get("PREVIEW_ORIGIN", "").strip()
    if preview_origin:
        # Specific origin, credentials allowed
        CORS(
            app,
            resources={r"/api/*": {"origins": preview_origin}},
            supports_credentials=True,
            methods=["GET", "OPTIONS"],
            allow_headers=["Content-Type", "Authorization"],
        )
    else:
        # Wildcard origin, NO credentials allowed
        CORS(
            app,
            resources={r"/api/*": {"origins": "*"}},
            supports_credentials=False,
            methods=["GET", "OPTIONS"],
            allow_headers=["Content-Type", "Authorization"],
        )

    # Example minimal routes to ensure CORS on required endpoints.
    @app.route("/api/health", methods=["GET", "OPTIONS"])
    def health():
        """
        PUBLIC_INTERFACE
        Health endpoint
        Returns a simple JSON to indicate the service is up.
        """
        return jsonify({"status": "ok"})

    # Note: The actual /api/neos and /api/planets should already exist in the project.
    # This file ensures CORS behavior; if handlers exist elsewhere and app factory differs,
    # integrate the CORS block into the existing app initialization instead.

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "3001")))
