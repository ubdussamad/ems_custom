# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ivm.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from ems_core import *
import time
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
    def mod_product_routine(self):
        if not(self.etax.isChecked() and self.eqty.isChecked()):
            return
        indexes = [i.row() for i in self.ivn.selectionModel().selectedRows()]
        if indexes:
            i = indexes[0]
            p_id = self.ivn.item(i,0).text()
            previous_qty = float(self.ivn.item(i,1).text())
        else:
            return

        qty = self.qty.text()
        rate = self.rate.text()
        tax = self.tax.text()
        brate = self.brate.text()
        data = (qty,rate,tax,brate)
        print(data)
        try:
            data = [float(i) for i in data]
        except Exception as err:
            print(err)
            self.label_7.setText(_translate("MainWindow", "Data not valid, select row again and try!", None))
            self.label_7.setStyleSheet(_fromUtf8("color:red;"))
            return
        data = data+[p_id]
        if data[0]:
            # Jos cahnge
            data[0] += previous_qty
            data = list(map(str,data))
            print(len(data))
            query = "UPDATE ivn SET Quantity = \"%s\", Unit_Rate = \"%s\" , Tax = \"%s\" , Stock_Price = \"%s\" WHERE P_id = \"%s\" "%tuple(map(str,data))
            self.update_stk(p_id,brate,qty)
        else:
            query = "UPDATE ivn SET Unit_Rate = \'%s\' , Tax = \'%s\' WHERE P_id = \'%s\' "%(data[1],data[2],data[4])
        some.imm.cursor.execute(query)
        some.imm.server.commit()
        self.etax.setChecked(False)
        self.eqty.setChecked(False)
        self.qty.clear()
        self.rate.clear()
        self.tax.clear()
        self.brate.clear()
        #setText("")

    def update_stk(self,p_id,rate,qty):
        modrate = some.imm.get_mod_rate(p_id)
        modrate = [i for i in modrate if i]
        if not modrate: #25:30,27:60
            #Get the value and create modrate
            modrate.append('%.3f:%.3f'%(float(rate),float(qty)))


        else:
            rate_list = [i.split(':')[0] for i in modrate]
            if rate in rate_list:
                index = rate_list.index(rate)
                tmp = modrate.pop(index)
                tmp = [ float(i)  for i in tmp.split(':') ]
                tmp[1] += float(qty)
                modrate.append(':'.join(map(str,tmp)))

            else:
                #Append is not in the rate list
                modrate.append('%.3f:%.3f'%(float(rate),float(qty)))
        modrate = [i for i in modrate if i]
        modrate = ','.join(modrate)
        some.imm.update(p_id,'mod_rate',[modrate])

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
            tax = self.ivn.item(i,5).text()
            hsn = self.ivn.item(i,6).text()
            sp = self.ivn.item(i,7).text()

            is_key = KEY in [i[0] for i in some.imm.return_item_names()]

            if not is_key:
                # New maal
                # P_id, Quantity, Unit, Unit_Rate, Description, Tax ,HSN/SAC, Stock_Price
                some.imm.append_ivn([KEY,qty,unit,rate,desc,tax,hsn,sp])
                self.update_stk(KEY,sp,qty)
            else:
                # No modrate required as it dosent changes anything
                data = (unit,desc,hsn,KEY)
                query = "UPDATE ivn SET Unit = \'%s\', Description = \'%s\' , `HSN/SAC` = \'%s\' WHERE P_id = \'%s\' "%data
                some.imm.cursor.execute(query)
                some.imm.server.commit()
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
        tax = QtGui.QTableWidgetItem('Tax')
        self.ivn.setItem(index,0,p_id)
        self.ivn.setItem(index,1,qty)
        self.ivn.setItem(index,2,unit)
        self.ivn.setItem(index,3,rate)
        self.ivn.setItem(index,4,desc)
        self.ivn.setItem(index,5,tax)

    def del_item_routine(self):
        #Just delete that itme form the database and update
        indexes = [i.row() for i in self.ivn.selectionModel().selectedRows()]
        if not indexes:
            return
        index = indexes[0]
        p_id = self.ivn.item(index,0).text()
        reply = QtGui.QMessageBox.question(self.centralwidget, 'Delete Item %s from Inventory??'%p_id.upper(), 
                 'Are you sure? \nIf you delete this item %s, all it\'s data will be lost!'%p_id.upper(), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            if indexes:
                self.ivn.removeRow(index)
                some.imm.delete(p_id)
            else:
                print(False)
        else:
            pass
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
            qty = QtGui.QTableWidgetItem('%.2f'%float(self.ivn_tuple[i][1]))
            unit = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][2]))
            rate = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][3]))
            desc = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][4]))
            tax = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][5]))
            hsn = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][6]))
            stkp = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][7]))
            self.ivn.setItem(i,0,p_id)
            self.ivn.setItem(i,1,qty)
            self.ivn.setItem(i,2,unit)
            self.ivn.setItem(i,3,rate)
            self.ivn.setItem(i,4,desc)
            self.ivn.setItem(i,5,tax)
            self.ivn.setItem(i,6,hsn)
            self.ivn.setItem(i,7,stkp)

    def update_fourm(self):
        indexes = [i.row() for i in self.ivn.selectionModel().selectedRows()]
        if indexes:
            i = indexes[0]
            p_id = self.ivn.item(i,0).text()
            qty = self.ivn.item(i,1).text()
            rate = self.ivn.item(i,3).text()
            brate = self.ivn.item(i,7).text()
            tax = self.ivn.item(i,5).text()

        self.qty.setPlaceholderText(_translate("MainWindow", qty, None))
        self.rate.setPlaceholderText(_translate("MainWindow", rate, None))
        self.brate.setPlaceholderText(_translate("MainWindow", brate, None))
        self.tax.setPlaceholderText(_translate("MainWindow", tax, None))
        self.label_7.setText(_translate("MainWindow", "Edit:    %s || Taxed Rate %.3f"% (p_id,(1+(float(tax)/100))*float(rate)), None))
        self.label_7.setStyleSheet(_fromUtf8("font-weight: bold;"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(706, 538)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        deleteShortcut = QtGui.QShortcut(QtGui.QKeySequence('Esc'),self.centralwidget)
        try:
            deleteShortcut.activated.connect(self.ret_login)
        except:
            print("Unit Testing Mode")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        #Search bar
        self.ivn_search = QtGui.QLineEdit(self.centralwidget)
        self.ivn_search.setObjectName(_fromUtf8("ivn_search"))
        self.ivn_search.textChanged.connect(lambda x:self.query_ivn(self.ivn_search.text()))
        self.verticalLayout.addWidget(self.ivn_search)

        # Ivn table
        self.ivn = QtGui.QTableWidget(self.centralwidget)
        self.ivn.setObjectName(_fromUtf8("ivn"))
        self.ivn.setAlternatingRowColors(True)
        self.ivn.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.ivn.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ivn.setTextElideMode(QtCore.Qt.ElideRight)
        self.ivn.setGridStyle(QtCore.Qt.NoPen)
        self.ivn.itemClicked.connect(self.update_fourm)
        self.ivn.resizeColumnsToContents()
        self.ivn_tuple = sorted(some.display_ivn()) # IVN Tuple
        self.ivn_length = len(self.ivn_tuple)
        self.ivn.setRowCount(self.ivn_length)
        self.ivn.setColumnCount(8)
        self.ivn_table_headers = ['Product'+' '*20,'Qty','Unit','Rate Untaxed',
        'Description','Tax','HSN/SAC','Bought Rate']# Ulta crude scaling technique
        self.ivn.setHorizontalHeaderLabels(self.ivn_table_headers)
        for i in range(0,self.ivn_length):
            p_id = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][0]))
            qty = QtGui.QTableWidgetItem('%.2f'%float(self.ivn_tuple[i][1]))
            unit = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][2]))
            rate = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][3]))
            desc = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][4]))
            tax = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][5]))
            hsn = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][6]))
            stkp = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][7]))
            self.ivn.setItem(i,0,p_id)
            self.ivn.setItem(i,1,qty)
            self.ivn.setItem(i,2,unit)
            self.ivn.setItem(i,3,rate)
            self.ivn.setItem(i,4,desc)
            self.ivn.setItem(i,5,tax)
            self.ivn.setItem(i,6,hsn)
            self.ivn.setItem(i,7,stkp)



        self.verticalLayout.addWidget(self.ivn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_3.addWidget(self.label_7)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 4, 1, 1)
        # Qty edit
        self.qty = QtGui.QLineEdit(self.centralwidget)
        self.qty.setObjectName(_fromUtf8("qty"))
        self.gridLayout.addWidget(self.qty, 1, 0, 1, 1)
        # Rate edit
        self.rate = QtGui.QLineEdit(self.centralwidget)
        self.rate.setObjectName(_fromUtf8("rate"))
        self.gridLayout.addWidget(self.rate, 1, 1, 1, 1)
        # Tax edit
        self.tax = QtGui.QLineEdit(self.centralwidget)
        self.tax.setObjectName(_fromUtf8("tax"))
        self.gridLayout.addWidget(self.tax, 1, 2, 1, 1)
        # Bought rate edit
        self.brate = QtGui.QLineEdit(self.centralwidget)
        self.brate.setObjectName(_fromUtf8("brate"))
        self.gridLayout.addWidget(self.brate, 1, 3, 1, 1)
        # Item modification button
        self.append = QtGui.QPushButton(self.centralwidget)
        self.append.setObjectName(_fromUtf8("append"))
        self.append.clicked.connect(self.mod_product_routine)
        self.gridLayout.addWidget(self.append, 1, 4, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        # Add inventory button
        self.add_ivn = QtGui.QPushButton(self.centralwidget)
        self.add_ivn.setStyleSheet(_fromUtf8("color:\"green\""))
        self.add_ivn.setObjectName(_fromUtf8("add_ivn"))
        self.add_ivn.clicked.connect(self.add_new)
        self.horizontalLayout.addWidget(self.add_ivn)

        # Update ivn button
        self.update_ivn = QtGui.QPushButton(self.centralwidget)
        self.update_ivn.setStyleSheet(_fromUtf8("color: rgb(85, 170, 255);"))
        self.update_ivn.setObjectName(_fromUtf8("update_ivn"))
        self.update_ivn.clicked.connect(self.update_ivn_routine)
        self.horizontalLayout.addWidget(self.update_ivn)


        # Delete item button
        self.del_item = QtGui.QPushButton(self.centralwidget)
        self.del_item.setStyleSheet(_fromUtf8("color: \'dark red\'"))
        self.del_item.setObjectName(_fromUtf8("del_item"))
        self.del_item.clicked.connect(self.del_item_routine)
        self.horizontalLayout.addWidget(self.del_item)

        # Back button
        self.back = QtGui.QPushButton(self.centralwidget)
        self.back.setObjectName(_fromUtf8("back"))
        try:
            self.back.clicked.connect(self.ret_login)
        except:
            pass
        self.horizontalLayout.addWidget(self.back)

        # Edit tac check box
        self.etax = QtGui.QCheckBox(self.centralwidget)
        self.etax.setObjectName(_fromUtf8("etax"))
        self.horizontalLayout.addWidget(self.etax)

        #c Edit qty check box
        self.eqty = QtGui.QCheckBox(self.centralwidget)
        self.eqty.setObjectName(_fromUtf8("eqty"))
        self.horizontalLayout.addWidget(self.eqty)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
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
        self.label_7.setText(_translate("MainWindow", "Modify Product", None))
        self.label_2.setText(_translate("MainWindow", "Add Qty (Kg)", None))
        self.label_3.setText(_translate("MainWindow", "Retail rate", None))
        self.label_4.setText(_translate("MainWindow", "Tax", None))
        self.label_5.setText(_translate("MainWindow", "Bought rate", None))
        self.label_6.setText(_translate("MainWindow", "Update Item", None))
        self.append.setText(_translate("MainWindow", "Update", None))
        self.add_ivn.setText(_translate("MainWindow", "Add New Item", None))
        self.update_ivn.setText(_translate("MainWindow", "Update", None))
        self.del_item.setText(_translate("MainWindow", "Delete", None))
        self.back.setText(_translate("MainWindow", "Back", None))
        self.etax.setText(_translate("MainWindow", "Edit Tax", None))
        self.eqty.setText(_translate("MainWindow", "Edit Qty", None))




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
else:
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
