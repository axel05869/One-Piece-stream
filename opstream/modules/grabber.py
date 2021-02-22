from bs4 import BeautifulSoup
import requests
import re


def episode_info_grabber():
	html = requests.get('https://www.animefillerlist.com/shows/one-piece').text
	soup = BeautifulSoup(html, 'html.parser')
	find1 = soup.find('tbody')
	find2 = find1.find_all('a')
	find3 = find1.find_all('span')

	eptitles = []
	for title in find2:
		eptitles.append(title.text)

	eptypes = [] # if its filler or canon
	for types in find3:
		eptypes.append(types.text)

	return eptitles, eptypes


def episode_link_grabber():
    html = requests.get('https://4anime.to/anime/one-piece').text
    soup = BeautifulSoup(html, 'html.parser')

    eplist = soup.find('ul', {'class': 'episodes range active'})
    eplinks = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(eplist)) # convert soup to text to work
    return eplinks


def video_link_grabber(episodelink):
	html = requests.get(episodelink).text
	soup = BeautifulSoup(html, 'html.parser')
	
	script = soup.find_all('script') # to reduce the url results
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(script))
	
	# sort out other links
	videolink = ''
	for url in urls:
		if '.mp4' in url: # this is the video
			# remove unnecessary char
			for char in url:
				if '\\' not in char:
					videolink = videolink + char
	return videolink


def filler_count(typelist, start): # count if the next ep is filler
	fillercount = 0
	for tayp in typelist[start:]:
		if tayp == 'Filler':
			fillercount += 1
		else:
			return fillercount

