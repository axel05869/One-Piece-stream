from pathlib import Path
import os

class colors:
  reset = "\033[0m"
  blue = "\033[34m"
  brightblue = "\033[34;1m"
  yellow = "\033[33m"
  brightyellow = "\033[33;1m"
  brightred = "\033[31;1m"


def dataPath():
    path = str(Path.home()/'opstream_data')
    return path


def makePath(path):
    if not os.path.exists(path):
        os.makedirs(path)


opstreamlogo = f'''
{colors.brightblue}
   ___   ____  _____  ________   _______  _____  ________    ______  ________  
 .'   `.|_   \|_   _||_   __  | |_   __ \|_   _||_   __  | .' ___  ||_   __  | 
/  .-.  \ |   \ | |    | |_ \_|   | |__) | | |    | |_ \_|/ .'   \_|  | |_ \_| 
| |   | | | |\ \| |    |  _| _    |  ___/  | |    |  _| _ | |         |  _| _  
\  `-'  /_| |_\   |_  _| |__/ |  _| |_    _| |_  _| |__/ |\ `.___.'\ _| |__/ | 
 `.___.'|_____|\____||________| |_____|  |_____||________| `.____ .'|________|{colors.yellow} `stream

{colors.reset}
'''

def generate_html(videolink, episodenumber, episodetitle):
  html_str = f'''
  <!DOCTYPE html>
  <html style="height:100%;">
  <head>
    <title>One Piece - Episode {episodenumber}</title>
  </head>
  <body style="height:100%; background-color:#0B0B0C;">
    <div style="height:100%; width:1280px; padding-top: 50px; margin:0 auto;">
      <a href="{videolink}" download style="color:#C8C3BC; font-family:Gill Sans,sans-serif; float:right; margin-bottom: 8px;">
      <img src="https://cutt.ly/xlsxwwc" width="40px" title="Download">
      </a>
      <center>
      <video width="1280" height="720" controls>
      <source src="{videolink}" type=video/mp4>
      </video>
      </center>
      <h2 style="color:#C8C3BC; font-family:Gill Sans,sans-serif; float:left;">Episode {episodenumber} - {episodetitle}</h2>
      <image src="https://bit.ly/2NoMmcp" style="width:220px; margin-top:8px; float:right;" alt="One Piece Logo">
    </div>
  </body>
  </html>
  '''
  return html_str