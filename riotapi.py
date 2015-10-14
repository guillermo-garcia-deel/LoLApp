import json
import urllib2
import time
import signal
import sys
import random
import RPi.GPIO as GPIO
from lists import keylist
from lists import namelist
from lists import menu

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)


key = '9c810c33-25b4-4857-b974-5576d0eefc38'

#Function to do random light show
def light_show():
	for i in range(0,2):
		leds = [17,22,27]
		num = leds[random.randrange(0,3,1)]
		GPIO.output(num,GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(num,GPIO.LOW)

def light_show_end():
	for i in range (0,10):
		leds = [17,22,27]
		for i in range (0,3):
			GPIO.output(leds[i],GPIO.HIGH)
			time.sleep(0.2)
			GPIO.output(leds[i],GPIO.LOW)

#Signal Handler to detect keyboard input to close program.
def signal_handler(signal, frame):
	GPIO.output(17,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)		
	GPIO.output(27,GPIO.LOW)
	sys.exit()


#Get summoner ID by name
def get_summoner_id(summoner,region):
	url_summoner = summoner.replace(' ', '%20')
	data_summoner = summoner.replace(' ', '')
	url = "https://"+str(region)+".api.pvp.net/api/lol/"+str(region)+"/v1.4/summoner/by-name/"+url_summoner+"?api_key=" + key
	json_obj = 	urllib2.urlopen(url)
	data = json.load(json_obj)
	summoner_id = data[data_summoner]['id']

	return summoner_id


def season_info_single(season,summoner_id,doThis,champOrAll,region):
	if season == 'season3':
		season = 'SEASON3'
	elif season == 'season4':
		season = 'SEASON2014'
	url = "https://"+str(region)+".api.pvp.net/api/lol/"+str(region)+"/v1.3/stats/by-summoner/"+str(summoner_id)+"/ranked?season="+season+"&api_key=" + key
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)
	found = False
	champion = champOrAll.replace(' ','')

	for item in data['champions']:
		if str(id_to_name(item['id'])).lower() == champion.lower():
			print str(namelist[doThis]) + " by " + str(id_to_name(item['id'])) + ": " + str(item['stats'][keylist[doThis]]) 
			light_show()
			found = True
			break
	if found == False:
		print("You did not use " + champion.title() + " on " + season)
		light_show()

#Display Information about a certain ranked season for all champions
def season_info(season,summoner_id, doThis,region):
	if season == 'season3':
		season = 'SEASON3'
	elif season == 'season4':
		season = 'SEASON2014'
	url = "https://"+str(region)+".api.pvp.net/api/lol/"+str(region)+"/v1.3/stats/by-summoner/"+str(summoner_id)+"/ranked?season="+season+"&api_key=" + key
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)
	count = 1
	total = 0


	for item in data['champions']:
			champ_name = str(id_to_name(item['id']))
			if str(champ_name) == '0':
				champ_name = 'All'

			if champ_name != 'All':	
				print str(count) + ". " + str(namelist[doThis]) + " by " + champ_name + ": " + str(item['stats'][keylist[doThis]])
				light_show()
				count += 1
			if champ_name == 'All':
				total = item['stats'][keylist[doThis]]
	print str(namelist[doThis]) + " by All: " + str(total)
	light_show_end()
		


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


signal.signal(signal.SIGINT, signal_handler)
running = True
print('Type in \'q\' or \'Q\' to exit the program.\n\n')
summoner = raw_input("Enter summoner name: ")

if summoner.lower() == 'q':
	quit()


region = raw_input('Enter region (na, eu, kr, br eune, euw, lan, las, oce, ru, tr): ')

if region.lower() == 'q':
	quit()

while running == True:
	season = raw_input("Enter \"season3\" or \"season4\" to choose a season to display info about: ")
	if season.lower() == 'q':
		running = False
		break

	champOrAll = raw_input('Enter the name of a Champion to find his stats or \'all\' to display stats of all champions: ')
	if champOrAll.lower() == 'q':
		runnig = False
		break

	print(menu)

	doThis = raw_input("Choose One: ")
	if doThis.lower() == 'q':
		running = False
		break


	#file_name = raw_input("All your information will be dumped in a text file, pick a name for it: ")

	summoner_id = get_summoner_id(summoner.lower(),region)

	if champOrAll.lower() == 'all':
		season_info(season,summoner_id, doThis, region)
	elif champOrAll != 'all':
		season_info_single(season,summoner_id, doThis,champOrAll, region)




