from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QStyle, QSlider, QFileDialog, QLCDNumber, QTextEdit, QListWidget
from PyQt5 import uic
import sys

class PlaylistUI(QMainWindow, object):
    def __init__(self):
        super(PlaylistUI, self).__init__()

        # Load the ui file
        uic.loadUi('winamp_playlist.ui', self)

        # Define widgets
        # Buttons
        self.pl_back_btn = self.findChild(QPushButton, "pl_back_btn")
        self.pl_play_btn = self.findChild(QPushButton, "pl_play_btn")
        self.pl_pause_btn = self.findChild(QPushButton, "pl_pause_btn")
        self.pl_stop_btn = self.findChild(QPushButton, "pl_stop_btn")
        self.pl_next_btn = self.findChild(QPushButton, "pl_next_btn")
        self.pl_download_btn = self.findChild(QPushButton, "pl_download_btn")

        #playlist list
        self.list_songs = self.findChild(QListWidget, 'list_songs')

        #textinputs
        self.time_song_text = self.findChild(QTextEdit, 'time_song_text')


        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    UIWindow = PlaylistUI()
    app.exec_()