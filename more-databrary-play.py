import requests

print('Beginning file download with requests')

url = 'https://nyu.databrary.org/party/6/avatar?size=96'  
r = requests.get(url)

with open('/Users/rick/Downloads/rog.jpg', 'wb') as f:  
    f.write(r.content)

# url = "https://nyu.databrary.org/slot/12212/0,15046/asset/46748/download?inline=true"
# r = requests.get(url)
# with open('/Users/rick/Downloads/snd.mp3', 'wb') as f:  
#     f.write(r.content)

import wget
wget.download(url, '/Users/rick/Desktop/rog.jpg')
wget.download("https://nyu.databrary.org/slot/12212/0,15046/asset/46748/download?inline=true", "/Users/rick/Desktop/snd.mp3")