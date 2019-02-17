#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
USER = ''
from PyQt4 import QtCore, QtGui
import sqlite3,hashlib,time
from central_control import central_control_window
from client_control import client_control_window
from inventory_management import inventory_management_window
from routine_egui import routine_window
from status import status_window


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
   #def dummy(self,*args):
    #    self.close()
    def login(self):
        self.server = sqlite3.connect('ems.db')
        self.cursor = self.server.cursor()
        user = self.lineEdit.text()
        self.cursor.execute('SELECT (password) FROM credentials WHERE user = (?)',
                                    (user,))
        data = self.cursor.fetchall()
        if not len(data):
            print("Wrong Username!")
            return(-1)
        if data[0][0] == hashlib.md5(self.lineEdit_2.text().encode()).hexdigest():
            print("Successful Login!")
            self.cursor.close() #Future Palns to close the connections
            self.server.close()
            global USER
            USER = user
            #Direct the pane to future
            self.dummy()
            #close(user)
        else:
            return(-1)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(_fromUtf8("background-image: url(:/backgrounds/resources/bg_tile.jpeg);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 120, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"selection-background-color: rgba(255, 255, 255, 0);\n"
"alternate-background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"border-right-color: rgba(255, 255, 255, 0);\n"
"border-bottom-color: rgba(255, 255, 255, 0);\n"
"border-left-color: rgba(255, 255, 255, 0);"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 190, 241, 27))
        self.lineEdit.setStyleSheet(_fromUtf8("color: rgb(200,200,200);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"selection-background-color: rgba(255, 255, 255, 0);\n"
"alternate-background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"border-right-color: rgba(255, 255, 255, 0);\n"
"border-bottom-color: rgba(255, 255, 255, 0);\n"
"border-left-color: rgba(255, 255, 255, 0);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 240, 241, 27))
        self.lineEdit_2.setStyleSheet(_fromUtf8("color: rgb(200,200,200);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"selection-background-color: rgba(255, 255, 255, 0);\n"
"alternate-background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"border-right-color: rgba(255, 255, 255, 0);\n"
"border-bottom-color: rgba(255, 255, 255, 0);\n"
"border-left-color: rgba(255, 255, 255, 0);"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.textChanged.connect(self.login)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 290, 111, 31))
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"selection-background-color: rgba(255, 255, 255, 0);\n"
"alternate-background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"border-right-color: rgba(255, 255, 255, 0);\n"
"border-bottom-color: rgba(255, 255, 255, 0);\n"
"border-left-color: rgba(255, 255, 255, 0);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.login)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "EMS | Login", None))
        self.label.setText(_translate("MainWindow", "Login | EMS", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password", None))
        self.pushButton.setText(_translate("MainWindow", "Login", None))

from resources import resource_rc
class XMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(XMainWindow, self).__init__(parent)
        self.setupUi(self)
    @QtCore.pyqtSlot()
    def dummy(self):
        self.closed.emit()
        self.close()

import sys

def main():
    app = QtGui.QApplication.instance()
    if app is None:
        app = QtGui.QApplication(sys.argv)
        
    wa = XMainWindow()
    wb = central_control_window(user=USER)
    wb.ret.connect(wa.show)
    wc = client_control_window()
    wd = inventory_management_window()
    we = routine_window()
    wf = status_window()
    wc.ret.connect(wb.show)
    wd.ret.connect(wb.show)
    we.ret.connect(wb.show)
    wf.ret.connect(wb.show)
    wa.closed.connect(lambda: wb.show_decorator(USER))
    wb.routine.connect(lambda :we.show_decorator(USER))
    wb.status.connect(lambda :wf.show_decorator(USER))
    wb.customer.connect(lambda :wc.show_decorator(USER))
    wb.inventory.connect(lambda :wd.show_decorator(USER))
    wa.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
