import io
import sys
import os
import time
from PyQt5 import uic, QtGui
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *
from dbmanager import *

temp = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Audioplayer</class>
 <widget class="QMainWindow" name="Audioplayer">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>394</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="0" column="0">
     <layout class="QVBoxLayout" name="verticalLayout_3">
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout_4">
        <item>
         <layout class="QVBoxLayout" name="verticalLayout_2">
          <property name="sizeConstraint">
           <enum>QLayout::SetFixedSize</enum>
          </property>
          <item>
           <widget class="QLabel" name="label">
            <property name="font">
             <font>
              <family>Miriam</family>
              <pointsize>20</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Song name:</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLabel" name="song_name">
            <property name="enabled">
             <bool>true</bool>
            </property>
            <property name="minimumSize">
             <size>
              <width>130</width>
              <height>50</height>
             </size>
            </property>
            <property name="maximumSize">
             <size>
              <width>130</width>
              <height>50</height>
             </size>
            </property>
            <property name="text">
             <string/>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="Add_to_playlist">
            <property name="font">
             <font>
              <family>Miriam CLM</family>
              <pointsize>10</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Add to playlist</string>
            </property>
            <property name="icon">
             <iconset>
              <normaloff>../../Downloads/playlist.png</normaloff>../../Downloads/playlist.png</iconset>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="Add_favourite">
            <property name="font">
             <font>
              <family>Miriam CLM</family>
              <pointsize>10</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Add to Favourites</string>
            </property>
            <property name="icon">
             <iconset>
              <normaloff>../../Downloads/love.png</normaloff>../../Downloads/love.png</iconset>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QDial" name="volume"/>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QVBoxLayout" name="verticalLayout">
          <item>
           <layout class="QHBoxLayout" name="horizontalLayout_3">
            <item>
             <widget class="QLabel" name="list_name">
              <property name="font">
               <font>
                <family>Miriam</family>
                <pointsize>10</pointsize>
               </font>
              </property>
              <property name="text">
               <string>Song List</string>
              </property>
             </widget>
            </item>
            <item>
             <widget class="QPushButton" name="Add_songs">
              <property name="text">
               <string/>
              </property>
              <property name="icon">
               <iconset>
                <normaloff>../../Downloads/add-to-playlist.png</normaloff>../../Downloads/add-to-playlist.png</iconset>
              </property>
              <property name="iconSize">
               <size>
                <width>25</width>
                <height>25</height>
               </size>
              </property>
              <property name="flat">
               <bool>true</bool>
              </property>
             </widget>
            </item>
            <item>
             <widget class="QPushButton" name="delete_song">
              <property name="text">
               <string/>
              </property>
              <property name="icon">
               <iconset>
                <normaloff>../../Downloads/bin.png</normaloff>../../Downloads/bin.png</iconset>
              </property>
              <property name="iconSize">
               <size>
                <width>25</width>
                <height>25</height>
               </size>
              </property>
              <property name="flat">
               <bool>true</bool>
              </property>
             </widget>
            </item>
            <item>
             <widget class="QPushButton" name="Delete_songs">
              <property name="text">
               <string/>
              </property>
              <property name="icon">
               <iconset>
                <normaloff>../../Downloads/icons8-delete-all-96.png</normaloff>../../Downloads/icons8-delete-all-96.png</iconset>
              </property>
              <property name="iconSize">
               <size>
                <width>35</width>
                <height>35</height>
               </size>
              </property>
              <property name="flat">
               <bool>true</bool>
              </property>
             </widget>
            </item>
           </layout>
          </item>
          <item>
           <widget class="QListWidget" name="song_list"/>
          </item>
          <item>
           <layout class="QHBoxLayout" name="horizontalLayout_2">
            <item>
             <widget class="QPushButton" name="all_songs">
              <property name="text">
               <string>Song List</string>
              </property>
              <property name="flat">
               <bool>false</bool>
              </property>
             </widget>
            </item>
            <item>
             <layout class="QVBoxLayout" name="verticalLayout_4">
              <item>
               <widget class="QPushButton" name="playlists">
                <property name="text">
                 <string>Playlists</string>
                </property>
               </widget>
              </item>
              <item>
               <layout class="QHBoxLayout" name="horizontalLayout_5">
                <item>
                 <widget class="QPushButton" name="open_btn">
                  <property name="text">
                   <string>Open</string>
                  </property>
                  <property name="icon">
                   <iconset>
                    <normaloff>../../Downloads/log-in.png</normaloff>../../Downloads/log-in.png</iconset>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="new_btn">
                  <property name="text">
                   <string>New</string>
                  </property>
                  <property name="icon">
                   <iconset>
                    <normaloff>../../Downloads/add.png</normaloff>../../Downloads/add.png</iconset>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="delete_btn">
                  <property name="text">
                   <string>Delete</string>
                  </property>
                  <property name="icon">
                   <iconset>
                    <normaloff>../../Downloads/bin.png</normaloff>../../Downloads/bin.png</iconset>
                  </property>
                 </widget>
                </item>
               </layout>
              </item>
             </layout>
            </item>
           </layout>
          </item>
         </layout>
        </item>
       </layout>
      </item>
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout">
        <item>
         <widget class="QPushButton" name="previous">
          <property name="text">
           <string/>
          </property>
          <property name="icon">
           <iconset>
            <normaloff>../../Downloads/rewind-button.png</normaloff>../../Downloads/rewind-button.png</iconset>
          </property>
          <property name="flat">
           <bool>true</bool>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="play">
          <property name="text">
           <string/>
          </property>
          <property name="icon">
           <iconset>
            <normaloff>../../Downloads/play-button-arrowhead.png</normaloff>../../Downloads/play-button-arrowhead.png</iconset>
          </property>
          <property name="iconSize">
           <size>
            <width>16</width>
            <height>16</height>
           </size>
          </property>
          <property name="flat">
           <bool>true</bool>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="stop">
          <property name="text">
           <string/>
          </property>
          <property name="icon">
           <iconset>
            <normaloff>../../Downloads/pause.png</normaloff>../../Downloads/pause.png</iconset>
          </property>
          <property name="flat">
           <bool>true</bool>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="next">
          <property name="text">
           <string/>
          </property>
          <property name="icon">
           <iconset>
            <normaloff>../../Downloads/forward-button.png</normaloff>../../Downloads/forward-button.png</iconset>
          </property>
          <property name="flat">
           <bool>true</bool>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QSlider" name="music_slider">
          <property name="orientation">
           <enum>Qt::Horizontal</enum>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLabel" name="time">
          <property name="text">
           <string>00:00/00:00</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

