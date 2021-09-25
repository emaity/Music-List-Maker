# Music-List-Maker
Generates a text file with music/file names on each line

Input an absolute file path to the folder containing music, and this code will create a text file within the same folder, named "!songs.txt" with the music names on each line.

Music files with non-traditional english characters will be added to the clipboard instead, so the user can paste those songs into the text file themselves.

^ That's probably not the best solution, but it's the one I thought of.


# Behavior
If the file has built-in meta data, then the program lists the music with the format: ARTIST - TITLE

If the file does not have either a title or artist specified, then the program copies the file name into the text file as is.

If the program encounters a UnicodeEncodeError, as is the case with non-english characters, then the file name is saved onto the clipboard instead.


# Executable Folder
This folder contains the windows application version of the python file, made using py2exe.

Running the .exe in this folder allows it to run without needing python installed on the user's computer.
