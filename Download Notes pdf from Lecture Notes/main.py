from fpdf import FPDF
import requests
from bs4 import BeautifulSoup as bs

base =  "https://lecturenotes.in/"
page =  open("html.html")   # parsing a saved html
soup =  bs(page,'html.parser')
ll   =  soup.select(".pic")

# pdf details
pdf=FPDF()
w=200
h=300

#make image
def make_image(url,name,x):
    image = requests.get(url)
    file = open(name,'wb')
    file.write(image.content)
    file.close()

#dowloading pages
pageno = 0
for x in ll:
    pageno = pageno + 1
    name = "./pages/"+str(pageno)+".jpg"
    url =  base+ x["style"].split('"')[1]
    print(url)
    make_image(url,name,x)
    pdf.add_page()
    pdf.image(name,0,0,w,h)
    image = requests.get(url)

pdf.output("final.pdf","F")

