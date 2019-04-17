# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mcw.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time
USER = ''
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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(746, 503)
        #MainWindow.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2C3E50, stop:1 #FD746C);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        deleteShortcut = QtGui.QShortcut(QtGui.QKeySequence('Esc'),self.centralwidget)
        deleteShortcut.activated.connect(self.ret_login)
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.rw = QtGui.QPushButton(self.centralwidget)
        self.rw.setObjectName(_fromUtf8("rw"))
        self.rw.clicked.connect(self.routine_wcall)
        self.gridLayout.addWidget(self.rw, 0, 0, 1, 1)
        self.sw = QtGui.QPushButton(self.centralwidget)
        self.sw.setObjectName(_fromUtf8("sw"))
        self.sw.clicked.connect(self.status_wcall)
        self.gridLayout.addWidget(self.sw, 0, 1, 1, 1)
        self.cm = QtGui.QPushButton(self.centralwidget)
        self.cm.setObjectName(_fromUtf8("cm"))
        self.cm.clicked.connect(self.customer_wcall)
        self.gridLayout.addWidget(self.cm, 0, 2, 1, 1)
        self.im = QtGui.QPushButton(self.centralwidget)
        self.im.setObjectName(_fromUtf8("im"))
        self.im.clicked.connect(self.inventory_wcall)
        self.gridLayout.addWidget(self.im, 1, 0, 1, 1)
        self.st = QtGui.QPushButton(self.centralwidget)
        self.st.setObjectName(_fromUtf8("st"))
        self.st.clicked.connect(self.history_wcall)
        self.gridLayout.addWidget(self.st, 1, 1, 1, 1)
        self.exit = QtGui.QPushButton(self.centralwidget)
        self.exit.setObjectName(_fromUtf8("exit"))
        self.exit.clicked.connect(self.ret_login)
        self.gridLayout.addWidget(self.exit, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.data = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.data.setFont(font)
        self.data.setAlignment(QtCore.Qt.AlignCenter)
        self.data.setObjectName(_fromUtf8("data"))
        self.gridLayout_2.addWidget(self.data, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(47)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
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

class central_control_window(QtGui.QMainWindow, Ui_MainWindow):
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
