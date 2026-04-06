import os
import sys
import tempfile
import subprocess
from pathlib import Path # find the absolute path of a directory

"""
This script toggles the path from relative to absolute and vice-versa for the files contained inside .m3u
playlist files.

In order to create those you can open a music player like fooyin and 'Create Playlist'.
After adding the files to the playlist save it with the name you want.

In the same directory that you saved the playlist files run the python script to convert the contents.
Normally the software should have saved the ABSOLUTE paths inside the .m3u file.

Why this is useful?
    Because you can save the Music/ folder anywhere you want and inside it save the Playlist/ folder.
    Inside the Playlist/ folder you save the .m3u and python script.
    This will enable you to export your music collection alongside your playlists everywhere*.

    *Tested on Linux and VLC for iOS.
"""
### Defining environment variables
DIRECTORY = Path(__file__).parent.resolve() #working directory where the script resides, absolute path
PLAYLISTDIR = DIRECTORY
RELATIVE = '../'
MUSIC = str(PLAYLISTDIR.parent) + '/' #.parent > returns Music
MUSIC_PATH = PLAYLISTDIR.parent


"""
Changing to MUSIC_PATH in order to use Path attributes like .name.

PurePath.name

    A string representing the final path component, excluding the drive and root, if any:

    PurePosixPath('my/library/setup.py').name
    'setup.py'

    UNC drive names are not considered:

    PureWindowsPath('//some/share/setup.py').name
    'setup.py'
    PureWindowsPath('//some/share').name
    ''
"""
def folder_structure():
    if MUSIC_PATH.name == "Music":
        print(f"Folder structure verified, initializing...")
        return 0

    if not PLAYLISTDIR.is_dir():
        print(f"Error: Script directory '{PLAYLISTDIR}' is not a directory.")
        return 2
    
    if not MUSIC_PATH.is_dir():
        print(f"Error: Parent '{MUSIC}' (Music/) does not exist.")
        return 4

    if MUSIC_PATH.name != "Music":
        print(f"Warning: Parent is '{MUSIC_PATH.name}', expected 'Music/'.")
        choice = input('Do you wish to continue anyway? Type [yes/no]:').strip().lower() #remove spaces and make lowercase
        if(choice != 'yes'):
            return 1
        return 0 # Allow continuing

"""
Method that checks the consistency of the files.
It returns a boolean value.

True -> if the files have the same paths
False -> if the files have mixed paths
It also counts the files that have the paths in two counters. They will be checked at the end. So if there are no relative/absolute paths the files are consistent.
"""
def file_consistency() -> bool:
    relativeCount = 0
    absoluteCount = 0

    for filename in os.listdir(DIRECTORY):

        if filename.endswith('.m3u'):
            filepath = os.path.join(DIRECTORY,filename)

            with open(filepath,'r') as file:
                content = file.read()

                if(RELATIVE in content):
                    relativeCount += 1
                elif(str(MUSIC) in content):
                    absoluteCount += 1
                else:
                    print('NO MATCH!')
                    continue

    print(f"Files with relative paths: {relativeCount}")
    print(f"Files with absolute paths: {absoluteCount}")

    return (relativeCount != absoluteCount and absoluteCount == 0) or (relativeCount != absoluteCount and relativeCount == 0)

"""
Method that converts all absolute paths to relative if the program saw inconsistency (there are mixed paths inside the files)
"""
def inconsistent_toggle():
    converted = 0

    for filename in os.listdir(DIRECTORY):

            if filename.endswith('.m3u'):
                filepath = os.path.join(DIRECTORY,filename)

                with open(filepath,'r') as file:
                    content = file.read()

                    if(str(MUSIC) in content):
                        conversion = content.replace(MUSIC,RELATIVE)
                        print('')
                        print('Absolute path found. Attempting consistency...')
                    else:
                        print('No match, skipping file...')
                        continue #Do not modify


                with tempfile.NamedTemporaryFile(mode='w', delete=False, dir=str(DIRECTORY)) as temp:
                    temp.write(conversion)
                    os.replace(temp.name, filepath)
                converted += 1

    print(f'Consistency achieved: {converted} files processed.')

"""
Main method to toggle/replace the relative path to absolute and vice-versa
"""
def toggle_paths():
    for filename in os.listdir(DIRECTORY): # os.listdir(path='.') Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order, and does not include the special entries '.' and '..'

        #print('Debugging: Entering for cycle')

        if filename.endswith('.m3u'):
            #print('Debugging: Entering IF statement...')
            #print('')
            filepath = os.path.join(DIRECTORY,filename) #join the path and file names, changes / and \ automatically
            #print('Debugging: filepath joined...')
            #print('')

            with open(filepath,'r') as file:
                content = file.read()
                #print('File contents: ')
                #print(content)

                if(RELATIVE in content): #if the string is inside
                    conversion = content.replace(RELATIVE, MUSIC)
                    print('')
                    print('CONVERTING: Relative to MUSIC')
                elif(str(MUSIC) in content):
                    conversion = content.replace(MUSIC,RELATIVE)
                    print('')
                    print('CONVERTING: MUSIC to Relative')
                else:
                    print('NO MATCH!')
                    continue

            with tempfile.NamedTemporaryFile(mode='w', delete=False, dir=str(DIRECTORY)) as temp:
                temp.write(conversion)
                #print('Temporary file: ',temp)
                os.replace(temp.name, filepath) # replace the original file with the temporary one

        print('Deleting temporary files...') # needs to exit the with statement to be done



"""
Main program, only run if directly loaded, NOT if imported
"""
if __name__ == "__main__":

    """TOGGLE # TO DEBUG
    print(f"Debugging SCRIPT folder: {DIRECTORY}")
    print(f"Debugging PLAYLIST folder: {PLAYLISTDIR}")
    print(f"Debugging RELATIVE folder: {RELATIVE}")
    print(f"Debugging MUSIC folder: {MUSIC}")
    """

    print('='*20)
    print("Expected folder structure:\n /home/USER/Music/Playlist\nExpected files:\n /home/USER/Music/SONG\\ NAME.m4a\n    /home/USER/Music/Playlist/ALL\\ SONGS.m3u\n    /home/USER/Music/Playlist/replace-paths.py")
    print('='*20)

    #error printing
    exit_code = folder_structure()
    if exit_code != 0:
        print(f"Exiting with code {exit_code}")
        sys.exit(exit_code)


    print(f"Are you really sure you want to continue with the conversion? (Make a backup of the playlists in case)")
    continue_choice = input('Type [yes/no]:').strip().lower()
    if(continue_choice != 'yes'):
        sys.exit()

    if file_consistency():
        print('The files are consistent, proceeding with normal toggle...')
        toggle_paths()
        print('All done!')

    else:
        print('Executing inconsistent toggle...')
        inconsistent_toggle()
        print('All done!')
        print('Files are now consistent, everything has been changed to RELATIVE path.')
        print('If you wish the ABSOLUTE path just re-run the program.')

