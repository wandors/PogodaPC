# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PogodaPC.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import os
import tempfile
import winreg
from urllib.request import *
from bs4 import BeautifulSoup
from PIL import Image, ImageOps
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 305)
        self.disctop = QtWidgets.QApplication.desktop()
        Form.move(int(self.disctop.width() - 300), 460)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 301, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(2)
        self.shadow.setColor(QtGui.QColor(0, 0, 0))
        self.shadow.setOffset(5)
        self.label.setGraphicsEffect(self.shadow)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(31)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 271, 181))
        self.shadow_2 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_2.setBlurRadius(2)
        self.shadow_2.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_2.setOffset(5)
        self.label_2.setGraphicsEffect(self.shadow_2)
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 220, 281, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        self.shadow_3 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_3.setBlurRadius(2)
        self.shadow_3.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_3.setOffset(5)
        self.label_3.setGraphicsEffect(self.shadow_3)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", ""))

    def upd(self):
        try:
            self.paths = tempfile.gettempdir() + "\\"
            # В нижней строку прописываем адрес на страницу региона здес адрес не полный#
            self.urs = Request("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%96%D0%B2%D0%B0%D0%BD%D1%87%D1%96")
            ##########################################################################################
            self.urs.add_header('User-Agent',
                                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,'
                                ' like Gecko) Chrome/45.0.2454.85 Safari/537.36 ')
            self.html_doc = urlopen(self.urs).read()
            self.soup = BeautifulSoup(self.html_doc, 'html.parser')
            self.teb = self.soup.find('div', 'lSide')
            for i in self.teb.find_all("img"):
                self.linc = "http:" + str(i)[int(str(i).find("src") + 5):int(str(i).find("width") - 2)]
            for ii in self.soup.find('p', 'today-temp'):
                self.label_3.setText(str(ii.string))
            self.uri = Request(self.linc)
            self.uri.add_header('User-Agent',
                                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,'
                                ' like Gecko) Chrome/45.0.2454.85 Safari/537.36 ')
            self.ur = urlopen(self.uri)
            self.fil = open(self.paths + "11.jpg", "wb")
            self.fil.write(self.ur.read())
            self.fil.close()
            self.ur.close()
            self.im = Image.open(self.paths + "11.jpg")
            self.im.save(self.paths + "11.png", "PNG")
            self.im = Image.open(self.paths + "11.png")
            self.pix = self.im.load()
            self.xx, self.yy = self.im.size
            # Обработка изображения убераем белий вон и оставляем только самк картинку
            self.x = 0
            self.y = 0
            while self.x < self.xx and self.y < self.yy:
                if self.pix[self.x, self.y] == (255, 255, 255):
                    self.pix[self.x, self.y] = (0, 0, 0, 0)
                self.x += 1
                if self.x == self.xx:
                    self.y += 1
                    self.x = 0
            self.im.save(self.paths + "11.png", "PNG")
            self.mask = Image.open(self.paths + "11.png").convert('L')
            self.output = ImageOps.fit(self.im, self.mask.size, centering=(0.5, 0.5))
            self.output.putalpha(self.mask)
            self.output.save(self.paths + "output.png")
            self.label.setText("За вікном!!!")
            self.label_2.setPixmap(QtGui.QPixmap(self.paths + "output.png"))
            try:
                os.remove(self.paths + "11.jpg")
                os.remove(self.paths + "11.png")
                os.remove(self.paths + "11.png")
            except:
                pass
            self.timer.setInterval(1800000)
        except:
            self.label.setText("Нет сети!!!")
            self.label_2.setPixmap(QtGui.QPixmap(None))
            self.label_3.setText("")
            self.timer.setInterval(1000)

    def Timers(self):
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.upd)
        self.timer.start()



if __name__ == "__main__":
    import sys
    try:
        regs = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        mykeys = winreg.OpenKey(regs, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(mykeys, 'PogodaPC')
        winreg.CloseKey(self.mykeys)
    except:
        pass
    regs = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    mykeys = winreg.OpenKey(regs, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(mykeys, 'PogodaPC', 0, winreg.REG_SZ, '"' + sys.argv[0] + '"' + " Minimum")
    winreg.CloseKey(mykeys)
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.Timers()
    Form.show()
    sys.exit(app.exec_())
