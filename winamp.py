from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QStyle, QSlider, QFileDialog, QLCDNumber, QTextEdit
from PyQt5 import uic
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
import sys

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
        #set icons
        self.back_btn.setIcon(self.style().standardIcon(QStyle.SP_ArrowBack))
        self.play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.pause_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.stop_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.next_btn.setIcon(self.style().standardIcon(QStyle.SP_ArrowRight))
        self.download_btn.setIcon(self.style().standardIcon(QStyle.SP_ArrowUp))

        #click Buttons
        self.play_btn.clicked.connect(self.play)
        self.pause_btn.clicked.connect(self.pause)
        self.download_btn.clicked.connect(self.download)

        #sliders
        self.time_slider = self.findChild(QSlider, 'time_slider')
        self.volume_slider = self.findChild(QSlider, 'volume_slider')

        #sliders value change
        self.time_slider.sliderMoved.connect(self.set_position)
        self.volume_slider.valueChanged.connect(self.set_volume)

        #LCD
        self.title_lcd = self.findChild(QTextEdit, 'title_lcd')

        #create media Player
        self.Player = QMediaPlayer()

        #create playlist
        self.playlist = QMediaPlaylist()

        #palyer signals
        self.Player.stateChanged.connect(self.audiostate_changed)
        self.Player.positionChanged.connect(self.position_changed)
        self.Player.durationChanged.connect(self.duration_changed)

        self.set_Enabled_button()
        #show The App
        self.show()


    def set_Enabled_button(self):
        self.back_btn.setEnabled(False)
        # self.play_btn.setEnabled(False)
        self.pause_btn.setEnabled(False)

    def play(self):
        self.Player.setPlaylist(self.playlist)
        print(self.playlist)
        self.Player.play()
        self.Player.setVolume(self.volume_slider.value())
        # self.title_lcd.setPlainText(filename.split('/')[-1])

    def pause(self):
        if self.Player.state() == QMediaPlayer.PlayingState:
            self.Player.pause()

    def download(self):
        filenames, _ = QFileDialog.getOpenFileNames(self, 'Play song')
        if len(filenames) != 0:
            for filename in filenames:
                url = QUrl.fromLocalFile(filename)
                self.playlist.addMedia(QMediaContent(url))
            self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

    def set_volume(self, value):
        self.Player.setVolume(value)

    def audiostate_changed(self, state):
        if self.Player.state() == QMediaPlayer.PlayingState:
            pass

    def position_changed(self, position):
        self.time_slider.setValue(position)

    def duration_changed(self, duration):
        self.time_slider.setRange(0, duration)

    def set_position(self, position):
        self.Player.setPosition(position)

    def handle_errors(self):
        self.play_btn.setEnabled(False)
        self.title_lcd.setPlainText('Error' + str(self.Player.errorString()))



app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()