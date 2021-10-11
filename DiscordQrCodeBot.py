import uuid
import os
import discord
from SecretConfig import *
from EthLib import *
from datetime import datetime
from DataService import *

now = datetime.now()
client = discord.Client()
dataService = DataService()

DiscordAccount = None
Scholars = None
Representative = None


@client.event
async def on_ready():
    print('\nWe are logged in as {0.user}'.format(client))


@client.event
# Listen for an in comming message
async def on_message(message):
    # If the author is the robot itself, then do nothing!
    if message.author == client.user:
        return
    # if author is not part of the discord
    if str(message.author.id) not in DiscordAccount:
        return

    authorName = getIskoName(message.author.id)

    if message.content.startswith("!qrof") and len(message.content.split(' ')) > 1:

        if len(message.mentions) > 0 and str(message.mentions[0].id):
            mentionIskoName = getIskoName(message.mentions[0].id)
        else:
            mentionIskoName = getIskoName(message.content.split(' ')[1])

        print('message content:')
        print(message.content)

        if not mentionIskoName:
            print(
                'Discord ID or Name is not map. Check if properly map with that ID or Name')
            await message.author.send('Discord ID or Name is not map. Check if properly map with that ID or Name')
            return

        if authorName in Managers:
            await sendQRCode(message, mentionIskoName)
        elif authorName in Representative and mentionIskoName in Representative[authorName]:
            await sendQRCode(message, mentionIskoName)
        elif authorName == mentionIskoName:
            await sendQRCode(message, mentionIskoName)
        else:
            print('No mention/tag')
            await message.author.send('No mention/tag')

    # If the user writes !qr
    elif message.content == "!qr":
        current_time = now.strftime("%H:%M:%S")
        print('\n')
        iskoName = getIskoName(message.author.id)
        # This for loop check for all the user's DiscordID in the Database
        if iskoName in Scholars:
            await sendQRCode(message, iskoName)
            return
        else:
            print("This user didn't receive a QR Code : " + message.author.name)
            print("Discord ID : " + str(message.author.id))
            print("Current time : ", current_time)
            return
    elif message.content == "!iskonames":
        list = []
        for x in Scholars:
            list.append(x)
        await message.channel.send(list)
    elif message.content == "!help":
        await message.channel.send('My commands are:\n!iskonames, !qr, !qrof, !ping, !help, !refreshCreds')
    elif message.content == "!ping":
        await message.channel.send('pong')
    elif message.content == "!refreshCreds" and authorName in Managers:
        refreshCreds()
        await message.author.send('refresh creds is  done')


def refreshCreds():
    print('fetching credentials from google sheet')
    global DiscordAccount, Scholars, Representative

    DiscordAccount = dataService.getDiscordAccounts()
    Scholars = dataService.getScholars()
    Representative = dataService.getRepresentatives()


def getIskoName(id):
    print('getIskoName: {}'.format(id))

    idLoweCase = str(id).lower()
    if str(id) in Scholars:
        return id

    for x in Scholars:
        if x.lower() == idLoweCase:
            return x

    if str(id) in DiscordAccount:
        return DiscordAccount[str(id)]

    for x in DiscordAccount:
        if x.lower() == idLoweCase:
            return DiscordAccount[x]

    return ''


def getUserFromMention(mention):
    if not mention:
        return

    if mention.startsWith('<@') and mention.endsWith('>'):
        mention = mention.slice(2, -1)

        if mention.startsWith('!'):
            mention = mention.slice(1)

        return mention


async def sendQRCode(message, scholarName):
    print("sendQRCode : " + scholarName)
    if scholarName in Scholars:
        print("Scholar Name : " + scholarName)
        print("Current time : ", now.strftime("%H:%M:%S"))
        # value with discordID
        botPlaceHolders = Scholars[scholarName]
        # discordID's privateKey from the database
        accountPrivateKey = botPlaceHolders[2].replace('0x', '')
        # discordID's EthWalletAddress from the database
        accountAddress = botPlaceHolders[1].replace('ronin:', '0x')
        # Get a message from AxieInfinty
        rawMessage = getRawMessage()
        # Sign that message with accountPrivateKey
        signedMessage = getSignMessage(rawMessage, accountPrivateKey)
        # Get an accessToken by submitting the signature to AxieInfinty
        accessToken = submitSignature(
            signedMessage, rawMessage, accountAddress)
        # Create a QrCode with that accessToken
        qrCodePath = f"QRCode_{message.author.id}_{str(uuid.uuid4())[0:8]}.png"
        qrcode.make(accessToken).save(qrCodePath)
        # Send the QrCode the the user who asked for
        await message.author.send(
            "------------------------------------------------\n\n\nHello " + message.author.name + "\nHere is the new QR Code of " + botPlaceHolders[0] + ": ")
        await message.author.send(file=discord.File(qrCodePath))
        os.remove(qrCodePath)
        return


print('This Discord QR Code Bot starting')

refreshCreds()

# Run the client (This runs first)
client.run(DiscordBotToken)
