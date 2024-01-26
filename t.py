from googleapiclient.discovery import build

service = build('sheets', 'v4')

spreadsheets = service.spreadsheets()
new_sheet_request = spreadsheets.create(body={"properties": {"title": "Cloud Spreadsheet :)"}})
new_sheet_response = new_sheet_request.execute()
print(new_sheet_response)
# sheets = spreadsheets.sheets()
# print(sheets)

spreadsheet_id = "1qpD2HiaVwxgtCCyMdCV6JdR7aytZFwsi8WCpYJPc5U0"

values = [
    ["Cell A1", "Cell B1", "Cell C1"],

]

body = {
    'values': values
}

result = spreadsheets.values().append(
    spreadsheetId=spreadsheet_id,
    range="Sheet1",  # Update with your sheet name or range
    valueInputOption="RAW",
    body=body
).execute()

print(spreadsheet_id)

print("Values added to the spreadsheet.")



service.close()
