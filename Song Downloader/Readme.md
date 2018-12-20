# Instructions to Use
Open the terminal in the directory where the script is present.

Make sure you have python 3 or greater installed. To install python3 type
    <pre>sudo apt-install python3</pre>

## Installing the libraries
Install the following libraries
1. bs4 (beautifulsoup 4-4.6.3 bs4-0.0.1)
    <pre>pip3 install bs4</pre> 
2. youtube-dl (youtube-dl-2018.12.17)
    <pre>pip3 install youtube-dl </pre>
3. emoji (emoji-0.5.1)   
    <pre>pip3 install emoji</pre>

## How to download Songs
1. Run the script as
    <pre>python3 dwdsong.py</pre>
2. Enter the song name say "Blank Space" when asked for song name
3. Select the index of the song you were searching for from the list of the songs show.

Your song will now get downloaded to MySongs folder in the directory where the script was present.

## Customization
By default the songs are downloaded to the "MySongs" folder. 
If no such folder is there it will create one. You can initialize the folderName variable in line 7 in the script to the name of the folder where you want to download the song.
    