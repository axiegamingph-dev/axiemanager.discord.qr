import os.path
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from collections import namedtuple
import httplib2
from SecretConfig import *

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']


#Data Types
Scholar = namedtuple("Scholar", "name address private_key")

class DataService:
    def getData(self,cellRange):
        creds = ServiceAccountCredentials.from_json_keyfile_name(
                    'creds.json', SCOPES)

        http = httplib2.Http()
        http = creds.authorize(http)

        service = build('sheets', 'v4', http=http)
        # service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()

        result = sheet.values().get(spreadsheetId=ISKO_SPREADSHEET_ID,
                    range=cellRange).execute()
        return result.get('values', [])


    def getScholars(self):
        values = self.getData(ISKO_Accounts)

        scholars = {}
        if not values:
            print('No scholar data found.')
        else:
            # columns A, B and C, which correspond to indices 0, 1 and 2.
            for row in values:
                if row and len(row) > 0:
                    scholars[row[0]] = row
        return scholars
    
    def getDiscordAccounts(self):
        values = self.getData(ISKO_DiscordAccount)

        discordAccounts = {}
        if not values:
            print('No discord accounts data found.')
        else:
            # columns A, B and C, which correspond to indices 0, 1 and 2.
            for row in values:
                if row and len(row) > 0:
                    name = row[0]
                    discordId = row[1]

                    if name and discordId:
                        discordAccounts[name] = discordId
                        discordAccounts[discordId] = name
        return discordAccounts

    def getRepresentatives(self):
        values = self.getData(ISKO_Representative)

        represnatives = {}
        if not values:
            print('No representatives data found.')
        else:
            # columns A, B and C, which correspond to indices 0, 1 and 2.
            for row in values:
                if row and len(row) > 0:
                    represnative = row[0]
                    targetName = row[1]

                    if represnative and targetName:
                        if represnative in represnatives:
                            list = represnatives[represnative]
                        else:
                            list = []
                            represnatives[represnative] = list
                        
                        list.append(targetName)

        return represnatives