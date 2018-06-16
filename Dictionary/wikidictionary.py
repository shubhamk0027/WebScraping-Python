import requests
from bs4 import BeautifulSoup as bs
import re

url = "https://en.wiktionary.org/wiki/"

def extract(st):
    s= st.find('[')
    e= st.find(']')
    while s!=e:
        st=st[:s]+st[e+1:]
        s= st.find('[')
        e= st.find(']')
    regex= re.compile('[\\][a-z][a-z][0-9]')
    re.sub(regex,"",st)
    st= st.encode('utf-8') #ecoding to ascii
    return str(st)

word = str(input('ENTER WORD:\t')) 
# enter as 'something' not as somehting
url = url + word.lower()
page =  requests.get(url)
if page.status_code ==200:
    soup=bs(page.text,'html.parser')
    heads = soup.select('h3')
    print
    print("Verb:")
    heads[2] = heads[2].next_sibling.next_sibling
    print(extract(heads[2].text))
    print(extract(heads[2].next_sibling.next_sibling.text))
    # when i will print both the lines inone print statemtent decoding of string will not occur
    print()
    print("Entomology:")
    print(heads[0].next_sibling.next_sibling.text)
    print()
    print("Pronounciation:")
    print(heads[1].next_sibling.next_sibling.text)
else:
    print("Invalid word")


