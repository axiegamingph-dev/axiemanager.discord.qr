# Axie Infinity Scholars QR Code Discord bot

- This is a Discord bot that will provide a QR Code to your Axie Infinity scholars.
- This version of the bot is compatible with ronin and metamask

- If you want to use it with Ethereum information instead:

In submitSignature function, change "mainnet":"ronin" to "mainnet":"ethereum"

## Setup

1. Create your own Discord bot by following this tutorial: https://discordpy.readthedocs.io/en/stable/discord.html
2. Install the required modules by running:
   for ubuntu

- `chmod +x install-ubuntu.sh`
- `sudo ./install-ubuntu.sh`

for windows

- `install-windows.cmd`

3. A Google Cloud Platform project with the Google Sheets API enabled. To create a project and enable an Google Sheets API, refer to Create a project and enable the API : https://developers.google.com/docs/api/quickstart/python
4. Create Service Accounts credentials. To learn how to create credentials, refer to Create credentials : https://developers.google.com/workspace/guides/create-credentials
5. Save the json token to creds.json file.

# Setup

1. Clone or download the code:

- `git clone https://github.com/axiegamingph-dev/axiemanager.discord.qr`

2. Install the needed packages by running:

3. Follow this tutorial to create and add a bot to your Discord Server:

- `https://discordpy.readthedocs.io/en/stable/discord.html`

4. Update the SecretConfig.py for the names of managers and discord oauth token
5. Run the script by running in to correct path:

- `python3 ./DiscordQrCodeBot.py`

# Features

- [x] Create a QR Code Bot
- [x] All ronin/metamask keys are stored in google sheet

Please tell me if you experience any bugs...

# Donations

Buy me a coffee!
Thank you!

- Ronin Wallet Address: ronin:67a3d9ef3058d94d941408109bd715a47804c222

# Help

If you need help with setup or you have any question or suggestion, please message on Discord: nottoday#5269