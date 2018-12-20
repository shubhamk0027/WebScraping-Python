import requests
import os
from bs4 import BeautifulSoup as bs

baseURL = "https://www.ibiblio.org/ram/"
page= requests.get(baseURL+"bcst_all.htm")

soup= bs(page.text,'html.parser')
songs = soup.find_all('table')[4].select('li a')

folderName = 'Bhajans'
if(not os.path.exists(folderName)):
    os.mkdir(folderName)
os.chdir('./'+folderName)

def dwd(song):
    name ="unknown"
    try:
        name = " ".join(song.contents[0].split()) 
        print("Name: "+song.contents[0].replace('\n',' ').replace('  ',''))
    except:
        print("SONG ITEM DOES NOT HAS ANY CONTENT!")
    print("URL: "+ baseURL+song['href'])
    print("Downloading Song...")
    r = requests.get(baseURL+song['href'])
    print("Song Downloaded ./"+folderName)
    open(name+'.mp3','wb').write(r.content)


for song in songs:
    dwd(song)
