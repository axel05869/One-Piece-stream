import os
import webbrowser
import colorama

from modules.grabber import *
from modules.misc import *


colorama.init() # this will fix ansii color not working on terminal
print(opstreamlogo)


# last watch episode
try:
	with open(f'{os.getcwd()}/data/lastwatch.txt', 'r') as f:
		lastwatch = f.read()
		print(colors.brightyellow + lastwatch + colors.reset)
except FileNotFoundError:
	pass


print(f'\nrequesting data...')
try:
	episodetitles, episodetypes = episode_info_grabber()
	episodelinks = episode_link_grabber()
except:
	print(f'Connection error!\n')
	os.system('pause')
	exit()


while True:
	while True:
		try:
			inputep = int(input(f'Input episode number to watch. between 1 to {len(episodelinks)}: '))
			if inputep > len(episodelinks) or inputep < 1:
				continue
			else:
				if episodetypes[inputep - 1] == 'Filler': # warn if episode is a filler
					totalfiller = filler_count(episodetypes,inputep - 1) - 1
					if totalfiller == 0:
						print('\nThis episode is a filler')
					else:
						print(f'\nThis, and the next {totalfiller} episode is a filler')
					print(f'Do you want to watch this episode? It is not part of the storyline so its okay for you to skip this.\nType \'{colors.brightred}yes{colors.reset}\' to watch, Enter to skip')
					if input('>') in ['yes', 'Yes']:
						break
				else:
					break
		except ValueError:
			continue

	with open(f'{os.getcwd()}/data/lastwatch.txt', 'w') as f: # save input to lastwatch
		lastwatch = f.write(f'Last Watch: Episode {inputep} - {episodetitles[inputep-1]}')

	try:
		videolink = video_link_grabber(episodelinks[inputep - 1]) # index list starts at 0. -1 will allow to get list data correctly
	except:
		print(f'Connection error!\n')
		os.system('pause')
		exit()

	print(f'\t{colors.brightred}One Piece - Episode {inputep}{colors.reset}')
	print(f'\t{colors.brightred}{episodetitles[inputep-1]}{colors.reset}')
	print(f'\t{colors.brightred}Direct link : {videolink}{colors.reset}\n')


	# attach data to html and open on browser
	generate_html = html(videolink, inputep, episodetitles[inputep-1])
	saveAs = f'{os.getcwd()}/data/videostream.html'
	with open(saveAs, "w") as html:
		html.write(generate_html)
	
	webbrowser.open(f'file:///{saveAs}')
