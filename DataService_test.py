from DataService import *

dataService = DataService()

discordAccounts = dataService.getDiscordAccounts()
print(discordAccounts)

scholars = dataService.getScholars()
print(scholars)

representatives = dataService.getRepresentatives()
print(representatives)
