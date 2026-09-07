"""
Koneksi ke Google Sheets via gspread + service account.
Baca data spreadsheet → list of dict.
"""
import gspread
from google.oauth2.service_account import Credentials
import config

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]


def get_client():
    """Buat gspread client dari service account credentials."""
    creds = Credentials.from_service_account_file(config.CREDS_FILE, scopes=SCOPES)
    return gspread.authorize(creds)


def get_data():
    """
    Baca seluruh data dari spreadsheet.
    Return: list of dict, satu dict per baris (header row = keys).
    Kolom yang diharapkan:
        No, Nama, NIM, Jenis Kelamin, Jenis Magang, Nama Sekolah / Universitas,
        Jurusan, Program Intership, Penempatan, No Hp,
        Tanggal Masuk, Tanggal Keluar, Waktu Magang, Mentor, Status
    """
    try:
        client = get_client()
        spreadsheet = client.open_by_key(config.SPREADSHEET_ID)
        worksheet = spreadsheet.worksheet(config.WORKSHEET_NAME)
        rows = worksheet.get_all_records()  # list of dict
        return rows
    except Exception as e:
        print(f"[Google Sheets Error] {e}")
        return []


# Kolom baku yang dipetakan dari spreadsheet
KOLOM_MAP = {
    "No": "no",
    "Nama": "nama",
    "NIM": "nim",
    "Jenis Kelamin": "jenis_kelamin",
    "Jenis Magang": "jenis_magang",
    "Nama Sekolah / Universitas": "universitas",
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


def get_normalized_data():
    """Baca data & normalisasi key ke snake_case."""
    raw = get_data()
    normalized = []
    for row in raw:
        item = {}
        for src_key, dst_key in KOLOM_MAP.items():
            item[dst_key] = str(row.get(src_key, "")).strip()
        normalized.append(item)
    return normalized
