'''
@Author: Yang
@Date: 2019-11-11 17:13:11
@LastEditors: Yang
@LastEditTime: 2019-11-12 14:31:41
@FilePath: /Python/qt.py
@Description:
'''

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout, QFormLayout, QLineEdit, QRadioButton

import sys


class PackageInstaller(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(600, 400)
        self.center()

        formlayout1 = QFormLayout()
        nameLabel = QLabel("姓名")
        nameLineEdit = QLineEdit("")
        formlayout1.addRow(nameLabel, nameLineEdit)
        # self.setLayout(formlayout1)

        formlayout2 = QFormLayout()
        label1 = QLabel("请选择")
        # btn1 = QRadioButton('1')
        # btn2 = QRadioButton('2')
        # btn3 = QRadioButton('3')
        formlayout2.addRow(label1)

        # execbtn = QPushButton('执行', self)
        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(execbtn)
        # hbox.addStretch(1)
        vbox = QVBoxLayout()

        vbox.addLayout(formlayout1)
        vbox.addStretch(1)
        vbox.addLayout(formlayout2)
        self.setLayout(vbox)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PackageInstaller()
    sys.exit(app.exec_())


"""
def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(850, 650)
    w.move(300, 200)
    w.setWindowTitle('HAHAHA')
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
"""
