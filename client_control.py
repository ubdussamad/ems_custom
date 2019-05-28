# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cmm.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ems_core import *
some = ems_core('ems','admin')

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def add_new(self):
        index = self.ivn.rowCount()+1
        self.ivn.setRowCount(index)
    def clr_due_routine(self):
        print("Due Clearing Routine Clear!")
        amount = self.due_clr_amt.text()
        amount = amount if amount else 0
        indexes = [i.row() for i in self.ivn.selectionModel().selectedRows()]
        if indexes:
            index = indexes[0]
            c_id = self.ivn.item(index,0).text()
            table_amount = self.ivn.item(index,2).text()
            delta = float(table_amount) - float(amount)
            delta = QtWidgets.QTableWidgetItem(str(delta))
            self.ivn.setItem(index,2,delta)
            self.update_details()
            
        else:
            print(False)
        
    def update_details(self):
        indexes = [i.row() for i in self.ivn.selectionModel().selectedRows()]
        index = indexes[0]
        self.c_name.setText(self.ivn.item(index,1).text())
        self.c_due.setText(self.ivn.item(index,2).text())
        self.c_total.setText(self.ivn.item(index,4).text())
    def update_ivn_routine( self ):  #Triggered by update button
        number_of_rows = self.ivn.rowCount()
        for i in range(number_of_rows):
            key = self.ivn.item(i , 0).text() #C_id
            name = self.ivn.item(i, 1).text()
            due  = self.ivn.item(i, 2).text()
            unit = self.ivn.item(i, 3).text()
            amount = self.ivn.item(i,4).text()
            desc = self.ivn.item(i, 5).text()

            is_key = some.cmm.is_user(key)

            if is_key:
                some.cmm.update( key , action=False , amount=0 , data = [name,due,unit,amount,desc])
            else:
                some.cmm.append([name,due,unit,amount,desc])
        self.query_ivn()

    def del_item_routine(self):
        #Just delete that item form the database and update
        indexes = [i.row() for i in self.ivn.selectionModel().selectedRows()]
        usr = self.ivn.item(indexes[0],1).text()
        reply = QtWidgets.QMessageBox.question(self.centralwidget, 'Delete User %s from System??'%usr.upper(), 
                 'Are you sure? \nIf you delete this user %s, all his data/dues will be lost!'%usr.upper(), QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            if indexes:
                index = indexes[0]
                p_id = self.ivn.item(index,0).text()
                self.ivn.removeRow(index)
                some.cmm.delete(p_id)
            else:
                print(False)
        else:
            pass
    def query_ivn(self, query=''):
        self.ivn.setRowCount(0);
        self.ivn_tuple = some.cmm.search(self.ivn_search.text())
        self.ivn_length = len(self.ivn_tuple)
        self.ivn.setRowCount(self.ivn_length)
        
        for i in range(0,self.ivn_length):
            c_id = QtWidgets.QTableWidgetItem(str(self.ivn_tuple[i][0]))
            client = QtWidgets.QTableWidgetItem(str(self.ivn_tuple[i][1]))
            due = QtWidgets.QTableWidgetItem(str(self.ivn_tuple[i][2]))
            unit = QtWidgets.QTableWidgetItem(str(self.ivn_tuple[i][3]))
            net = QtWidgets.QTableWidgetItem(str(self.ivn_tuple[i][4]))
            desc = QtWidgets.QTableWidgetItem(str(self.ivn_tuple[i][5]))
            self.ivn.setItem(i,0,c_id)
            self.ivn.setItem(i,1,client)
            self.ivn.setItem(i,2,due)
            self.ivn.setItem(i,3,unit)
            self.ivn.setItem(i,4,net)
            self.ivn.setItem(i,5,desc)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 681)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        deleteShortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Esc'),self.centralwidget)
        try:
            deleteShortcut.activated.connect(self.ret_login)
        except:
            print("Unit test mode!")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(820, 264, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(820, 304, 68, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(820, 334, 68, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(820, 364, 141, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(820, 414, 251, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(0,10, 0);")
        self.label_7.setObjectName("label_7")
        self.c_name = QtWidgets.QLabel(self.centralwidget)
        self.c_name.setGeometry(QtCore.QRect(990, 304, 68, 17))
        self.c_name.setObjectName("c_name")
        self.c_due = QtWidgets.QLabel(self.centralwidget)
        self.c_due.setGeometry(QtCore.QRect(990, 334, 68, 17))
        self.c_due.setObjectName("c_due")
        self.c_total = QtWidgets.QLabel(self.centralwidget)
        self.c_total.setGeometry(QtCore.QRect(990, 364, 68, 17))
        self.c_total.setObjectName("c_total")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(820, 444, 161, 17))
        self.label_11.setObjectName("label_11")
        self.due_clr_amt = QtWidgets.QLineEdit(self.centralwidget)
        self.due_clr_amt.setGeometry(QtCore.QRect(820, 464, 181, 27))
        self.due_clr_amt.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.due_clr_amt.setObjectName("due_clr_amt")
        self.clr_due = QtWidgets.QPushButton(self.centralwidget)
        self.clr_due.setGeometry(QtCore.QRect(820, 494, 101, 27))
        self.clr_due.setMaximumSize(QtCore.QSize(520, 16777215))
        self.clr_due.setObjectName("clr_due")
        self.clr_due.clicked.connect(self.clr_due_routine)
        # Update Button
        self.update_cl = QtWidgets.QPushButton(self.centralwidget)
        self.update_cl.setGeometry(QtCore.QRect(820, 154, 97, 27))
        self.update_cl.setStyleSheet("")
        self.update_cl.setObjectName("update_cl")
        self.update_cl.clicked.connect(self.update_ivn_routine)
        #Delete client
        self.del_cl = QtWidgets.QPushButton(self.centralwidget)
        self.del_cl.setGeometry(QtCore.QRect(820, 187, 145, 27))
        self.del_cl.setObjectName("del_cl")
        self.del_cl.clicked.connect(self.del_item_routine)
        #Add Clients
        self.add_cl = QtWidgets.QPushButton(self.centralwidget)
        self.add_cl.setGeometry(QtCore.QRect(820, 121, 117, 27))
        self.add_cl.setObjectName("add_cl")
        self.add_cl.clicked.connect(self.add_new)
        #Exit button
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(820, 220, 85, 27))
        self.exit.setObjectName("exit")
        try:
            self.exit.clicked.connect(self.ret_login)
        except:
            pass
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 791, 621))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        #IVN Search
        self.ivn_search = QtWidgets.QLineEdit(self.layoutWidget)
        self.ivn_search.setObjectName("ivn_search")
        self.ivn_search.textChanged.connect(lambda x:self.query_ivn(self.ivn_search.text()))
        self.verticalLayout_2.addWidget(self.ivn_search)

        #IVN Routine
        self.ivn = QtWidgets.QTableWidget(self.layoutWidget)
        self.ivn.setObjectName("ivn")
        self.ivn.setAlternatingRowColors(True)
        self.ivn.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ivn.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ivn.setTextElideMode(QtCore.Qt.ElideRight)
        self.ivn.setGridStyle(QtCore.Qt.NoPen)
        self.ivn.itemClicked.connect(self.update_details)
        self.ivn.resizeColumnsToContents()
        
        self.ivn_tuple = some.cmm.search(self.ivn_search.text())
        self.ivn_length = len(self.ivn_tuple)
        self.ivn.setRowCount(self.ivn_length)
        self.ivn.setColumnCount(6)
        self.ivn_table_headers = ['C_id','Client','Due','Unit','Total Amt','Description']# Ulta crude scaling technique
        self.ivn.setHorizontalHeaderLabels(self.ivn_table_headers)

        for i in range(0,self.ivn_length):
            c_id = QtWidgets.QTableWidgetItem(str(self.ivn_tuple[i][0]))
            client = QtWidgets.QTableWidgetItem(str(self.ivn_tuple[i][1]))
            due = QtWidgets.QTableWidgetItem(str(self.ivn_tuple[i][2]))
            unit = QtWidgets.QTableWidgetItem(str(self.ivn_tuple[i][3]))
            net = QtWidgets.QTableWidgetItem(str(self.ivn_tuple[i][4]))
            desc = QtWidgets.QTableWidgetItem(str(self.ivn_tuple[i][5]))
            self.ivn.setItem(i,0,c_id)
            self.ivn.setItem(i,1,client)
            self.ivn.setItem(i,2,due)
            self.ivn.setItem(i,3,unit)
            self.ivn.setItem(i,4,net)
            self.ivn.setItem(i,5,desc)
        self.verticalLayout_2.addWidget(self.ivn)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "EMS | Client Management Control", None))
        self.label_2.setText(_translate("MainWindow", "Customer Details", None))
        self.label_4.setText(_translate("MainWindow", "Name", None))
        self.label_5.setText(_translate("MainWindow", "Due", None))
        self.label_6.setText(_translate("MainWindow", "Total Transactions", None))
        self.label_7.setText(_translate("MainWindow", "Clear Due for this Customer:", None))
        self.c_name.setText(_translate("MainWindow", "Random", None))
        self.c_due.setText(_translate("MainWindow", "TextLabel", None))
        self.c_total.setText(_translate("MainWindow", "TextLabel", None))
        self.label_11.setText(_translate("MainWindow", "Enter amount paid:", None))
        self.due_clr_amt.setPlaceholderText(_translate("MainWindow", "Enter numbers..", None))
        self.clr_due.setText(_translate("MainWindow", "Clear Due", None))
        self.update_cl.setText(_translate("MainWindow", "Update List", None))
        self.del_cl.setText(_translate("MainWindow", "Remove Customer", None))
        self.add_cl.setText(_translate("MainWindow", "Add Customer", None))
        self.exit.setText(_translate("MainWindow", "Exit", None))
        self.label.setText(_translate("MainWindow", "Search and select customers", None))
        self.ivn_search.setPlaceholderText(_translate("MainWindow", "Enter customer\'s name here", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
else:
    class client_control_window(QtWidgets.QMainWindow, Ui_MainWindow):
        closed = QtCore.pyqtSignal()
        ret = QtCore.pyqtSignal()
        def __init__(self, parent=None , user = ''):
            super(client_control_window, self).__init__(parent)
            USER = user
            self.setupUi(self)
        @QtCore.pyqtSlot()
        def ret_login(self):
            self.ret.emit()
            self.close()
        def show_decorator(self,user):
            global some
            some = ems_core('ems',user)
            self.show()
        @QtCore.pyqtSlot()
        def dummy(self):
            self.closed.emit()
            self.close()
