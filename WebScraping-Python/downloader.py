import requests,emoji,sys
from pytube import YouTube, Playlist 
from bs4 import BeautifulSoup as bs

song=False
byname=False
playlist=False
playlists=[
    #enter links here
]
res=[
    ['360p','480p','720p','1080p'],
    ['480p','360p','720p','1080p'],
    ['720p','480p','360p','1080p'],
    ['1080p','720p','480p','360p']
]
defaultres =-1
#headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'}


opt=int(input('\nDO YOU WANT TO DOWNLOAD PLAYLIST/SINGLE FILE(1/0)'))
if opt==1 : 
    playlist=True
else:    
    opt= int(input('SEARCH BY NAME/LINK?(1/0)'))
    if opt==1 : byname=True
opt= int(input('DOWNLOAD SONG/VIDEO(1/0)'))
if opt==1 : song=True


def resorder():
    if defaultres != -1: 
        print('DEFAULT RESOLUTION AVAILABLE!')
        return res[defaultres]
    opt =int(input('ENTER RESOLUTION PREFERENCE ORDER-\n'+str(res[0])+str(res[1])+str(res[2])+' (0/1/2/3)'))
    if opt >3 or opt <0:
        print('RESOLUTION NOT VALID!')
        return resorder()
    print('DOWNLOADING AT '+str(res[opt]))    
    return res[opt]    

def dwdvideo(link,res):
    yt = YouTube(link)
    print('SEARCHING VIDEO....')
    for r in res:
        vs = yt.streams.filter(res=r).all()
        if len(vs)==0:
            print(r+' NOT AVAILABLE')
        else:
            print('RESOLUTION AT '+r)
            break    
    #vs.all() made a list    
    #print(vs[0])
    print('DOWNLOADING VIDEO....')
    #print(link)
    vs[0].download()
    print('VIDEO DOWNLOADED'+emoji.emojize(':thumbsup:',use_aliases=True))


def dwdsong(link):
    print('EXTRACTING SONG...')
    #print(link)
    songs= YouTube(link).streams.filter(only_audio=True).all() # a list 
    print('DOWNLOADING SONG....')
    song =songs[0].download()   
    print(song.title)
    print('SONG DOWNLOADED'+emoji.emojize(':thumbsup:',use_aliases=True))
    # yt = YouTube(link).streams.filter(only_audio=True)  not a list since .all() is not added
    # print(yt.all())
    # yt.download() 



if playlist:
    link = input('ENTER LINK OF THE PLAYLIST')
    #link='https://www.youtube.com/watch?v=ADvbXr6kLNw&list=PLGLfVvz_LVvQiyIiurLo0KRVu0cd0c8dp'
    page=requests.get(link)
    soup= bs(page.text,'html.parser')
    file=open('1.html','w')
    for s in soup:
        file.write(str(s))
    vids = soup.select('.playlist-video')
    if len(playlists)==0:
        for v in vids:
            playlists.append('https://www.youtube.com'+v['href'])
    opt=int(input('DO YOU WANT TO PROVIDE SEPARATE RESOLUTION ORDER FOR EACH VIDEO?(1/0)'))
    if opt==0:
        defaultres=resorder()
    for link in playlists:
        dwdvideo(link,resorder())        
        print(link,resorder())

elif byname:
    name = input("ENTER NAME:")
    #name='kuch to h tujhse rabta'  
    link='https://www.youtube.com/results?search_query='+name.replace(' ','+')+'&sp=CAASAhABQgQIABIA'
    print('GETTING INFORMATION...')
    #print(link)
    page = requests.get(link)
    soup = bs(page.text,'html.parser')
    file=open('1.html','w')
    for s in soup:
        file.write(str(s))
    vids = soup.select('.yt-lockup-title')
    print(str(len(vids))+' VIDEOS BY NAME \''+name+'\' FOUND!')
    for vid in vids:
        print(vid.text)
        nxt = int(input('DO YOU WANT TO DOWNLOAD THIS?- 1/(0 for next)'))
        if nxt == 1:
            link = "https://www.youtube.com"+vid.select('a')[0]['href']
            if song: dwdsong(link)
            else: 
                dwdvideo(link,resorder())
            break
else:
    link=input('Enter link')
    if song: dwdsong(link)
    else: dwdvideo(link,resorder())    

