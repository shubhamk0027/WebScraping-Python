# How to Use the Downloader
1. Open the web page displaying the file to be downloaded on www.lecturenotes.in. It will be in following format - 
    https://lecturenotes.in/materials/....
2. Load till the page you want to download on the site by scrolling down to that page number. If you want to download the full pdf, scroll till the last page.

3. Press Ctrl+Shift+ I on the site to open the inspect element section. Using ctrl+f and find "book-container" div element. 

4. Copy all the code (this contains the links of all the things we need to make the pdf) under this div element and paste it to the html.html file under the same div element

5. Simply Run the script as python3 main.py in the terminal

# Note

Make sure you have python3 installed in the terminal and the following libraries are installed- 

    1. fpdf
    2. bs4

if not then, type pip3 fpdf to install fpdf library, same for bs4

