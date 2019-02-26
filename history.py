# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hisotry.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from recipt_genrator import *
from ems_core import *
some = ems_core('ems','admin')
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

    def query_history(self, query='' , qtype=0):
        self.history.setRowCount(0);
        self.history_tuple = sorted(some.lmm.search(query,qtype))
        self.history_length = len(self.history_tuple)
        self.history.setRowCount(self.history_length)
        for i in range(0,self.history_length):
            p_id = QtGui.QTableWidgetItem(str(self.history_tuple[i][0]))
            qty = QtGui.QTableWidgetItem(str(self.history_tuple[i][1]))
            unit = QtGui.QTableWidgetItem(str(self.history_tuple[i][2]))
            rate = QtGui.QTableWidgetItem(str(self.history_tuple[i][3]))
            desc = QtGui.QTableWidgetItem(str(self.history_tuple[i][4]))
            self.history.setItem(i,0,p_id)
            self.history.setItem(i,1,qty)
            self.history.setItem(i,2,unit)
            self.history.setItem(i,3,rate)
            self.history.setItem(i,4,desc)
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        #History Table
        self.history = QtGui.QTableWidget(self.centralwidget)
        self.history.setObjectName(_fromUtf8("history"))
        self.history.setColumnCount(5)
        self.history.setObjectName(_fromUtf8("history"))
        self.table_headers = ['Transaction id'+' '*25,'Date','Customer','Amount','Products'+' '*30]# Ulta crude scaling technique
        self.history.setHorizontalHeaderLabels(self.table_headers)
        self.history_tuple = sorted(some.lmm.search())
        self.history_length = len(self.history_tuple)
        self.history.setRowCount(self.history_length)
        self.history.setAlternatingRowColors(True)
        self.history.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.history.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.history.setTextElideMode(QtCore.Qt.ElideRight)
        self.history.setGridStyle(QtCore.Qt.NoPen)
        self.history.resizeColumnsToContents()
        self.history_length = len(self.history_tuple)
        self.history.setRowCount(self.history_length)
        for i in range(0,self.history_length):
            p_id = QtGui.QTableWidgetItem(str(self.history_tuple[i][0]))
            qty = QtGui.QTableWidgetItem(str(self.history_tuple[i][1]))
            unit = QtGui.QTableWidgetItem(str(self.history_tuple[i][2]))
            rate = QtGui.QTableWidgetItem(str(self.history_tuple[i][3]))
            desc = QtGui.QTableWidgetItem(str(self.history_tuple[i][4]))
            self.history.setItem(i,0,p_id)
            self.history.setItem(i,1,qty)
            self.history.setItem(i,2,unit)
            self.history.setItem(i,3,rate)
            self.history.setItem(i,4,desc)

        
        self.gridLayout.addWidget(self.history, 2, 0, 1, 3)

        #Update button
        self.update = QtGui.QPushButton(self.centralwidget)
        self.update.setObjectName(_fromUtf8("update"))
        self.gridLayout.addWidget(self.update, 3, 0, 1, 1)
        self.update.clicked.connect(self.query_history)

        #C name search widget
        self.cname = QtGui.QLineEdit(self.centralwidget)
        self.cname.setObjectName(_fromUtf8("cname"))
        self.gridLayout.addWidget(self.cname, 0, 2, 1, 1)
        self.cname.textChanged.connect(lambda x:self.query_history(self.cname.text(),2))

        #Search by date
        self.date = QtGui.QLineEdit(self.centralwidget)
        self.date.setObjectName(_fromUtf8("date"))        
        self.date.textChanged.connect(lambda x:self.query_history(self.date.text(),1))
        self.gridLayout.addWidget(self.date, 0, 1, 1, 1)

        #Search by tid
        self.tid = QtGui.QLineEdit(self.centralwidget)
        self.tid.setObjectName(_fromUtf8("tid"))
        self.tid.textChanged.connect(lambda x:self.query_history(self.tid.text(),0))
        self.gridLayout.addWidget(self.tid, 0, 0, 1, 1)

        #Back button
        self.back = QtGui.QPushButton(self.centralwidget)
        self.back.setObjectName(_fromUtf8("back"))
        self.back.clicked.connect(self.ret_login)
        self.gridLayout.addWidget(self.back, 3, 1, 1, 1)
        
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "EMS | History Management Module", None))
        self.update.setText(_translate("MainWindow", "Update", None))
        self.cname.setPlaceholderText(_translate("MainWindow", "Search with Customer name...", None))
        self.date.setPlaceholderText(_translate("MainWindow", "Search with date..", None))
        self.tid.setPlaceholderText(_translate("MainWindow", "Search with Transaction Id", None))
        self.back.setText(_translate("MainWindow", "Back", None))

class history_window(QtGui.QMainWindow, Ui_MainWindow):
    closed = QtCore.pyqtSignal()
    ret = QtCore.pyqtSignal()
    def ret_login(self):
        self.ret.emit()
        self.close()
    def __init__(self, parent=None , user = ''):
        super(history_window, self).__init__(parent)
        USER = user
        self.setupUi(self)
        
    @QtCore.pyqtSlot()
    def dummy(self):
        self.closed.emit()
        self.close()
    def show_decorator(self,user):
        global some
        some = ems_core('ems',user)
        self.show()
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

