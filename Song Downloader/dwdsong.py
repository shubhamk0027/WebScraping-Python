import youtube_dl
import os
import requests,emoji,sys
from bs4 import BeautifulSoup as bs

# Add your own folder name
folderName = 'MySongs'

#Download config:
opts={
    'format':'bestaudio/best',
    'outtmpl':'%(title)s.%(ext)s',
    'nocheckcertificate':True,
    'min-views':1000000,
    'postprocessors':[{
        'key':'FFmpegExtractAudio',
        'preferredcodec':'mp3',
        'preferredquality':'320',
    }],
}

def dwdsong(link):
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    os.chdir(folderName)
    print('DOWNLOADING YOUR SONG....')
    with youtube_dl.YoutubeDL(opts) as dl:
        dl.download([link])
    print('SONG DOWNLOADED'+emoji.emojize(':thumbsup:',use_aliases=True))





name = str(input("ENTER NAME:"))
link='https://www.youtube.com/results?search_query='+name.replace(' ','+')+'&sp=CAASAhABQgQIABIA'
print('GETTING INFORMATION...')
page = requests.get(link)
soup = bs(page.text,'html.parser')
vids = soup.select('.yt-lockup-title')
print(str(len(vids))+' VIDEOS BY NAME \''+name+'\' FOUND!')
i=1
for vid in vids:
    print(i, vid.text)
    i=i+1

print("ENTER THE INDEX NUMBER OF THE SONG YOU WANT TO DOWNLOAD")
index = int(input())
link = "https://www.youtube.com"+vids[index-1].select('a')[0]['href']
dwdsong(link)


