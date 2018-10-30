import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

def mark_attendance():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    
    sheet = client.open('Attendance').sheet1
    
    result = sheet.get_all_records()
    pp = pprint.PrettyPrinter()
    pp.pprint(result)
    
mark_attendance()
