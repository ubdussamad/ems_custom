# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ivm.ui'
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
    
    def update_ivn_routine( self ):  #Triggered by update button
        # We make a tuple that's queried by the search bar
        # We change the table accordingly to the search bar's key

        #Get data from table : self.ivn.item(i,1).text()
        # Embed data into table:
        # amount = QtGui.QTableWidgetItem(str(tmp))
        # self.ivn.setItem(i,0,p_id)
        rc,cc= self.ivn.rowCount() , self.ivn.columnCount()
        # Pickup data from ivn table
        for i in range(rc):
            KEY = self.ivn.item(i,0).text()
            qty = self.ivn.item(i,1).text()
            unit = self.ivn.item(i,2).text()
            rate = self.ivn.item(i,3).text()
            desc = self.ivn.item(i,4).text()
            data = [qty,unit,rate,desc]
            #print([i[0] for i in some.imm.return_item_names()])
            is_key = KEY in [i[0] for i in some.imm.return_item_names()]
            
            if not is_key:
                print("Key is: %s"%(KEY) , is_key)
                some.imm.append_ivn([KEY,qty,unit,rate,desc])
            else:
                some.imm.update( KEY , 'total_update' , data )
        self.query_ivn()
    def add_new(self):
        index = self.ivn.rowCount()+1
        self.ivn.setRowCount(index)
        p_id ='Enter Name'
        qty = 'Enter Qty'
        unit = 'Enter Unit'
        rate = 'Enter Rate'
        desc = 'Enter Description'
        p_id = QtGui.QTableWidgetItem(p_id)
        qty = QtGui.QTableWidgetItem(qty)
        unit = QtGui.QTableWidgetItem(unit)
        rate = QtGui.QTableWidgetItem(rate)
        desc = QtGui.QTableWidgetItem(desc)
        self.ivn.setItem(index,0,p_id)
        self.ivn.setItem(index,1,qty)
        self.ivn.setItem(index,2,unit)
        self.ivn.setItem(index,3,rate)
        self.ivn.setItem(index,4,desc)
        
    def del_item_routine(self):
        #Just delete that itme form the database and update
        indexes = [i.row() for i in self.ivn.selectionModel().selectedRows()]
        if indexes:
            index = indexes[0]
            p_id = self.ivn.item(index,0).text()
            self.ivn.removeRow(index)
            some.imm.delete(p_id)
        else:
            print(False)
    def clear_ivn_routine(self):
        self.ivn.setRowCount(0);
        some.ivn = []
            
    def query_ivn(self, query=''):
        self.ivn.setRowCount(0);
        self.ivn_tuple = sorted(some.display_ivn(query))
        self.ivn_length = len(self.ivn_tuple)
        self.ivn.setRowCount(self.ivn_length)
        for i in range(0,self.ivn_length):
            p_id = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][0]))
            qty = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][1]))
            unit = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][2]))
            rate = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][3]))
            desc = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][4]))
            self.ivn.setItem(i,0,p_id)
            self.ivn.setItem(i,1,qty)
            self.ivn.setItem(i,2,unit)
            self.ivn.setItem(i,3,rate)
            self.ivn.setItem(i,4,desc)
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(706, 538)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        #Search Bar
        self.ivn_search = QtGui.QLineEdit(self.centralwidget)
        self.ivn_search.setObjectName(_fromUtf8("ivn_search"))
        self.verticalLayout.addWidget(self.ivn_search)
        self.ivn_search.textChanged.connect(lambda x:self.query_ivn(self.ivn_search.text()))
        
        #Inventory table
        self.ivn = QtGui.QTableWidget(self.centralwidget)
        self.ivn.setObjectName(_fromUtf8("ivn"))
        self.ivn.setAlternatingRowColors(True)
        self.ivn.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.ivn.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ivn.setTextElideMode(QtCore.Qt.ElideRight)
        self.ivn.setGridStyle(QtCore.Qt.NoPen)
        #self.ivn.itemClicked.connect(self.append_to_ivn)
        self.ivn.resizeColumnsToContents()
        
        self.ivn_tuple = sorted(some.display_ivn())
        self.ivn_length = len(self.ivn_tuple)
        self.ivn.setRowCount(self.ivn_length)
        self.ivn.setColumnCount(5)
        self.ivn_table_headers = ['Product_id'+' '*20,'Qty','Unit','Rate/Unit','Description']# Ulta crude scaling technique
        self.ivn.setHorizontalHeaderLabels(self.ivn_table_headers)

        for i in range(0,self.ivn_length):
            p_id = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][0]))
            qty = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][1]))
            unit = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][2]))
            rate = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][3]))
            desc = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][4]))
            self.ivn.setItem(i,0,p_id)
            self.ivn.setItem(i,1,qty)
            self.ivn.setItem(i,2,unit)
            self.ivn.setItem(i,3,rate)
            self.ivn.setItem(i,4,desc)

        
        self.verticalLayout.addWidget(self.ivn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(98, 0, -1, -1)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        #Deleting a thing
        self.del_item = QtGui.QPushButton(self.centralwidget)
        self.del_item.setStyleSheet(_fromUtf8("color: \'dark red\'"))
        self.del_item.setObjectName(_fromUtf8("del_item"))
        self.del_item.clicked.connect(self.del_item_routine)
        
        self.gridLayout.addWidget(self.del_item, 2, 0, 1, 1)
        self.add_ivn = QtGui.QPushButton(self.centralwidget)
        self.add_ivn.setStyleSheet(_fromUtf8("color:\"green\""))
        self.add_ivn.setObjectName(_fromUtf8("add_ivn"))
        self.add_ivn.clicked.connect(self.add_new)
        self.gridLayout.addWidget(self.add_ivn, 0, 0, 1, 1)

        self.update_ivn = QtGui.QPushButton(self.centralwidget)
        self.update_ivn.setStyleSheet(_fromUtf8("color: rgb(85, 170, 255);"))
        self.update_ivn.setObjectName(_fromUtf8("update_ivn"))
        self.update_ivn.clicked.connect(self.update_ivn_routine)

        self.gridLayout.addWidget(self.update_ivn, 1, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.ret_login)
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.formLayout.setLayout(1, QtGui.QFormLayout.LabelRole, self.gridLayout)

        
        self.del_ivn = QtGui.QPushButton(self.centralwidget)
        self.del_ivn.setStyleSheet(_fromUtf8("color:\'red\';"))
        self.del_ivn.setObjectName(_fromUtf8("del_ivn"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.del_ivn)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:\"dark red\";"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 706, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "EMS | Inventory Management", None))
        self.label.setText(_translate("MainWindow", "Select the  product and modify then press update.", None))
        self.ivn_search.setPlaceholderText(_translate("MainWindow", "Search the inventory ....", None))
        self.label_3.setText(_translate("MainWindow", "Add / Modify new Products to Stock", None))
        self.del_item.setText(_translate("MainWindow", "Delete Item", None))
        self.add_ivn.setText(_translate("MainWindow", "Add New Item", None))
        self.update_ivn.setText(_translate("MainWindow", "Update Inventory", None))
        self.pushButton.setText(_translate("MainWindow", "Back", None))
        self.del_ivn.setText(_translate("MainWindow", "Delete all Inventory", None))
        self.label_2.setText(_translate("MainWindow", "Caution", None))

class inventory_management_window(QtGui.QMainWindow, Ui_MainWindow):
    ret = QtCore.pyqtSignal()
    def ret_login(self):
        self.ret.emit()
        self.close()
    def __init__(self, parent=None , user = ''):
        super(inventory_management_window, self).__init__(parent)
        USER = user
        self.setupUi(self)
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

