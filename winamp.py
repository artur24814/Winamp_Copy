from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QStyle, QSlider, QFileDialog, QLCDNumber, QTextEdit
from PyQt5 import uic
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
import sys
from utils import get_html, convert_duration_to_show

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #Load the ui file
        uic.loadUi('winamp_player.ui', self)
        self.setWindowIcon(QIcon('winamp-icon.png'))

        #Define widgets
        #Buttons
        self.back_btn = self.findChild(QPushButton, "back_btn")
        self.play_btn = self.findChild(QPushButton, "play_btn")
        self.pause_btn = self.findChild(QPushButton, "pause_btn")
        self.stop_btn = self.findChild(QPushButton, "stop_btn")
        self.next_btn = self.findChild(QPushButton, "next_btn")
        self.download_btn = self.findChild(QPushButton, "download_btn")
        self.shuffle_btn = self.findChild(QPushButton, 'shuffle_btn')
        self.loop_btn = self.findChild(QPushButton, 'loop_btn')
        #set icons
        self.back_btn.setIcon(self.style().standardIcon(QStyle.SP_ArrowBack))
        self.play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.pause_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.stop_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.next_btn.setIcon(self.style().standardIcon(QStyle.SP_ArrowRight))
        self.download_btn.setIcon(self.style().standardIcon(QStyle.SP_ArrowUp))

        #click Buttons
        self.back_btn.clicked.connect(self.back)
        self.play_btn.clicked.connect(self.play)
        self.pause_btn.clicked.connect(self.pause)
        self.stop_btn.clicked.connect(self.stop)
        self.next_btn.clicked.connect(self.next)
        self.download_btn.clicked.connect(self.download)
        self.shuffle_btn.clicked.connect(self.shuffle)
        self.loop_btn.clicked.connect(self.loop)

        #sliders
        self.time_slider = self.findChild(QSlider, 'time_slider')
        self.volume_slider = self.findChild(QSlider, 'volume_slider')

        #sliders value change
        self.time_slider.sliderMoved.connect(self.set_position)
        self.volume_slider.valueChanged.connect(self.set_volume)

        #LCD
        self.time_lcd =self.findChild(QTextEdit, 'time_lcd')
        self.title_lcd = self.findChild(QTextEdit, 'title_lcd')

        #create media Player
        self.Player = QMediaPlayer()

        #create playlist
        self.playlist = QMediaPlaylist()

        #palyer signals
        self.Player.stateChanged.connect(self.audiostate_changed)
        self.Player.positionChanged.connect(self.position_changed)
        self.Player.durationChanged.connect(self.duration_changed)

        #current song
        self.playlist.currentMediaChanged.connect(self.songChanged)

        #set value for loop plaing
        self.loop_plaing = False

        self.set_Enabled_button()
        #show The App
        self.show()

    def set_Enabled_button(self):
        #when init player
        if self.playlist.isEmpty():
            self.back_btn.setEnabled(False)
            self.play_btn.setEnabled(False)
            self.pause_btn.setEnabled(False)
            self.stop_btn.setEnabled(False)
            self.next_btn.setEnabled(False)
        #when we have some music in playlist
        else:
            self.back_btn.setEnabled(True)
            self.play_btn.setEnabled(True)
            self.pause_btn.setEnabled(True)
            self.stop_btn.setEnabled(True)
            self.next_btn.setEnabled(True)

    #to previous song
    def back(self):
        self.playlist.previous()

    #play music
    def play(self):
        #if already play
        if self.Player.state() == QMediaPlayer.PlayingState:
            self.Player.pause()
        else:
            self.Player.play()
            self.Player.setVolume(self.volume_slider.value())

    #pause music
    def pause(self):
        if self.Player.state() == QMediaPlayer.PlayingState:
            self.Player.pause()
        else:
            self.play()

    #stop music
    def stop(self):
        if self.Player.state() == QMediaPlayer.PlayingState:
            self.Player.stop()

    #next song
    def next(self):
        self.playlist.next()

    #download list of music
    def download(self):
        #open dialog window
        filenames, _ = QFileDialog.getOpenFileNames(self, 'Play song')
        if len(filenames) != 0:
            for filename in filenames:
                url = QUrl.fromLocalFile(filename)
                #add song to playlist
                self.playlist.addMedia(QMediaContent(url))
            #add playlist to player
            self.Player.setPlaylist(self.playlist)
            #set button to enabled
            self.set_Enabled_button()

    def set_volume(self, value):
        self.Player.setVolume(value)

    def audiostate_changed(self, state):
        if self.Player.state() == QMediaPlayer.PlayingState:
            pass

    #update slider position
    def position_changed(self, position):
        self.time_slider.setValue(position)
        duration_list = convert_duration_to_show(position)
        time = duration_list[0] + ':' + duration_list[1]
        self.time_lcd.setHtml(get_html(time))

    #set slider range
    def duration_changed(self, duration):
        self.time_slider.setRange(0, duration)
        #add duration to song title
        duration_list = convert_duration_to_show(duration)
        text = self.title_lcd.toPlainText() + ' (' + duration_list[0] + ':' + duration_list[1] + ')'
        self.title_lcd.setPlainText(text)

    #set position played song
    def set_position(self, position):
        self.Player.setPosition(position)

    #show title played of song in text input
    def songChanged(self, media):
        if not media.isNull():
            url = media.canonicalUrl()
            text = str(self.playlist.currentIndex() + 1 ) + '.' + url.fileName().split('/')[-1]
            self.title_lcd.setPlainText(text)

    def shuffle(self):
        self.playlist.shuffle()

    def loop(self):
        #if mode plyilist = sequential
        if self.loop_plaing is False:
            self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
            self.loop_btn.setStyleSheet(""" background-color : rgb(53, 159, 159);
                                            border-top: 4px double rgb(253, 253, 253);
                                            border-right: 4px double #DFDBDD;
                                            border-bottom: 4px double #BCB8BA;
                                            border-left: 4px double #EFEAEC;""")
            self.loop_plaing = True
        #if already play in loop
        else:
            self.playlist.setPlaybackMode(QMediaPlaylist.Sequential)
            self.loop_btn.setStyleSheet("""background-color: rgb(221, 221, 221);
                                            border-top: 4px double rgb(253, 253, 253);
                                            border-right: 4px double #DFDBDD;
                                            border-bottom: 4px double #BCB8BA;
                                            border-left: 4px double #EFEAEC;""")
            self.loop_plaing = False

    #show error in TextInput
    def handle_errors(self):
        self.play_btn.setEnabled(False)
        self.title_lcd.setPlainText('Error' + str(self.Player.errorString()))

    def __del__(self):
        if hasattr(self, "playlist"):
            del self.playlist



app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()