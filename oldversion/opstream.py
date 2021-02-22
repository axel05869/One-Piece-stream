from bs4 import BeautifulSoup
import requests
import webbrowser
import re # to find complicated str
from pathlib import Path
# this will fix ansii color not working on terminal
import colorama
colorama.init()

class colors:
	reset = "\033[0m"
	blue = "\033[34m"
	brightblue = "\033[34;1m"
	yellow = "\033[33m"
	brightyellow = "\033[33;1m"
	brightred = "\033[31;1m"

def savePath():
    path = str(Path.home()/'Documents')
    return path

def video_link_grabber(episodelink):
	html_ep = requests.get(episodelink).text
	soup_ep = BeautifulSoup(html_ep, 'html.parser')
	
	script = soup_ep.find_all('script') # to reduce the url results
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(script)) # convert soup to text to work
	
	# sort out other links
	videolink = ''
	for url in urls:
		if '.mp4' in url: # this is the video
			# remove unnecessary char
			for char in url:
				if '\\' not in char:
					videolink = videolink + char
	
	return videolink



print(f'''
{colors.brightblue}
   ___   ____  _____  ________   _______  _____  ________    ______  ________  
 .'   `.|_   \|_   _||_   __  | |_   __ \|_   _||_   __  | .' ___  ||_   __  | 
/  .-.  \ |   \ | |    | |_ \_|   | |__) | | |    | |_ \_|/ .'   \_|  | |_ \_| 
| |   | | | |\ \| |    |  _| _    |  ___/  | |    |  _| _ | |         |  _| _  
\  `-'  /_| |_\   |_  _| |__/ |  _| |_    _| |_  _| |__/ |\ `.___.'\ _| |__/ | 
 `.___.'|_____|\____||________| |_____|  |_____||________| `.____ .'|________|{colors.yellow} `stream

{colors.reset}
''')

html = requests.get('https://4anime.to/anime/one-piece').text
soup = BeautifulSoup(html, 'html.parser')

# get episode data
eplist = soup.find('ul', {'class': 'episodes range active'})
eplinks = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(eplist))

# alternative method to get urls
#link = chapterlist.find_all('a')
#eplinks = []
#for link in atag:
#    eplinks.append(link['href'])


while True:
	inputep = int(input(f'Input episode number to watch. between 1 to {len(eplinks)}: '))
	inputep -= 1 # index list starts at 0. -1 will allow to get list data correctly

	videolink = video_link_grabber(eplinks[inputep])
	print(f'\t{colors.brightred}Watching One Piece - Episode {inputep + 1}{colors.reset}')
	print(f'\t{colors.brightred}Direct link : {videolink}{colors.reset}\n')


	# attach video link to html
	html_str = f'''
	<!DOCTYPE html>
	<html style="height:100%;">
	<head>
		<title>One Piece - Episode {inputep + 1}</title>
	</head>
	<body style="height:100%; background-color:#0B0B0C;">
		<div style="height:100%; width:1280px; padding-top: 50px; margin:0 auto;">
			<center>
			<video width="1280" height="720" controls>
			<source src="{videolink}" type=video/mp4>
			</video>
			</center>
			<h3 style="color:#C8C3BC; font-family:Gill Sans,sans-serif; float:left;">Episode {inputep + 1}</h4>
			<image src="https://bit.ly/2NoMmcp" style="width:250px; margin-top:8px; float:right;" alt="One Piece Logo"></image>
		</div>
	</body>
	</html>
	'''

	# save html to file
	saveTo = f'{savePath()}/opstream.html'
	with open(saveTo, "w") as html:
		html.write(html_str)

	# open html to default browser
	webbrowser.open(f'file:///{saveTo}')

	# open on specific browser
	#webbrowser.register('firefox',
	#	None,
	#	webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
	#webbrowser.get('firefox').open(f'file:///{saveTo}')
