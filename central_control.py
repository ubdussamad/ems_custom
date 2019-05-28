# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mcw.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time
USER = ''
try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(746, 503)
        #MainWindow.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2C3E50, stop:1 #FD746C);"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        deleteShortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Esc'),self.centralwidget)
        deleteShortcut.activated.connect(self.ret_login)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.rw = QtWidgets.QPushButton(self.centralwidget)
        self.rw.setObjectName("rw")
        self.rw.clicked.connect(self.routine_wcall)
        self.gridLayout.addWidget(self.rw, 0, 0, 1, 1)
        self.sw = QtWidgets.QPushButton(self.centralwidget)
        self.sw.setObjectName("sw")
        self.sw.clicked.connect(self.status_wcall)
        self.gridLayout.addWidget(self.sw, 0, 1, 1, 1)
        self.cm = QtWidgets.QPushButton(self.centralwidget)
        self.cm.setObjectName("cm")
        self.cm.clicked.connect(self.customer_wcall)
        self.gridLayout.addWidget(self.cm, 0, 2, 1, 1)
        self.im = QtWidgets.QPushButton(self.centralwidget)
        self.im.setObjectName("im")
        self.im.clicked.connect(self.inventory_wcall)
        self.gridLayout.addWidget(self.im, 1, 0, 1, 1)
        self.st = QtWidgets.QPushButton(self.centralwidget)
        self.st.setObjectName("st")
        self.st.clicked.connect(self.history_wcall)
        self.gridLayout.addWidget(self.st, 1, 1, 1, 1)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.ret_login)
        self.gridLayout.addWidget(self.exit, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.data = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.data.setFont(font)
        self.data.setAlignment(QtCore.Qt.AlignCenter)
        self.data.setObjectName("data")
        self.gridLayout_2.addWidget(self.data, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(47)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "EMS | Central Control", None))
        self.rw.setText(_translate("MainWindow", "Routine Window", None))
        self.sw.setText(_translate("MainWindow", "Status Window", None))
        self.cm.setText(_translate("MainWindow", "Customer Managment Window", None))
        self.im.setText(_translate("MainWindow", "Inventory Management Window", None))
        self.st.setText(_translate("MainWindow", "History", None))
        self.exit.setText(_translate("MainWindow", "Back", None))
        self.label.setText(_translate("MainWindow", "Please select the utility you wish to use", None))
        self.data.setText(_translate("MainWindow",  "%s | %s"%(time.ctime(),USER), None))
        self.label_2.setText(_translate("MainWindow", "EMS | Central Control", None))

class central_control_window(QtWidgets.QMainWindow, Ui_MainWindow):
    routine = QtCore.pyqtSignal()
    status = QtCore.pyqtSignal()
    customer = QtCore.pyqtSignal()
    inventory = QtCore.pyqtSignal()
    history = QtCore.pyqtSignal()
    ret = QtCore.pyqtSignal()
    def __init__(self, parent=None , user = ''):
        super(central_control_window, self).__init__(parent)
        self.setupUi(self)
    ret = QtCore.pyqtSignal()
    def ret_login(self):
        self.ret.emit()
        self.close()
    def show_decorator(self,user):
        #print("Username is: %s"%user)
        USER = user
        self.data.setText(_translate("MainWindow",  "%s | %s"%(time.ctime(),user.capitalize()), None))
        #self.retranslateUi(self)
        self.show()
    @QtCore.pyqtSlot()
    def history_wcall(self):self.history.emit();self.close()
    @QtCore.pyqtSlot()
    def routine_wcall(self):self.routine.emit();self.close()
    @QtCore.pyqtSlot()
    def status_wcall(self):self.status.emit();self.close()
    @QtCore.pyqtSlot()
    def customer_wcall(self):self.customer.emit();self.close()
    @QtCore.pyqtSlot()
    def inventory_wcall(self):self.inventory.emit();self.close()
