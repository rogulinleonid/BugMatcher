import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_reference_bugs(sheet_url, sheet_name):
    scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    
    sheet = client.open_by_url(sheet_url).worksheet(sheet_name)
    data = sheet.get_all_records()
    
    reference_bugs = {}
    for row in data:
        reference_bugs[row['BugID']] = {
            'title': row['Title'],
            'description': row['Description'],
            'severity': row['Severity']
        }
    return reference_bugs