'''

temp1 = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Audioplayer</class>
 <widget class="QMainWindow" name="Audioplayer">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>363</width>
    <height>245</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout_2">
    <item row="0" column="0">
     <layout class="QGridLayout" name="gridLayout">
      <item row="1" column="0">
       <widget class="QListWidget" name="Playlist_names"/>
      </item>
      <item row="2" column="0">
       <layout class="QHBoxLayout" name="horizontalLayout_2">
        <item>
         <widget class="QPushButton" name="Add_song_to_playlist">
          <property name="text">
           <string>Add song to playlist</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="close_btn">
          <property name="text">
           <string>Close</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item row="0" column="0">
       <widget class="QLabel" name="label">
        <property name="font">
         <font>
          <family>Miriam</family>
          <pointsize>17</pointsize>
         </font>
        </property>
        <property name="text">
         <string>Playlists</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

'''


class Audioplayer(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(temp)
        uic.loadUi(f, self)
        self.setWindowTitle('Audioplayer')
        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.player = QMediaPlayer()

        self.playlist_or_all_songs_tab = 0

        self.initial_volume = 20
        self.player.setVolume(self.initial_volume)
        self.volume.setValue(self.initial_volume)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.move_slider)

        self.player.mediaStatusChanged.connect(self.song_finished)
        self.music_slider.sliderMoved[int].connect(
            lambda: self.player.setPosition(self.music_slider.value())
        )
        self.Add_songs.clicked.connect(self.add_songs)
        self.Add_songs.setIcon(QtGui.QIcon('pngs/add-to-playlist.png'))
        self.play.clicked.connect(self.play_song)
        self.play.setIcon(QtGui.QIcon('pngs/play-button-arrowhead.png'))
        self.stop.clicked.connect(self.stop_song)
        self.stop.setIcon(QtGui.QIcon('pngs/pause.png'))
        self.next.clicked.connect(self.next_song)
        self.next.setIcon(QtGui.QIcon('pngs/forward-button.png'))
        self.previous.clicked.connect(self.previous_song)
        self.previous.setIcon(QtGui.QIcon('pngs/rewind-button.png'))
        self.Delete_songs.clicked.connect(self.remove_all_songs)
        self.Delete_songs.setIcon(QtGui.QIcon('pngs/icons8-delete-all-96.png'))
        self.delete_song.clicked.connect(self.remove_song)
        self.delete_song.setIcon(QtGui.QIcon('pngs/trash.png'))
        self.all_songs.clicked.connect(self.switch_all_songs_tab)
        self.playlists.clicked.connect(self.switch_playlists_tab)
        self.open_btn.clicked.connect(self.open_playlist)
        self.open_btn.setIcon(QtGui.QIcon('pngs/log-in.png'))
        self.new_btn.clicked.connect(self.create_playlist)
        self.new_btn.setIcon(QtGui.QIcon('pngs/add.png'))
        self.delete_btn.clicked.connect(self.delete_playlist)
        self.delete_btn.setIcon(QtGui.QIcon('pngs/trash.png'))

        self.volume.valueChanged.connect(lambda: self.volume_changed())
        self.Add_favourite.clicked.connect(self.add_song_to_favourites)
        self.Add_favourite.setIcon(QtGui.QIcon('pngs/love.png'))
        self.Add_to_playlist.clicked.connect(self.add_song_to_playlist)
        self.Add_to_playlist.setIcon(QtGui.QIcon('pngs/playlist.png'))

        self.tab(self.playlist_or_all_songs_tab)

    # функция которая выводит список песен/плейлистов.
    def tab(self, n):
        self.song_list.clear()
        if n == 0:
            for file in DBManager().tab_conclusion('song_list'):
                self.song_list.addItem(
                    QListWidgetItem(
                        os.path.basename(file[0])
                    )
                )
            self.Add_songs.setEnabled(True)
            self.Add_favourite.setEnabled(True)
            self.Add_to_playlist.setEnabled(True)
            self.open_btn.setEnabled(False)
            self.new_btn.setEnabled(False)
            self.delete_btn.setEnabled(False)
            self.list_name.setText('Song List')
        elif n == 2:
            for file in DBManager().tab_conclusion(self.list_name.text()):
                self.song_list.addItem(
                    QListWidgetItem(
                        os.path.basename(file[0])
                    )
                )
        else:
            for file in DBManager().tab_conclusion('playlists'):
                self.song_list.addItem(
                    QListWidgetItem(
                        file[0]
                    )
                )
            self.Add_songs.setEnabled(True)
            self.Add_favourite.setEnabled(False)
            self.Add_to_playlist.setEnabled(False)
            self.open_btn.setEnabled(True)
            self.new_btn.setEnabled(True)
            self.delete_btn.setEnabled(True)
            self.list_name.setText('Playlists')

    # функцияя для открытия и добавления файлов.
    def add_songs(self):
        if self.list_name.text() != 'Playlists':
            files, _ = QFileDialog.getOpenFileNames(
                self, caption='Add Songs to the app', directory=':\\',
                filter='Supported Files (*.mp3;*.mpeg;*.ogg;*.m4a;*.MP3;*.wma;*.acc;*.amr)'
            )
            if files:
                self.song_list.clear()
                for file in files:
                    DBManager().add_files('song_list', file)

            for file in DBManager().tab_conclusion('song_list'):
                self.song_list.addItem(
                    QListWidgetItem(
                        os.path.basename(file[0])
                    )
                )

    # функция для добавления трека в "избранные".
    def add_song_to_favourites(self):
        if self.song_list:
            current_selection = self.song_list.currentRow()
            current_song = DBManager().tab_conclusion('song_list')[current_selection][0]
            DBManager().add_files('favourites', current_song)

    # функция для добавления трека в плейлист. открывает окно выбора плейлиста.
    def add_song_to_playlist(self):
        if self.song_list:
            global current
            current_selection = self.song_list.currentRow()
            current = DBManager().tab_conclusion('song_list')[current_selection][0]
            self.playlists_window = Plailists()
            self.playlists_window.show()

    # функция для удаления выбранной песни
    def remove_song(self):
        if self.list_name.text() != 'Playlists' and self.song_list:
            current_selection = self.song_list.currentRow()
            if self.playlist_or_all_songs_tab == 0:
                current_song = DBManager().tab_conclusion('song_list')[current_selection][0]
                DBManager().delete_one_file('song_list', current_song)
                self.tab(0)
            else:
                current_song = DBManager().tab_conclusion(self.list_name.text())[current_selection][0]
                DBManager().delete_one_file(self.list_name.text(), current_song)
                self.tab(2)

    # функция для удаления сразу всех песен
    def remove_all_songs(self):
        if self.playlist_or_all_songs_tab == 0:
            self.song_list.clear()
            DBManager().delete_all_files('song_list')
        elif self.list_name.text() != 'Playlists':
            self.song_list.clear()
            DBManager().delete_all_files(self.list_name.text())

    # функция для получени выбранной песни
    def song_select(self, current_selection):
        if self.playlist_or_all_songs_tab == 0:
            current_song = DBManager().tab_conclusion('song_list')[current_selection][0]
        else:
            current_song = DBManager().tab_conclusion(self.list_name.text())[current_selection][0]

        song_url = QMediaContent(QUrl.fromLocalFile(current_song))
        self.player.setMedia(song_url)
        self.player.play()

        self.song_name.setText(f'{os.path.basename(current_song)}')

    # функция для запуска воспроизведения
    def play_song(self):
        if self.list_name.text() != 'Playlists' and self.song_list:
            current_selection = self.song_list.currentRow()
            self.song_select(current_selection)

    # функция для остановки воспроизведения
    def stop_song(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    # функция для перехода к следующему треку
    def next_song(self):
        if self.list_name.text() != 'Playlists' and self.song_list:
            current_selection = self.song_list.currentRow() + 1
            if current_selection == len(self.song_list):
                current_selection = 0
                self.song_list.setCurrentRow(current_selection)
            else:
                self.song_list.setCurrentRow(current_selection)

            self.song_select(current_selection)

    # функция для перехода к предыдущему треку
    def previous_song(self):
        if self.list_name.text() != 'Playlists' and self.song_list:
            current_selection = self.song_list.currentRow() - 1
            if current_selection == -1:
                current_selection = len(self.song_list) - 1
                self.song_list.setCurrentRow(current_selection)
            else:
                self.song_list.setCurrentRow(current_selection)

            self.song_select(current_selection)

    # функция включающая воспроизведение следующего трека при окончании первого
    def song_finished(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.next_song()

    # функция для изменения громкости
    def volume_changed(self):
        self.initial_volume = self.volume.value()
        self.player.setVolume(self.initial_volume)

    # функция для перемотки аудиозаписи через слайдер
    def move_slider(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.music_slider.setMinimum(0)
            self.music_slider.setMaximum(self.player.duration())
            slider_position = self.player.position()
            self.music_slider.setValue(slider_position)

            current_time = time.strftime("%M:%S", time.localtime(self.player.position() / 1000))
            song_duration = time.strftime("%M:%S", time.localtime(self.player.duration() / 1000))
            self.time.setText(f"{current_time} / {song_duration}")

    # функция открывающая диалоговое окно для создания плейлиста
    def create_playlist(self):
        text, ok = QInputDialog.getText(self, 'Create Playlist', 'Playlist name:')
        if ok:
            try:
                DBManager().create_table(str(text))
                DBManager().add_files('playlists', str(text))
                self.song_list.clear()
                for file in DBManager().tab_conclusion('playlists'):
                    self.song_list.addItem(QListWidgetItem(file[0]))
                self.delete_btn.setEnabled(True)
                self.Add_songs.setEnabled(True)
                self.list_name.setText('Playlists')
            except:
                pass

    # функция открывающая выбранный плейлист
    def open_playlist(self):
        current_selection = self.song_list.currentRow()
        current_playlist = DBManager().tab_conclusion('playlists')[current_selection][0]
        self.song_list.clear()
        for file in DBManager().tab_conclusion(current_playlist):
            self.song_list.addItem(
                QListWidgetItem(
                    os.path.basename(file[0])
                )
            )
        self.list_name.setText(current_playlist)
        self.delete_btn.setEnabled(False)
        self.Add_songs.setEnabled(False)

    # функция удаляющая выбранный плейлист
    def delete_playlist(self):
        current_selection = self.song_list.currentRow()
        current_playlist = DBManager().tab_conclusion('playlists')[current_selection][0]
        if current_playlist != 'favourites':
            DBManager().delete_tabel(current_playlist)
            DBManager().delete_one_file('playlists', current_playlist)
            self.song_list.clear()
            for file in DBManager().tab_conclusion('playlists'):
                self.song_list.addItem(
                    QListWidgetItem(
                        file[0]
                    )
                )

    # функция для вывода на экран списка плейлистов
    def switch_playlists_tab(self):
        self.playlist_or_all_songs_tab = 1
        self.tab(self.playlist_or_all_songs_tab)

    # функция для вывода на экран списка всех треков
    def switch_all_songs_tab(self):
        self.playlist_or_all_songs_tab = 0
        self.tab(self.playlist_or_all_songs_tab)


class Plailists(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(temp1)
        uic.loadUi(f, self)
        self.setWindowTitle('Audioplayer')
        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.Add_song_to_playlist.clicked.connect(self.add_song)
        self.close_btn.clicked.connect(self.close)

        for file in DBManager().tab_conclusion('playlists'):
            self.Playlist_names.addItem(QListWidgetItem(file[0]))

    # закрывает окно
    def close(self):
        self.hide()

    # добавляет выбранную песню в выбранный плейлист
    def add_song(self):
        global current
        current_selection = self.Playlist_names.currentRow()
        current_playlist = DBManager().tab_conclusion('playlists')[current_selection][0]
        DBManager().add_files(current_playlist, current)
        self.hide()


current = ''

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Audioplayer()
    ex.show()

    sys.exit(app.exec())
