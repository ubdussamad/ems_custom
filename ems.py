#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
USER = ''
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3,hashlib,time
from central_control import central_control_window
from client_control import client_control_window
from inventory_management import inventory_management_window
from routine_egui import routine_window
from history import history_window
from status import status_window


try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
   #def dummy(self,*args):
    #    self.close()
    def login(self):
        self.server = sqlite3.connect('data/ems.db')
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
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #1D4350, stop:1 #A43931);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 120, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"selection-background-color: rgba(255, 255, 255, 0);\n"
"alternate-background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"border-right-color: rgba(255, 255, 255, 0);\n"
"border-bottom-color: rgba(255, 255, 255, 0);\n"
"border-left-color: rgba(255, 255, 255, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 190, 241, 27))
        self.lineEdit.setStyleSheet("color: rgb(150,150,150);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"selection-background-color: rgba(255, 255, 255, 0);\n"
"alternate-background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"border-right-color: rgba(255, 255, 255, 0);\n"
"border-bottom-color: rgba(255, 255, 255, 0);\n"
"border-left-color: rgba(255, 255, 255, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 240, 241, 27))
        self.lineEdit_2.setStyleSheet("color: rgb(150,150,150);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"selection-background-color: rgba(255, 255, 255, 0);\n"
"alternate-background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"border-right-color: rgba(255, 255, 255, 0);\n"
"border-bottom-color: rgba(255, 255, 255, 0);\n"
"border-left-color: rgba(255, 255, 255, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password);
        self.lineEdit_2.textChanged.connect(self.login)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 290, 111, 31))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 10);\n"
"selection-background-color: rgba(255, 255, 255, 10);\n"
"alternate-background-color: rgba(255, 255, 255, 10);\n"
"border-color: rgba(255, 255, 255, 200);\n"
"border-right-color: rgba(255, 255, 255, 200);\n"
"border-bottom-color: rgba(255, 255, 255, 200);\n"
"border-left-color: rgba(255, 255, 255, 200);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Login | EMS", None))
        self.label.setText(_translate("MainWindow", "Login | EMS", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password", None))
        self.pushButton.setText(_translate("MainWindow", "Login", None))


class XMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(XMainWindow, self).__init__(parent)
        self.setupUi(self)
    @QtCore.pyqtSlot()
    def dummy(self):
        self.closed.emit()
        self.close()
    def show_decorator(self):
        self.lineEdit_2.clear()
        self.show()

import sys

def main():
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
        
    wa = XMainWindow()
    wb = central_control_window(user=USER)
    wb.ret.connect(wa.show_decorator)
    wc = client_control_window()
    wd = inventory_management_window()
    we = routine_window()
    wf = status_window()
    wg = history_window()
    
    wc.ret.connect(wb.show)
    wd.ret.connect(wb.show)
    we.ret.connect(wb.show)
    wf.ret.connect(wb.show)
    wg.ret.connect(wb.show)
    
    wa.closed.connect(lambda: wb.show_decorator(USER))
    wb.routine.connect(lambda :we.show_decorator(USER))
    wb.status.connect(lambda :wf.show_decorator(USER))
    wb.customer.connect(lambda :wc.show_decorator(USER))
    wb.inventory.connect(lambda :wd.show_decorator(USER))
    wb.history.connect(lambda :wg.show_decorator(USER))
    
    wa.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
