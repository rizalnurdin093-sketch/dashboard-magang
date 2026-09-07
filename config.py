"""
Konfigurasi Dashboard Magang.

Google Sheets:
- SPREADSHEET_ID: dari URL spreadsheet
  Contoh: https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit
- CREDS_FILE: path ke service account JSON (dari Google Cloud Console)
- WORKSHEET_NAME: nama sheet/tab di dalam spreadsheet

Cara setup Google Sheets API:
1. Buka console.cloud.google.com → buat project
2. Enable Google Sheets API + Google Drive API
3. Buat Service Account → download JSON credential
4. Share spreadsheet ke email service account (editor)
"""
import os

SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID", "")
CREDS_FILE = os.environ.get("CREDS_FILE", "credentials.json")
WORKSHEET_NAME = os.environ.get("WORKSHEET_NAME", "Sheet1")
PORT = int(os.environ.get("PORT", 5003))
