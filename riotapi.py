import json
import urllib2
from lists import keylist
from lists import namelist
from lists import menu

key = '9c810c33-25b4-4857-b974-5576d0eefc38'

#Get summoner ID by name
def get_summoner_id(summoner):
	url_summoner = summoner.replace(' ', '%20')
	data_summoner = summoner.replace(' ', '')
	url = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/"+url_summoner+"?api_key=" + key
	json_obj = 	urllib2.urlopen(url)
	data = json.load(json_obj)
	summoner_id = data[data_summoner]['id']

	return summoner_id

#Display Information about a certain ranked season
def season_info(season,summoner_id, doThis):
	if season == 'season3':
		season = 'SEASON3'
	elif season == 'season4':
		season = 'SEASON2014'
	url = "https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/"+str(summoner_id)+"/ranked?season="+season+"&api_key=" + key
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)
	total = 0
	


	for item in data['champions']:
			champ_name = str(id_to_name(item['id']))
			if str(champ_name) == '0':
				champ_name = 'All'
			print str(namelist[doThis]) + " by " + champ_name + ": " + str(item['stats'][keylist[doThis]]) 
		



#Change champion ID  to name
def id_to_name(champ_id):
	if champ_id != 0:
		url = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/"+str(champ_id)+"?locale=en_US&api_key=" + key
		json_obj = urllib2.urlopen(url)
		data = json.load(json_obj)
		champ_name = data['key']

		return champ_name

	else:
		return 0




summoner = raw_input("Enter summoner name: ")
season = raw_input("Enter \"season3\" or \"season4\" to choose a season to display info about: ")

print(menu)

doThis = raw_input("Choose One: ")


#file_name = raw_input("All your information will be dumped in a text file, pick a name for it: ")

summoner_id = get_summoner_id(summoner.lower())
season_info(season,summoner_id, doThis)




