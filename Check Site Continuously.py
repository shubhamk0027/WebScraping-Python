import time
import requests
from bs4 import BeautifulSoup as bs
import re

url = "https://cumsdtu.in/registration_student/login/login.jsp"

print('Real Time Monitoring ON')
print('Montoring in Progress......')

while 1:
    page =  requests.get(url)
    if page.status_code ==200:
        print('Site is On now!!! You can register!')
    else:
        print('Site is still down :(')
    print('Waiting for 60 secs...')
    time.sleep(60)


