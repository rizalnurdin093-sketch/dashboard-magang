"""Production runner — dashboard magang."""
import app
import config

if __name__ == "__main__":
    app.app.run(host="0.0.0.0", port=config.PORT, debug=False, use_reloader=False)
