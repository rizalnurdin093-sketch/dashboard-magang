"""WSGI entry — mount app di /magang/ (Nginx proxy)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from app import app as flask_app

# Mount app di prefix /magang
application = DispatcherMiddleware(
    flask_app,  # root: kosong
    {
        '/magang': flask_app
    }
)

if __name__ == '__main__':
    import config
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', config.PORT, application, use_reloader=False)
