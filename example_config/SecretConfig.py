Managers = ['Shim', 'Mike', 'Ryan', 'Kevin', 'Wessa', 'ser0wl']

# google spreedsheet id
ISKO_SPREADSHEET_ID = ''

# the list of names with discord ID
ISKO_DiscordAccount = 'DiscordAccount!A2:B100'

# the list of Names, ronin address, ronin private keys
# eg:
# Name      | Address                               | Privatekey
# Isko1     | ronin:8213789127387543adfgsasdkjsd... | 0x0666c1234567890...
# Isko2     | ronin:8213789127387543adfgsasdkjsd... | 0x0666c1234567890...
# Isko3     | ronin:8213789127387543adfgsasdkjsd... | 0x0666c1234567890...

# note: Name should map to the ISKO_DiscordAccount values

ISKO_Accounts = 'Isko!A2:C100'

# list of names that can request qr code on behalf of that person.
# eg:
# Representative    | IskoName
# Isko1             | Isko1
# Isko1             | Isko2
# this means Isko1 can request code for Isko1 and Isko2 using the !qrof Isko1 and !qrof Isko2.
ISKO_Representative = 'Representative!A2:B100'

# Put Your Discord Bot Token Here
DiscordBotToken_Prod = ''
DiscordBotToken_Test = ''
DiscordBotToken = DiscordBotToken_Prod
