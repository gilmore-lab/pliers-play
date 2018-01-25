# mining_databrary.py
from pliers.stimuli import ImageStim
import urllib

img_url = "https://nyu.databrary.org/slot/15068/-/asset/63850/download?inline=true"
img_local = "peep_icon.html"
urllib.urlretrieve(img_url, img_local) # python 2.7

# Try wget
import wget
wget.download(img_url, "peep_icon.jpg")