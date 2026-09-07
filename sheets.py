"""
Baca data dari file Excel yang diupload.
Kolom yang diharapkan:
  No, Nama, NIM, Jenis Kelamin, Jenis Magang,
  Nama Sekolah / Universitas, Jurusan, Program Intership,
  Penempatan, No Hp, Tanggal Masuk, Tanggal Keluar,
  Waktu Magang, Mentor, Status
"""
import os
import openpyxl

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Kolom baku → snake_case
KOLOM_MAP = {
    "No": "no",
    "Nama": "nama",
    "NIM": "nim",
    "Jenis Kelamin": "jenis_kelamin",
    "Jenis Magang": "jenis_magang",
    "Nama Sekolah / Universitas": "universitas",
    "Nama Sekolah/Universitas": "universitas",
    "Jurusan": "jurusan",
    "Program Intership": "program",
    "Penempatan": "penempatan",
    "No Hp": "hp",
    "Tanggal Masuk": "tanggal_masuk",
    "Tanggal Keluar": "tanggal_keluar",
    "Waktu Magang": "waktu_magang",
    "Mentor": "mentor",
    "Status": "status",
}


def read_excel(filepath):
    """Baca .xlsx → list of dict (satu per baris)."""
    wb = openpyxl.load_workbook(filepath, read_only=True, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    wb.close()
    if not rows:
        return []
    # Header = baris pertama
    headers = [str(h).strip() if h else "" for h in rows[0]]
    data = []
    for row in rows[1:]:
        # Skip baris kosong
        if not any(cell for cell in row):
            continue
        item = {}
        for col_idx, header in enumerate(headers):
            # Map header ke snake_case
            mapped = KOLOM_MAP.get(header, header.lower().replace(" ", "_").replace("/", "_").replace("-", "_"))
            val = row[col_idx] if col_idx < len(row) else ""
            # Format tanggal dari datetime object
            if hasattr(val, "strftime"):
                val = val.strftime("%d %B %Y")
            item[mapped] = str(val).strip() if val is not None else ""
        data.append(item)
    return data


def save_upload(file_storage):
    """Simpan file upload ke uploads/, return path."""
    filename = file_storage.filename
    filepath = os.path.join(UPLOAD_DIR, filename)
    file_storage.save(filepath)
    return filepath


# State sederhana: path file terakhir yang diupload
_current_file = None


def set_current_file(path):
    global _current_file
    _current_file = path


def get_current_file():
    return _current_file


def get_data():
    """Baca data dari file yang aktif. Return list of dict."""
    if _current_file and os.path.exists(_current_file):
        return read_excel(_current_file)
    return []
