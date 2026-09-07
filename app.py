"""
Dashboard Magang — Flask App
Upload Excel → tampilkan dashboard grafik.
"""
from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
import sheets

app = Flask(__name__)
app.secret_key = "dashboard-magang-secret"


@app.route("/", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        f = request.files.get("file")
        if not f or not f.filename:
            flash("Pilih file Excel terlebih dahulu.", "error")
            return redirect(url_for("dashboard"))
        if not f.filename.endswith((".xlsx", ".xls")):
            flash("File harus format .xlsx atau .xls", "error")
            return redirect(url_for("dashboard"))
        filepath = sheets.save_upload(f)
        sheets.set_current_file(filepath)
        flash(f"File '{f.filename}' berhasil diupload.", "success")
        return redirect(url_for("dashboard"))

    data = sheets.get_data()
    current = sheets.get_current_file()
    filename = None
    if current:
        import os
        filename = os.path.basename(current)
    return render_template("dashboard.html", data=data, filename=filename)


@app.route("/api/data")
def api_data():
    return jsonify(sheets.get_data())


if __name__ == "__main__":
    import config
    app.run(host="0.0.0.0", port=config.PORT, debug=True)
