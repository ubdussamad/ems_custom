# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'status_new.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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
    def genrate_data(self):
        some.lmm.cursor.execute('SELECT Net_Amt, Time FROM hmm')
        self.data = some.lmm.cursor.fetchall()
    def get_total(self):
        year = self.year.currentText()
        month = self.month.currentText()
        data = [ float(i[0]) if (year in i[1] and month in i[1]) else 0.0 for i in self.data ]
        total = sum(data)
        self.amount.setText('%.2f'%total)
        self.total.setText('%.2f'%total)
        return
    def update_tables(self , table ,data , formatting ):
        try:
            self.get_total()
        except Exception as err:
            pass
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

    def total_update(self):
        self.update_tables( self.cl_due , some.cmm.dues() , ['Customer','Due','Unit'])
        self.update_tables( self.mbs , some.lmm.most_bought() , ['Product','Times Sold'])
        self.update_tables( self.sivn , some.imm.scarce() , ['Product','Qty Left','Unit'])

    def setupUi(self, MainWindow):
        self.genrate_data()
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        deleteShortcut = QtGui.QShortcut(QtGui.QKeySequence('Esc'),self.centralwidget)
        deleteShortcut.activated.connect(self.ret_login)
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
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

        # Client due routine
        self.cl_due = QtGui.QTableWidget(self.centralwidget)
        self.cl_due.setObjectName(_fromUtf8("cl_due"))
        self.update_tables( self.cl_due , some.cmm.dues() , ['Customer','Due','Unit'])
        self.gridLayout.addWidget(self.cl_due, 1, 0, 1, 1)

        # Most Bought Stock
        self.mbs = QtGui.QTableWidget(self.centralwidget)
        self.mbs.setObjectName(_fromUtf8("mbs"))
        self.update_tables( self.mbs , some.lmm.most_bought() , ['Product','Times Sold'])
        self.gridLayout.addWidget(self.mbs, 1, 1, 1, 1)

        # Scarce inventory
        self.sivn = QtGui.QTableWidget(self.centralwidget)
        self.sivn.setObjectName(_fromUtf8("sivn"))
        self.update_tables( self.sivn , some.imm.scarce() , ['Product','Qty Left','Unit'])


        self.gridLayout.addWidget(self.sivn, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)

        # Month Selection Combo box
        self.month = QtGui.QComboBox(self.centralwidget)
        self.month.setObjectName(_fromUtf8("month"))
        self.horizontalLayout.addWidget(self.month)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)

        # Year selection combobox
        self.year = QtGui.QComboBox(self.centralwidget)
        self.year.setObjectName(_fromUtf8("year"))
        self.horizontalLayout.addWidget(self.year)

        years = set([ i[1][-4:] for i in self.data ])
        months = set([ i[1][3:7] for i in self.data ])
        for i in years:
            self.year.addItem(i)
        self.month.clear()
        for i in months:
            self.month.addItem(i)

        # Update button
        self.update = QtGui.QPushButton(self.centralwidget)
        self.update.setObjectName(_fromUtf8("update"))
        self.update.clicked.connect(self.total_update)
        self.horizontalLayout.addWidget(self.update)

        # Back button
        self.back = QtGui.QPushButton(self.centralwidget)
        self.back.setObjectName(_fromUtf8("back"))
        self.back.clicked.connect(self.ret_login)
        self.horizontalLayout.addWidget(self.back)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)

        # Amount Label
        self.amount = QtGui.QLabel(self.centralwidget)
        self.amount.setObjectName(_fromUtf8("amount"))
        self.horizontalLayout_2.addWidget(self.amount)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)
        self.extra_des = QtGui.QLabel(self.centralwidget)
        self.extra_des.setText(_fromUtf8(""))
        self.extra_des.setObjectName(_fromUtf8("extra_des"))
        self.horizontalLayout_2.addWidget(self.extra_des)
        self.extra_amt = QtGui.QLabel(self.centralwidget)
        self.extra_amt.setText(_fromUtf8(""))
        self.extra_amt.setObjectName(_fromUtf8("extra_amt"))
        self.horizontalLayout_2.addWidget(self.extra_amt)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_2.addWidget(self.label_9)

        # Total amount
        self.total = QtGui.QLabel(self.centralwidget)
        self.total.setObjectName(_fromUtf8("total"))
        self.horizontalLayout_2.addWidget(self.total)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "EMS | Status Utility", None))
        self.label.setText(_translate("MainWindow", "Customers with most Due", None))
        self.label_2.setText(_translate("MainWindow", "Most bought Stock", None))
        self.label_3.setText(_translate("MainWindow", "Scarce Stock items", None))
        self.label_4.setText(_translate("MainWindow", "Total Sale For the month:", None))
        self.label_5.setText(_translate("MainWindow", "and Year:", None))
        self.update.setText(_translate("MainWindow", "Update", None))
        self.back.setText(_translate("MainWindow", "Back", None))
        self.label_6.setText(_translate("MainWindow", "Amount:", None))
        self.amount.setText(_translate("MainWindow", "0.0", None))
        self.label_8.setText(_translate("MainWindow", "Rupees", None))
        self.label_9.setText(_translate("MainWindow", "Total:", None))
        self.total.setText(_translate("MainWindow", "0.0", None))


class status_window(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None , user = ''):
        super(status_window, self).__init__(parent)
        USER = user
        self.setupUi(self)
    ret = QtCore.pyqtSignal()
    def ret_login(self):
        self.ret.emit()
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
