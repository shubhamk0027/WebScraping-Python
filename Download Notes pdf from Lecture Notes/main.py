from fpdf import FPDF
import requests
from bs4 import BeautifulSoup as bs


base =  "https://lecturenotes.in/"
page =  open("html.html")   # parsing a saved html
soup =  bs(page,'html.parser')
ll   =  soup.select(".pic")

#make image
def make_image(url,name,x):
    image = requests.get(url)
    file = open(name,'wb')
    file.write(image.content)
    file.close()

