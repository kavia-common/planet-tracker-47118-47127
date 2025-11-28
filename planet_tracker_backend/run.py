import os
from app import app

if __name__ == "__main__":
    """
    Backend entrypoint.

    Binds to 0.0.0.0 so the server is reachable from preview environment.
    Port defaults to 3001 to match the frontend expectation, but can be overridden
    via the PORT environment variable.
    """
    host = os.getenv("HOST", "0.0.0.0")
    try:
        port = int(os.getenv("PORT", "3001"))
    except ValueError:
        port = 3001

    debug = os.getenv("FLASK_DEBUG", "").lower() in ("1", "true", "yes", "on")
    # Use use_reloader False to avoid double-start issues in some CI/preview envs
    app.run(host=host, port=port, debug=debug, use_reloader=False)
