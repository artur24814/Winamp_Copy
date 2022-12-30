# Winamp_Copy

<center><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Python_and_Qt.svg/1200px-Python_and_Qt.svg.png' width=300 height=300></center>

## Contents
 * <a href="#info"><strong>Info</strong></a><p>Information about the resources used in this project</p>
 * <a href="#winamp"><strong>WINAMP_copy</strong></a><p>A copy of the ancient and legendary Winamp, written using the PyQt5 python framework</p>
 * <a href="#clone_project"><strong>Clone and Run Project</strong></a><p>how run projects in your computer or in an telephone</p>

<hr>

<details><summary id="info" style="font-size: 30px;"> INFO</summary>
<h4>Information about the additional library, external Api used in this project and general information</h4>

<strong>PyQt5</strong> PyQt5 is a comprehensive set of Python bindings for Qt v5.

<strong>pyqt5-tools</strong> The PyQt5 wheels do not provide tools such as Qt Designer that were included in the old binary installers. This package aims to provide those in a separate package which is useful for developers while the official PyQt5 wheels stay focused on fulfilling the dependencies of PyQt5 applications.

</details>

<hr>
<center><h1 id="winamp"> WINAMP copy <span style='font-size:80px;'><img src="https://img.icons8.com/color/96/null/winamp.png"/></span></h1></center>

#### Some info about Winamp:

Winamp is a media player for Microsoft Windows originally developed by Justin Frankel and Dmitry Boldyrev by their company Nullsoft, which they later sold to AOL in 1999 for $80 million. It was then acquired by Radionomy in 2014. Since version 2 it has been sold as freemium and supports extensibility with plug-ins and skins, and features music visualization, playlist and a media library, supported by a large online community.

Version 1 of Winamp was released in 1997, and quickly grew popular with over 3 million downloads, paralleling the developing trend of MP3 (music) file sharing. Winamp 2.0 was released on September 8, 1998. The 2.x versions were widely used and made Winamp one of the most downloaded Windows applications.[11] By 2000, Winamp had over 25 million registered users[12] and by 2001 it had 60 million users.[13] A poor reception to the 2002 rewrite, Winamp3, was followed by the release of Winamp 5 in 2003, and a later release of version 5.5 in 2007. A now-discontinued version for Android was also released, along with early counterparts for MS-DOS and Macintosh. 

### My Winamp

My copy of Winamp have most functionality from original version.

In a start if playlist is empty all buttons are not enabled, in this case our player doesn't useful.
<center><img alt="player1" src="https://user-images.githubusercontent.com/97242088/210106051-17e6ff27-8988-44a1-92ba-56689c57b4ef.png"></center>

To start work with player click button 'arrow up'. <br>You will get pop up FileDialog choose directory with your songs to play and press Ctrl and choose songs to play, click button 'Open' and now the fun begins.<br>The playlist window will appear too.
<center><img alt='add_files' src='https://user-images.githubusercontent.com/97242088/210106049-7531e769-bb56-4ab8-8e4d-320f5f3893f1.png'></center>

Now all buttons are available<br>
And you have at your disposal: 

 * <img src="https://img.icons8.com/fluency-systems-filled/48/null/chevron-left--v2.png" height='20' width='20'/> - previous song
 * <img src="https://img.icons8.com/ios-glyphs/30/null/play--v1.png" height='20' width='20'/> - play song
 * <img src="https://img.icons8.com/ios-glyphs/30/null/pause--v1.png" height='20' width='20'/> - pause
 * <img src="https://img.icons8.com/ios-filled/50/null/stop.png" height='20' width='20'/> - stop(The next time when you push the button  play, our song will play from the beginning)
 * <img src="https://img.icons8.com/external-others-inmotus-design/67/null/external-Right-basic-web-ui-elements-others-inmotus-design-2.png" height='20' width='20'/> - next song

In the left LCD window, you can see the time in the right - song title which play on this moment with time range of particular song.

Under the LCD window with time we have a time slider, the movement of which depends on the time of the song playback. You can move this slider and set the playing time of the song.

And of course you can set the volume (slider on the right side of the LCD window with time).

You can choose the playback mode. If you listen your playlist few times you already know which song follows which, to feel less predictable push the button 'Shuffle', content of your playlist will be randomly shuffle (all indexes will change).<br>
The button <img src="https://img.icons8.com/pastel-glyph/64/null/loop-arrow.png" height='20' width='20'/> It will put your playlist in loop mode (when the playlist ends, the first song will play).

<center><img alt="song" src="https://user-images.githubusercontent.com/97242088/210106053-f152ab86-bd4a-4d5f-80f4-23ad4c7c07a3.png"></center>

If you want to play a specific song, just click on that song from list 'Winamp Playlist'.

If you look at the bottom right corner you will see the same buttons as in our main window, they have the same functionality. That's because you can close the main window and only use the playlist window if you want. Or you can close the playlist window and only use the main window, they can exist on their own.

<center><img alt="song2" src="https://user-images.githubusercontent.com/97242088/210106054-1f8b6b43-2df8-43e6-a76c-c0f1354c9248.png"></center>

<center><h2 id="clone_project">Clone and Run a Project</h2></center>


To start, we need to clone my project from Github:-
<p>Above the list of files, click Code.</p>
<img src="https://docs.github.com/assets/cb-20363/images/help/repository/code-button.png">

Copy the URL for the repository.
<ul>
<li>To clone the repository using HTTPS, under "HTTPS", click</li>
<li>To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click</li>
<li>To clone a repository using GitHub CLI, click GitHub CLI, then click</li>
</ul>
<img src="https://docs.github.com/assets/cb-33207/images/help/repository/https-url-clone-cli.png">

Open Terminal.

Change the current working directory to the location where you want the cloned directory.

Type git clone, and then paste the URL you copied earlier.

`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

Press Enter to create your local clone.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...<br>
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Before diving let’s look at the things we are required to install in our system.

To run App prefer to use the Virtual Environment

`pip install virtualenv`

Making and Activating the Virtual Environment:-

`virtualenv “name as you like”`

`source “name as you like”/bin/activate`

Install the project dependencies:

`pip install -r requirements.txt`

to run

`python winamp.py`



Have fun
<p style="font-size:100px">&#129409;</p>

