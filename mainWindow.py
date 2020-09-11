import sys
# from PyQt5.QtGui import
# from PyQt5.QtGui import QFont, QCursor, QPalette, QBrush, QColor
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import winsound
from time import sleep


class mainWindow(QWidget):
    def __init__(self):

        self.dic = {}
        self.dic['A'] = '01'
        self.dic['B'] = '1000'
        self.dic['C'] = '1010'
        self.dic['D'] = '100'
        self.dic['E'] = '0'
        self.dic['F'] = '0010'
        self.dic['G'] = '110'
        self.dic['H'] = '0000'
        self.dic['I'] = '00'
        self.dic['J'] = '0111'
        self.dic['K'] = '101'
        self.dic['L'] = '0100'
        self.dic['M'] = '11'
        self.dic['N'] = '10'
        self.dic['O'] = '111'
        self.dic['P'] = '0110'
        self.dic['Q'] = '1101'
        self.dic['R'] = '010'
        self.dic['S'] = '000'
        self.dic['T'] = '1'
        self.dic['U'] = '001'
        self.dic['V'] = '0001'
        self.dic['W'] = '011'
        self.dic['X'] = '1001'
        self.dic['Y'] = '1011'
        self.dic['Z'] = '1100'
        self.dic['1'] = '01111'
        self.dic['2'] = '00111'
        self.dic['3'] = '00011'
        self.dic['4'] = '00001'
        self.dic['5'] = '00000'
        self.dic['6'] = '10000'
        self.dic['7'] = '11000'
        self.dic['8'] = '11100'
        self.dic['9'] = '11110'
        self.dic['0'] = '11111'
        self.dic[' '] = '2'

        super().__init__()
        self.initUI()


    def initUI(self):
        #window
        self.setWindowTitle('BeepBeep-Morse')
        self.setWindowIcon(QtGui.QIcon('BeepIcon.png'))
        self.move(100, 100)
        self.resize(1200, 800)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(203, 240, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)

        self.setPalette(palette)

        #mainLabel
        mainLabel = QLabel('모스 부호로 바꿀 말을 써주세요', self)
        mainLabel.move(200, 80)
        mainLabel.resize(800, 100)

        font = QtGui.QFont()
        font.setFamily("210 Cherryblossom")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        mainLabel.setFont(font)
        mainLabel.setStyleSheet("")
        mainLabel.setAlignment(Qt.AlignCenter)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(68, 88, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)

        mainLabel.setPalette(palette)


        #mainEdit
        self.mainEdit = QLineEdit(self)
        self.mainEdit.move(200, 200)
        self.mainEdit.resize(800, 100)

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        self.mainEdit.setFont(font)
        self.mainEdit.setAlignment(Qt.AlignCenter)

        #button
        btn = QPushButton(self)
        btn.setText('CONVERT')
        btn.move(500, 350)
        btn.resize(200, 80)

        font = QtGui.QFont()
        font.setFamily("210 Paranusan")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        btn.setFont(font)
        btn.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        btn.setAutoFillBackground(False)
        btn.setStyleSheet("background-color: skyblue;"
                          "border-radius: 15px;"
                          "")
        btn.setDefault(False)
        btn.setFlat(False)

        btn.clicked.connect(self.convert)



        #subLabel
        self.subLabel = QLabel('', self)
        self.subLabel.move(200, 500)
        self.subLabel.resize(800, 200)

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(161, 105, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)

        self.subLabel.setPalette(palette)

        font = QtGui.QFont()
        font.setFamily("210 맨발의청춘 L")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.subLabel.setFont(font)
        self.subLabel.setAlignment(QtCore.Qt.AlignCenter)

        #eraseBtn
        eraseBtn = QPushButton(self)
        eraseBtn.move(1050, 700)
        eraseBtn.resize(100, 50)
        eraseBtn.setText("ERASE")
        eraseBtn.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

        font = QtGui.QFont()
        font.setFamily("210 Paranusan")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        eraseBtn.setFont(font)

        eraseBtn.setStyleSheet("background-color: #32a8a0;"
                          "border-radius: 5px;"
                          "")

        eraseBtn.clicked.connect(self.erase)



        self.show()


    #
    def convert(self):

        str = self.mainEdit.text().upper()
        temp = []
        conv = []
        convText = ''
        
        for i in str:
            if i in self.dic:
                temp.append(self.dic[i])

        for i in temp:
            listBool = []
            for element in i:
                if element == '0':
                    listBool.append(True)
                    convText += '따 '
                elif element == '1':
                    listBool.append(False)
                    convText += '따~ '

            conv.append(listBool)
            convText += '  '

        if convText.__len__() > 0:
            self.subLabel.setText(convText)
        else:
            self.subLabel.setText("알파벳과 숫자만 입력 가능합니다")

        print(conv)
        for i in conv:
            for element in i:
                if element:
                    winsound.Beep(1000, 80)
                else:
                    winsound.Beep(1000, 400)

            sleep(0.5)

    def erase(self):
        self.subLabel.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())
