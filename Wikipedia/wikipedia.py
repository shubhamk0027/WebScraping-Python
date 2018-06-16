from bs4 import BeautifulSoup as bs
import requests
import re

url="https://en.wikipedia.org/"

word = input('ENTER A TOPIC/WORD\t')
word =word.replace(" ","_").lower()    
url= url+'wiki/'+word
page = requests.get(url)
#print(page.status_code,url)
if page.status_code == 200:
    soup = bs(page.text,'html.parser')
    para = soup.select('p')
    p= para[0].text 
    res=""
    while 1:
        s= p.find('[')
        e= p.find(']')
        if s==e: 
            break
        res = p[:s] + p[e+1:]
        p=res
    if len(res)==0:
        res = p 
    print(p)  

    if "may refer to" or'as in:' in p:
        content = soup.select('.mw-parser-output')[0]
        links =content.select('li')
        #print(type(content))
        for link in links:
            print(link.text)            
else: 
    print("Not a word")




