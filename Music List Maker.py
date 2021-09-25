#! python3

import os, pyperclip
from tinytag import TinyTag

print('This program will change your clipboard contents!\nMake sure you\'ve got nothing important copied right now ;)')
# move to music directory
print('What folder is your music in? (put a file path here)')
path = input()
try:
    os.chdir(path)
except:
    print('Oops! Looks like there was something wrong with that file path')
    
# open text file
finalFile = open('!songs.txt', 'w')

songsList = os.listdir()
songsNum = len(songsList)

#empty string for clipboard
clipString = ''

for song in range(songsNum):
    try:
        tag = TinyTag.get(songsList[song])
        try:
            finalFile.write(tag.artist + ' - ' + tag.title + '\n')
        # Case: can find tags, but cannot write  -> if non-english characters are in title or artist, add to clipboard instead
        except UnicodeEncodeError:
            clipString += tag.artist + ' - ' + tag.title + '\n'
        # Case: cannot find tags
        except:
            try:
                finalFile.write(songsList[song] + '\n')
            except UnicodeEncodeError:
                # non-english character in title of song, put to clipboard instead
                clipString += songsList[song] + '\n'
    except:
        continue

pyperclip.copy(clipString)
finalFile.close()
print('Done!')
