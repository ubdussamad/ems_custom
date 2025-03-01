#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'routine_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from ems_core import *
from recipt_genrator import *
some = ems_core('ems','admin')
#from sys import platform
USER = 'admin'
import os


GRAND_TOTAL_AMOUNT_FOR_SESSION = 0
LAST_SALE_AMOUNT = 0
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

class Printer(QtGui.QDialog):
    def __init__(self):
        super(Printer, self).__init__()
        self.setWindowTitle('Recipt Preview')
        self.resize(1030, 629)
        self.editor = QtGui.QTextEdit(self)
        self.editor.textChanged.connect(self.handleTextChanged)
        self.buttonPrint = QtGui.QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QtGui.QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        self.handleOpen(os.path.abspath("recipt.html"))
        layout.addWidget(self.buttonPrint, 1, 0)
        layout.addWidget(self.buttonPreview, 1, 1)
        self.handleTextChanged()

    def handleOpen(self,path):
        if path:
            file = QtCore.QFile(path)
            if file.open(QtCore.QIODevice.ReadOnly):
                stream = QtCore.QTextStream(file)
                text = stream.readAll()
                info = QtCore.QFileInfo(path)
                if info.completeSuffix() == 'html':
                    self.editor.setHtml(text)
                else:
                    self.editor.setPlainText(text)
                file.close()

    def handlePrint(self):
        dialog = QtGui.QPrintDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.editor.document().print_(dialog.printer())

    def handlePreview(self):
        dialog = QtGui.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.editor.print_)
        dialog.exec_()

    def handleTextChanged(self):
        enable = not self.editor.document().isEmpty()
        self.buttonPrint.setEnabled(enable)
        self.buttonPreview.setEnabled(enable)


