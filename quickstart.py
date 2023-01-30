from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of a sample spreadsheet.
SPREADSHEET_ID = '1DNoNf4glcuMxKoVzHVrFo-MktmsVji1wf4IHeraWH84'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="A1:B2").execute()
values = result.get('values', [])
print(values)

aoa = [["3/1/2022", 4000],["4/4/2022", 3000],["7/12/2022", 7000]]
request = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
                                range="Sheet2!B2", valueInputOption="USER_ENTERED",
                                body={"values":aoa})
response = request.execute()
print(response)
