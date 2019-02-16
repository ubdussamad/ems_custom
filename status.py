# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'status.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from ems_core import *
some = ems_core('ems','kallu')
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
    def update_tables(self , table ,data , formatting ):
        table.setAlternatingRowColors(True)
        table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        table.setTextElideMode(QtCore.Qt.ElideRight)
        table.setGridStyle(QtCore.Qt.NoPen)
        #self.ivn.itemClicked.connect(self.append_to_ivn)
        table.resizeColumnsToContents()
        self.length = len(data)
        table.setRowCount(self.length)
        table.setColumnCount(len(formatting))
        table.setHorizontalHeaderLabels(formatting)

        for i in range(0,self.length):
            db_data = [ QtGui.QTableWidgetItem(str(j)) for j in data[i] ]
            for j in range(len(db_data)):
                table.setItem(i,j,db_data[j])
                
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        # Due list
        self.cl_due = QtGui.QTableWidget(self.centralwidget)
        self.cl_due.setObjectName(_fromUtf8("cl_due"))
        self.update_tables( self.cl_due , some.cmm.dues() , ['Customer','Due','Unit'])
        self.gridLayout.addWidget(self.cl_due, 1, 0, 1, 1)

        # Bought Stock List
        self.mbs = QtGui.QTableWidget(self.centralwidget)
        self.mbs.setObjectName(_fromUtf8("mbs"))
        self.gridLayout.addWidget(self.mbs, 1, 1, 1, 1)
        self.update_tables( self.mbs , some.lmm.most_bought() , ['Product','Times Sold'])
        #Scarce Inventory list
        self.sivn = QtGui.QTableWidget(self.centralwidget)
        self.sivn.setObjectName(_fromUtf8("sivn"))
        self.update_tables( self.sivn , some.imm.scarce() , ['Product','Qty Left','Unit'])

        
        self.gridLayout.addWidget(self.sivn, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.guidance = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guidance.sizePolicy().hasHeightForWidth())
        self.guidance.setSizePolicy(sizePolicy)
        self.guidance.setMinimumSize(QtCore.QSize(47, 218))
        self.guidance.setText(_fromUtf8(""))
        self.guidance.setObjectName(_fromUtf8("guidance"))
        self.gridLayout_2.addWidget(self.guidance, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Customers with most Due", None))
        self.label_2.setText(_translate("MainWindow", "Most bought Stock", None))
        self.label_3.setText(_translate("MainWindow", "Scarce Stock items", None))
        #self.label_4.setText(_translate("MainWindow", "Sales timing trend", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

