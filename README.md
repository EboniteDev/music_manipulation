# Music intro:
You can use whatever DAW you want, I'm not a musician.

What I can suggest however is:
- FFmpeg (obviously)
	it is a command line utility suite of programs and libraries for manipulating audio and video streams, it is incorporated/used by basically all software that has to do with audio. It comes with ffprobe to see the metadatas of a file and ffplay, a really simple media player.
	<p>

- Audacious
	a lightweight music player.
	<p>

- VLC
	a well equipped media (audio+video) player.
	<p>
-  Gapless (flathub)
	A simple and user friendly music player. It has a minimal UI akin to Spotify and has the ability to export the images of the songs, allegedly, without loss of quality and with the same name of the song file.
	<p>
- fooyin
	a reasonable music player with a lot of straightforward User Interface customization compared to other players. It also has the possibility to edit lyrics. And export images.

![View of a custom layout](https://raw.githubusercontent.com/EboniteDev/Images/refs/heads/main/fooyin_configuration_example.png?token=GHSAT0AAAAAADZX74NGYI2SS7L2X2MC54K42OT5PQA)
![View of simple lyrics](https://raw.githubusercontent.com/EboniteDev/Images/refs/heads/main/fooyin_simple_lyrics_example.png?token=GHSAT0AAAAAADZX74NHU4APGD5IK6H5VHWC2OT5PUQ)
	<p>
- Kid3
	a multiplatform KDE software for tagging your music, adding simple lyrics and attaching images.
	<p>
- Aegisub
	a not so straightforward, but powerful subtitle generator with timestamps, styles and more. You can use it to do Karaoke-style lyrics (like ニコカラ videos)
	<p>
- Audacity
	to export audios of your works in different formats and manipulate them.
	<p>
- Easy Effects
	a program that adds effect to your mic through a Digital Microphone, like noise reduction etc...
	<p>

Be sure to have a reasonable folder structure.
For my works/programs/etc... your folder structure should look like this:
~~~
Master directory (UNIX reference):
    /home/USERNAME/Music

    Inside the master directories there should be these directories:
		
		/home/USERNAME/Music/'Artist Icons'         # For storing your icons etc...
        /home/USERNAME/Music/'In Progress'          # For unfinished works
        /home/USERNAME/Music/'Lyrics'               # More complex lyrics for your music which can be .ass files for Aegisub.
        /home/USERNAME/Music/'Playlists'            # To store playlist files (mainly .m3u) etc...
        /home/USERNAME/Music/'Scripts and Commands' # To store useful commands
        /home/USERNAME/Music/'Song Specific Cover'  # For storing individual covers of songs
        /home/USERNAME/Music/'Text Subtitles'       # Lyrics or subtitles for the songs in .txt format
             
~~~

---
## ReplayGain - normalizing the volume of songs
> [!Question]
>> Why should I do this?

> [!Answer]
With ReplayGain you can listen to your library or songs without bleeding your ears because the previous song was too quiet.

### How should I do this?

> I found useful to install on Linux systems this package "rsgain", there are other programs obviously, but I only found this to be reliable on different software like: VLC (desktop and iOS), Audacious, qmmp, fooyin.
> 
> You can find my command in this repository but you should change it accordingly because it SHOULD only work with .ogg files and the target loudness is -6dB.

### Are there any drawbacks?

> Personally I did not find any but if your song as many variation of loudness it could interfere with the volumes, in the sense that you might ear something funny, like audio corruption in a nutshell.

## Replace relative/absolute paths
> [!Question]
>> Why should I do this?

> [!Answer]
Because you can export, move the Music folder around or even import your song playlists collection to VLC for iOS.

You can run the script provided on Github under EboniteDev or do it manually.

### Manually
For every file:
You can open a text editor and "Find and Replace" all instances of either ../ to /home/USER/*etc*.

Or using vim/neovim with these commands:
<pre>
	To make relative paths:
		:%s/\/home\/USER\/Music\//..\//g
		
	To make absolute paths:
		:%s/..\//\/home\/USER\/Music\//g
</pre>
