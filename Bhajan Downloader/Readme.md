What I like most about python is that within a short span of time and with few lines of code we can sovle our day to day tasks very easily.

# About
This a Hindi Bhajan Downloader that downloads all the hindi bhajans in mp3 format from  https://www.ibiblio.org/ram/ in python. 

I created this script when my grandfather asked me to get him all hindi bhajans.
If you are thinking to give your grandfather the same thing you are free to use it/modify it/share it.
But note that since there are many songs(more than 100), and so it will take hours to download all the songs!


# Instructions to Use
Open the terminal in the directory where the script is present.

Make sure you have python 3 or greater installed. To install python3 type
    <pre>sudo apt-install python3</pre>

## Installing the libraries
Install the following libraries
1. bs4 (beautifulsoup 4-4.6.3 bs4-0.0.1)
    <pre>pip3 install bs4</pre> 

## Running the Script
1. Run the script as
    <pre>python3 dwdBhajan.py</pre>
The name of the song, its downloading url and the directory where it has been downloaded will be shown in the terminal.

## Customization
By default all the Bhajans are downloaded in a  "Bhajans" folder in the directory from where the terminal is running. You can initialize the folderName variable in line 11 to the folder name where you want to download.