class Ui_EMS(object):
    def __get_ttype(self):
        self.__higher_priority = USER.lower() in ['noman','desk1','desk2','desk3'] #The user has auth
        self.__internal_sale = self.radioButton.isChecked() # The user wishes to proceed to internal sale
        return(self.__higher_priority and self.__internal_sale)

    def sanity_check(self):
        allRows = self.cart.rowCount()
        print("Checking Sanity!!")
        for row in range(0,allRows):
            print(self.cart.item(row,1).text())
            float(self.cart.item(row,3).text())

    def dummy(self):
        print("Iam a dummy!")
    def normal_checkout(self):
        try:
            self.sanity_check()
        except Exception as err:
            self.statusbar.showMessage("Invalid Values, Check Values in Cart!",2000)
            print(err)
            # This happens when user tries to enter invalid (non-numeric) rate or qty
            # values in Cart
            return
        global GRAND_TOTAL_AMOUNT_FOR_SESSION
        global LAST_SALE_AMOUNT
        if self.__get_ttype():
            print("Internal Sale")
        LAST_SALE_AMOUNT = float(self.total_amt.text())
        GRAND_TOTAL_AMOUNT_FOR_SESSION += float(self.total_amt.text())
        self.garbage.setText('%.2f'%GRAND_TOTAL_AMOUNT_FOR_SESSION+' / '+ str(LAST_SALE_AMOUNT))
        ret = some.check_out("current" , self.__get_ttype())
        self.clear_cart_routine()
        if ret != -1:
            self.print_recipt.setEnabled(True)
        else:
            self.statusbar.showMessage("Empty Cart, Please Fill Cart.",2000)
        self.query_ivn(self.ivn_sb.text())
    def borrow_checkout(self):
        try:
            self.sanity_check()
        except:
            self.statusbar.showMessage("Invalid Values, Check Values in Cart!",2000)
            # This happens when user tries to enter invalid (non-numeric) rate or qty
            # values in Cart
            return
        if self.__get_ttype():
            return
        global GRAND_TOTAL_AMOUNT_FOR_SESSION
        global LAST_SALE_AMOUNT
        LAST_SALE_AMOUNT = float(self.total_amt.text())
        GRAND_TOTAL_AMOUNT_FOR_SESSION += float(self.total_amt.text())
        self.garbage.setText(str(GRAND_TOTAL_AMOUNT_FOR_SESSION)+' / '+ str(LAST_SALE_AMOUNT))
        ret = some.check_out("borrow", self.__get_ttype())
        self.clear_cart_routine()
        if ret != -1:
            self.print_recipt.setEnabled(True)
        else:
            self.statusbar.showMessage("Empty Cart, Please Fill Cart.",2000)
        self.query_ivn(self.ivn_sb.text())

    def print_recipt_routine(self):
        recipt = genrate_recipt(some.recipt,self.__get_ttype())
        p = Printer()
        p.exec_()

    def customer_change(self):
        # change self.c_name
        customer = str(self.comboBox.currentText())
        self.c_name.setText(customer)
        self.clear_cart_routine()
        some.change_cid(customer)
        due = some.cmm.client_details(customer)[2]
        self.due_label.setText(str(due))
        self.total_amount = 0
        self.total_amt.setText('0.0')
        self.print_recipt.setEnabled(False)
        return
    def update_cart_with_amount( self, ttype = 0,warnings=False):  #Triggered by update button
        self.print_recipt.setEnabled(False)
        try:
            if not warnings:
                self.sanity_check()
            else:
                pass
        except:
            self.statusbar.showMessage("Invalid Cart Data!!",1000)
            self.total_amt.setText('0.0')
        if self.__get_ttype():
            self.due_self.setEnabled(False)
        else:
            self.due_self.setEnabled(True)
        if not any(some.cart):
            self.statusbar.showMessage('Empty or Invalid Cart data, Please Check Cart Data 0x1',2000)
            return
        rc,cc= self.cart.rowCount() , self.cart.columnCount()
        for i,j in zip(range(rc),range(cc)):
            some.cart = sorted(some.cart)
            p_id = self.cart.item(i,0).text()
            ivn_qty = some.display_ivn(p_id)
            ivn_qty  = ivn_qty[0][1]
            amt = self.cart.item(i,1).text()
            if float(ivn_qty) < float(amt):
                reply = QtGui.QMessageBox.question(self.centralwidget, "Inventory Contradiction", 
                 "Only %.2fKgs of %s is left in the inventory, Continue ?"%(float(ivn_qty),p_id), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    pass
                else:
                    amt = ivn_qty
                    self.statusbar.showMessage("Amount of %s exceeded the qty! Reducing Qty."%p_id,4000)

            rate = self.cart.item(i,3).text()
            # Updating internal cart tuple with the modified data
            some.cart[i][1] = amt
            some.cart[i][3] = rate

        self.total_amount = 0
        self.cart_tuple = sorted(some.display_cart()) ##Change
        self.cart_length = len(self.cart_tuple)
        self.cart.setRowCount(self.cart_length)
        self.cart.setColumnCount(6)
        self.cart_table_headers = ['Product_id','Qty','Unit','Rate/Unit','Tax Amount','Total Amount']# Ulta crude scaling technique
        self.cart.setHorizontalHeaderLabels(self.cart_table_headers)
        for i in range(0,self.cart_length):
            p_id = QtGui.QTableWidgetItem(str(self.cart_tuple[i][0]))
            qty = QtGui.QTableWidgetItem(str(self.cart_tuple[i][1]))
            unit = QtGui.QTableWidgetItem(str(self.cart_tuple[i][2]))
            rate = QtGui.QTableWidgetItem(str(self.cart_tuple[i][3]))
            tmp = float(self.cart_tuple[i][1])*float(self.cart_tuple[i][3])
            tax_percentage = float(self.cart_tuple[i][4])/100
            tax_amount = tmp*tax_percentage if not ttype else 0
            tmp += tax_amount
            self.total_amount += tmp
            amount = QtGui.QTableWidgetItem('%.2f'%tmp)
            tax = QtGui.QTableWidgetItem('%.2f'%tax_amount)
            self.cart.setItem(i,0,p_id)
            self.cart.setItem(i,1,qty)
            self.cart.setItem(i,2,unit)
            self.cart.setItem(i,3,rate)
            self.cart.setItem(i,4,tax)
            self.cart.setItem(i,5,amount)
        self.total_amt.setText('%.2f'%self.total_amount)
    def clear_cart_routine(self):
        self.print_recipt.setEnabled(False)
        self.total_amt.setText('0.0')
        self.cart.setRowCount(0);
        some.cart = []
    def delete_selected_cart_item(self):
        try:index = [i.row() for i in self.cart.selectionModel().selectedRows()][0]
        except:return
        self.cart.removeRow(index)
        some.cart = sorted(some.cart)
        del some.cart[index]
        self.update_cart_with_amount(self.__get_ttype())
    def query_ivn(self, query=''):
        self.ivn.setRowCount(0);
        key = self.ivn_search_key_select.currentText()
        self.ivn_tuple = sorted(some.display_ivn(query,key[0]))
        self.ivn_length = len(self.ivn_tuple)
        self.ivn.setRowCount(self.ivn_length)
        for i in range(0,self.ivn_length):
            p_id = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][0]))
            qty = QtGui.QTableWidgetItem('%.2f'%float(self.ivn_tuple[i][1]))
            unit = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][2]))
            rate = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][3]))
            desc = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][4]))
            tax = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][5]))
            hsc = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][6]))
            self.ivn.setItem(i,0,p_id)
            self.ivn.setItem(i,1,qty)
            self.ivn.setItem(i,2,unit)
            self.ivn.setItem(i,3,rate)
            self.ivn.setItem(i,4,desc)
            self.ivn.setItem(i,5,tax)
            self.ivn.setItem(i,6,hsc)
    def append_to_cart ( self , event= '' , dec='' , action=0 , ttype = 0):
        #print("Current User is: %s"%USER)
        # This function is called when something is to be added into the cart
        self.print_recipt.setEnabled(False)
        print(event.key())
        if action or event.key() == QtCore.Qt.Key_Return or event.key() == 16777221: #This updates the cart
            self.update_cart_with_amount(self.__get_ttype(),warnings=True) #Calling it for updating the cart everytime with amount
            self.total_amount = 0

            indexes = [i.row() for i in self.ivn.selectionModel().selectedRows()]
            item = self.ivn_tuple[indexes[0]] #This is the datum from the iventory

            #Protection from adding the same thing multiple times
            if item[0] in [self.cart.item(i,0).text() for i in range(self.cart.rowCount())]:
                return

            some.add_to_cart(item[0],'1',item[2],item[3],item[5]) #Adding the selected data to the main cart tuple

            self.cart_tuple = sorted(some.display_cart()) ##Change


            self.cart_length = len(self.cart_tuple)
            self.cart.setRowCount(self.cart_length)
            self.cart.setColumnCount(6)
            self.cart_table_headers = ['Product_id','Qty','Unit','Rate/Unit','Tax Amount','Amount']# Ulta crude scaling technique
            self.cart.setHorizontalHeaderLabels(self.cart_table_headers)

            for i in range(0,self.cart_length):
                p_id = QtGui.QTableWidgetItem(str(self.cart_tuple[i][0]))
                qty = QtGui.QTableWidgetItem('%.2f'%float(self.cart_tuple[i][1]))
                unit = QtGui.QTableWidgetItem(str(self.cart_tuple[i][2]))
                rate = QtGui.QTableWidgetItem(str(self.cart_tuple[i][3]))
                tmp = float(self.cart_tuple[i][1])*float(self.cart_tuple[i][3])

                tax_percentage = float(self.cart_tuple[i][4])/100
                tax_amount = tmp * tax_percentage if not ttype else 0
                self.total_amount += tmp + tax_amount if not ttype else 0 #Updated for kaccha
                tmp += tax_amount if not ttype else 0
                amount = QtGui.QTableWidgetItem('%.2f'%tmp)
                tax_amount = QtGui.QTableWidgetItem('%.2f'%tax_amount)
                self.cart.setItem(i,0,p_id)
                self.cart.setItem(i,1,qty)
                self.cart.setItem(i,2,unit)
                self.cart.setItem(i,3,rate)
                self.cart.setItem(i,4,tax_amount)
                self.cart.setItem(i,5,amount)
            self.total_amt.setText('%.2f'%self.total_amount)

        elif event.key() == QtCore.Qt.Key_R:
            print("R is pressed!")
        else:
            print("Something else is pressed!")

    def bought_rate(self):
        indexes = [i.row() for i in self.cart.selectionModel().selectedRows()]
        index = indexes[0]
        table = some.display_ivn()
        for i in table:
            if i[0]== self.cart.item(index,0).text():
                self.statusbar.showMessage("%s : Bought Rate: %d Rs/Kgs , Taxed Rate: %.2f Rs/Kgs"%\
                    (i[0],i[7],i[3]*(1+(i[5]/100))),3000)
                break
        #\
        #    (self.cart.item(index,0).text(),table[table.index(self.cart.item(index,0).text())][7]))
    def setupUi(self, EMS):
        EMS.setObjectName(_fromUtf8("EMS"))
        EMS.resize(1030, 629)
        EMS.setSizeIncrement(QtCore.QSize(19, 567))
        EMS.setWindowFilePath(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(EMS)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_6.addWidget(self.label)

        deleteShortcut = QtGui.QShortcut(QtGui.QKeySequence('Esc'),self.centralwidget)
        try:
            deleteShortcut.activated.connect(self.ret_login)
        except:
            print("Unit-Testing Mode")

        self.horizontalLayout6 = QtGui.QHBoxLayout()
        self.horizontalLayout6.setObjectName(_fromUtf8("Search Horizontal Layout"))
        
        self.ivn_sb = QtGui.QLineEdit(self.centralwidget)
        self.ivn_sb.setObjectName(_fromUtf8("ivn_sb"))
        self.ivn_search_key_select = QtGui.QComboBox(self.centralwidget)
        self.ivn_search_key_select.addItem('Product Name')
        self.ivn_search_key_select.addItem('HSN/SAC')
        self.horizontalLayout6.addWidget(self.ivn_sb)
        self.horizontalLayout6.addWidget(self.ivn_search_key_select)

        self.verticalLayout_6.addLayout(self.horizontalLayout6)


        self.ivn_sb.textChanged.connect(lambda x:self.query_ivn(self.ivn_sb.text()))

        self.ivn = QtGui.QTableWidget(self.centralwidget)
        self.ivn.setObjectName(_fromUtf8("ivn"))
        self.ivn.setColumnCount(7)
        self.ivn.setObjectName(_fromUtf8("ivn"))
        self.table_headers = ['Product_id'+' '*15,'Qty','Unit','Rate/Unit','Description','Tax','HSN/SAC']# Ulta crude scaling technique
        self.ivn.setHorizontalHeaderLabels(self.table_headers)
        self.ivn_tuple = some.display_ivn()
        self.ivn_length = len(self.ivn_tuple)
        self.ivn.setRowCount(self.ivn_length)
        self.ivn.setAlternatingRowColors(True)
        self.ivn.setSortingEnabled(True)
        self.ivn.horizontalHeader().setSortIndicatorShown(True)
        self.ivn.horizontalHeader().setStretchLastSection(True)
        self.ivn.verticalHeader().setSortIndicatorShown(True)
        self.ivn.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.ivn.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ivn.setTextElideMode(QtCore.Qt.ElideRight)
        self.ivn.setGridStyle(QtCore.Qt.NoPen)
        #self.ivn.itemClicked.connect(self.append_to_cart)
        self.ivn.resizeColumnsToContents()
        self.ivn.keyPressEvent = lambda x:self.append_to_cart(event=x,ttype=self.__get_ttype()) #This function adds selected item to the cart

        self.ivn_tuple = sorted(some.display_ivn())
        self.ivn_length = len(self.ivn_tuple)
        self.ivn.setRowCount(self.ivn_length)
        for i in range(0,self.ivn_length):
            p_id = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][0]))
            qty = QtGui.QTableWidgetItem('%.2f'%float(self.ivn_tuple[i][1]))
            unit = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][2]))
            rate = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][3]))
            desc = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][4]))
            tax = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][5]))
            hsc = QtGui.QTableWidgetItem(str(self.ivn_tuple[i][6]))
            self.ivn.setItem(i,0,p_id)
            self.ivn.setItem(i,1,qty)
            self.ivn.setItem(i,2,unit)
            self.ivn.setItem(i,3,rate)
            self.ivn.setItem(i,4,desc)
            self.ivn.setItem(i,5,tax)
            self.ivn.setItem(i,6,hsc)

        self.verticalLayout_6.addWidget(self.ivn)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.time_label = QtGui.QLabel(self.centralwidget)
        self.time_label.setObjectName(_fromUtf8("time_label"))
        self.horizontalLayout.addWidget(self.time_label)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)
        self.user_label = QtGui.QLabel(self.centralwidget)
        self.user_label.setObjectName(_fromUtf8("user_label"))
        self.horizontalLayout_2.addWidget(self.user_label)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_3.addWidget(self.label_9)
        self.garbage = QtGui.QLabel(self.centralwidget)
        self.garbage.setObjectName(_fromUtf8("garbage"))
        self.horizontalLayout_3.addWidget(self.garbage)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        #Customer Selection box
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.clear()
        for text in some.display_all_customers():
            self.comboBox.addItem(text[0])
        self.comboBox.currentIndexChanged.connect(self.customer_change)

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        #Customer Name Label
        self.c_name = QtGui.QLabel(self.centralwidget)
        self.c_name.setObjectName(_fromUtf8("c_name"))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.c_name.setFont(font)

        self.gridLayout.addWidget(self.c_name, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        #Due display label
        self.due_label = QtGui.QLabel(self.centralwidget)
        self.due_label.setObjectName(_fromUtf8("due_label"))
        self.gridLayout.addWidget(self.due_label, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        #Cart Routine
        self.cart = QtGui.QTableWidget(self.centralwidget) #CART ROUTINE
        self.cart.setObjectName(_fromUtf8("cart"))
        self.cart.setAlternatingRowColors(True)
        self.cart.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.cart.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.cart.setTextElideMode(QtCore.Qt.ElideRight)
        self.cart.setGridStyle(QtCore.Qt.NoPen)
        self.cart.itemClicked.connect(lambda x: self.update_cart_with_amount(self.__get_ttype()))
        self.cart.resizeColumnsToContents()
        self.cart.itemSelectionChanged.connect(self.bought_rate)
        #self.cart.keyPressEvent = self.append_to_cart


        self.verticalLayout.addWidget(self.cart)

        #Shortcuts testing utility
        deleteShortcut = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Delete),self.cart)
        deleteShortcut.activated.connect(self.delete_selected_cart_item)

        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.total_amt = QtGui.QLabel(self.centralwidget)
        self.total_amt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_amt.setObjectName(_fromUtf8("total_amt"))
        self.horizontalLayout_5.addWidget(self.total_amt)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))

        #Clear item button
        self.clear_item = QtGui.QPushButton(self.centralwidget)
        self.clear_item.setObjectName(_fromUtf8("clear_item"))
        self.clear_item.clicked.connect(self.delete_selected_cart_item)
        self.horizontalLayout_4.addWidget(self.clear_item)

        #Cart Clearing button
        self.clear_cart = QtGui.QPushButton(self.centralwidget)
        self.clear_cart.setObjectName(_fromUtf8("clear_cart"))
        self.clear_cart.clicked.connect(self.clear_cart_routine)
        self.horizontalLayout_4.addWidget(self.clear_cart)

        #Update  button
        self.update = QtGui.QPushButton(self.centralwidget)
        self.update.setObjectName(_fromUtf8("update"))
        self.update.clicked.connect(lambda x:self.update_cart_with_amount(self.__get_ttype()))


        self.horizontalLayout_4.addWidget(self.update)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout_2.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout_2.addWidget(self.radioButton, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        #Checkout button current
        self.chk_out = QtGui.QPushButton(self.centralwidget)
        self.chk_out.setObjectName(_fromUtf8("chk_out"))
        self.chk_out.clicked.connect(self.normal_checkout)

        self.verticalLayout_2.addWidget(self.chk_out)

        #Checkout DUE
        self.due_self = QtGui.QPushButton(self.centralwidget)
        self.due_self.setObjectName(_fromUtf8("due_self"))
        self.due_self.clicked.connect(self.borrow_checkout)

        self.verticalLayout_2.addWidget(self.due_self)
        self.print_recipt = QtGui.QPushButton(self.centralwidget)
        #Print Recipt Button
        self.print_recipt.setObjectName(_fromUtf8("print_recipt"))
        self.verticalLayout_2.addWidget(self.print_recipt)
        self.print_recipt.clicked.connect(self.print_recipt_routine)
        self.print_recipt.setEnabled(False)
        self.clr = QtGui.QPushButton(self.centralwidget)
        self.clr.setObjectName(_fromUtf8("clr"))
        self.clr.clicked.connect(self.clear_cart_routine)
        #########################################
        self.verticalLayout_2.addWidget(self.clr)
        self.exit = QtGui.QPushButton(self.centralwidget)
        self.exit.setObjectName(_fromUtf8("exit"))
        try:
            self.exit.clicked.connect(self.ret_login)
        except:
            pass
        self.verticalLayout_2.addWidget(self.exit)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 2, 1, 1)
        EMS.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(EMS)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        EMS.setStatusBar(self.statusbar)

        self.retranslateUi(EMS)
        QtCore.QMetaObject.connectSlotsByName(EMS)
    def retranslateUi(self, EMS):
        EMS.setWindowTitle(_translate("EMS", "EMS Custom | Routine Operations ", None))
        self.label.setText(_translate("EMS", "Search the Inventory", None))
        self.ivn_sb.setPlaceholderText(_translate("EMS", "Try Red...", None))
        self.label_7.setText(_translate("EMS", "Date:", None))
        self.time_label.setText(_translate("EMS",time.ctime(), None))
        self.label_8.setText(_translate("EMS", "User:", None))
        self.user_label.setText(_translate("EMS", "Admin", None))
        self.label_9.setText(_translate("EMS", "Total / Last Sale (Rupees):", None))
        self.garbage.setText(_translate("EMS", "0.0 / 0.0", None))
        self.label_2.setText(_translate("EMS", "Select Customer", None))
        self.label_3.setText(_translate("EMS", "Current Customer:", None))
        self.c_name.setText(_translate("EMS","Random", None))
        self.label_5.setText(_translate("EMS", "Payment Due:", None))
        self.due_label.setText(_translate("EMS", "0.0", None))
        self.label_6.setText(_translate("EMS", "Total", None))
        self.total_amt.setText(_translate("EMS", "0.0", None))
        self.clear_item.setText(_translate("EMS", "Clear Item", None))
        self.clear_cart.setText(_translate("EMS", "Clear Cart", None))
        self.update.setText(_translate("EMS", "Update", None))
        self.label_4.setText(_translate("EMS", "Rate", None))
        self.radioButton_2.setText(_translate("EMS", "Wholesale", None))
        self.radioButton.setText(_translate("EMS", "Retail", None))
        self.chk_out.setText(_translate("EMS", "Check Out", None))
        self.due_self.setText(_translate("EMS", "Due / Self", None))
        self.print_recipt.setText(_translate("EMS", "Print Recipt", None))
        self.clr.setText(_translate("EMS", "Clear", None))
        self.exit.setText(_translate("EMS", "Back", None))
        self.total_amount = 0


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EMS = QtGui.QMainWindow()
    ui = Ui_EMS()
    ui.setupUi(EMS)
    EMS.show()
    sys.exit(app.exec_())
else:
    class routine_window(QtGui.QMainWindow, Ui_EMS):
        closed = QtCore.pyqtSignal()
        ret = QtCore.pyqtSignal()
        def ret_login(self):
            self.ret.emit()
            self.close()
        def __init__(self, parent=None , user = ''):
            super(routine_window, self).__init__(parent)
            USER = user
            self.setupUi(self)

        @QtCore.pyqtSlot()
        def dummy(self):
            self.closed.emit()
            self.close()
        def show_decorator(self,user):
            global some
            global USER
            USER = user
            self.user_label.setText(_translate("EMS", user.capitalize(), None))
            some = ems_core('ems',user)
            self.comboBox.clear()
            for text in some.display_all_customers():
                self.comboBox.addItem(text[0])
            self.query_ivn()
            self.show()

