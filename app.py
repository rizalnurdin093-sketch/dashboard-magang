"""
Dashboard Magang — Flask App
"""
from flask import Flask, render_template, jsonify
import sheets

app = Flask(__name__)


@app.route("/")
def dashboard():
    data = sheets.get_normalized_data()
    return render_template("dashboard.html", data=data)


@app.route("/api/data")
def api_data():
    """JSON endpoint untuk grafik (fetch dari JS)."""
    return jsonify(sheets.get_normalized_data())


if __name__ == "__main__":
    import config
    app.run(host="0.0.0.0", port=config.PORT, debug=True)
