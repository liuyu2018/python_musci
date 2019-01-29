# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'download_song.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import QQmusic_download
import sys,_thread

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1102, 644)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.INPUT_SEARCH = QtWidgets.QLineEdit(self.centralwidget)
        self.INPUT_SEARCH.setGeometry(QtCore.QRect(110, 50, 611, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.INPUT_SEARCH.setFont(font)
        self.INPUT_SEARCH.setObjectName("INPUT_SEARCH")
        self.BTN_SEARCH = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_SEARCH.setGeometry(QtCore.QRect(760, 50, 75, 23))
        self.BTN_SEARCH.setObjectName("BTN_SEARCH")
        self.TEXT_DOWNLOAD_RESULT = QtWidgets.QTextEdit(self.centralwidget)
        self.TEXT_DOWNLOAD_RESULT.setGeometry(QtCore.QRect(690, 90, 391, 461))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.TEXT_DOWNLOAD_RESULT.setFont(font)
        self.TEXT_DOWNLOAD_RESULT.setObjectName("TEXT_DOWNLOAD_RESULT")
        self.TEXT_SEARCH_RESUTL = QtWidgets.QTextEdit(self.centralwidget)
        self.TEXT_SEARCH_RESUTL.setGeometry(QtCore.QRect(40, 90, 531, 491))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.TEXT_SEARCH_RESUTL.setFont(font)
        self.TEXT_SEARCH_RESUTL.setObjectName("TEXT_SEARCH_RESUTL")
        self.INPUT_DOWNLOAD_NUM = QtWidgets.QLineEdit(self.centralwidget)
        self.INPUT_DOWNLOAD_NUM.setGeometry(QtCore.QRect(590, 130, 71, 31))
        self.INPUT_DOWNLOAD_NUM.setObjectName("INPUT_DOWNLOAD_NUM")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.BTN_DOWNLOAD = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_DOWNLOAD.setGeometry(QtCore.QRect(590, 180, 75, 23))
        self.BTN_DOWNLOAD.setObjectName("BTN_DOWNLOAD")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(690, 570, 81, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.INPUT_SAVE_PATH = QtWidgets.QLineEdit(self.centralwidget)
        self.INPUT_SAVE_PATH.setGeometry(QtCore.QRect(770, 570, 311, 20))
        self.INPUT_SAVE_PATH.setObjectName("INPUT_SAVE_PATH")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #自定义参数
        self.songs = []
        self.save_file_path = ""

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "歌曲名："))
        self.BTN_SEARCH.setText(_translate("MainWindow", "搜索"))
        self.label_2.setText(_translate("MainWindow", "下载序号："))
        self.BTN_DOWNLOAD.setText(_translate("MainWindow", "下载"))
        self.label_3.setText(_translate("MainWindow", "存放路径："))

    def search_songs(self):
        song_name = self.INPUT_SEARCH.text()
        _thread.start_new_thread(self.get_and_set_song_list(song_name))

    def get_and_set_song_list(self,song_name):
        songs = QQmusic_download.get_song_list(song_name)
        self.TEXT_SEARCH_RESUTL.setText('')
        if songs['totalnum'] == 0 : 
            print('没有搜到此歌曲，请换个关键字')
            self.TEXT_SEARCH_RESUTL.setText('没有搜到此歌曲，请换个关键字')
        else:
            self.songs = songs
            for num, song in enumerate(songs['list']):
                songname = song['songname']
                singer_length = len(song['singer'])
                singers = []
                for i in range(singer_length):
                    singers.append(song['singer'][i]['name'])
                singers = ('/').join(singers)
                album_name = song['albumname']
                time = song['interval']
                m, s = divmod(time, 60)
                time = "%02d:%02d" % (m, s)
                print(num,'歌曲名字：',songname,'作者：' ,singers, '专辑：',album_name, '时长：',time)
                self.TEXT_SEARCH_RESUTL.append(str(num) +"  歌名："+ songname +"  作者："+ singers +"  专辑："+album_name+"  时长："+time)

    def download(self):
        select_no  = int(self.INPUT_DOWNLOAD_NUM.text())
        _thread.start_new_thread(self.download_by_no(select_no))

    def download_by_no(self,no):
        url = QQmusic_download.get_mp3_url(self.songs,int(no))
        if not url :
            print('歌曲已下架 找不到下载地址 下载失败')
            self.TEXT_DOWNLOAD_RESULT.append('歌曲已下架 找不到下载地址 下载失败')
        else:
            songname = self.songs['list'][int(no)]['songname']
            download = QQmusic_download.download_mp3(url, songname,"")
            if download[0]:
                self.TEXT_DOWNLOAD_RESULT.append('歌曲 '+songname+' 下载成功，路径：'+download[1])
            else:
                self.TEXT_DOWNLOAD_RESULT.append('歌曲 '+songname+' 下载失败')

    def bind_event(self):
        self.BTN_SEARCH.clicked.connect(self.search_songs)
        self.BTN_DOWNLOAD.clicked.connect(self.download)


if __name__ == "__main__":             
    app = QtWidgets.QApplication(sys.argv) 
    MainWindow = QtWidgets.QMainWindow()  
    ui = Ui_MainWindow()                
    ui.setupUi(MainWindow)                
    ui.bind_event()

    MainWindow.show()     
    sys.exit(app.exec_())    
