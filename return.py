# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'return.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import base64
try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)
'''
# TODO

* Make internal searching routine *
* Develop internal return routine
* Test everything
'''

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(593, 448)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.internal = QtWidgets.QCheckBox(self.layoutWidget)
        self.internal.setObjectName("internal")
        self.gridLayout.addWidget(self.internal, 1, 1, 1, 1)
        self.tid = QtWidgets.QLineEdit(self.layoutWidget)
        self.tid.setWhatsThis("")
        self.tid.setObjectName("tid")
        self.gridLayout.addWidget(self.tid, 1, 0, 1, 1)
        self.ttable = QtWidgets.QTableWidget(self.layoutWidget)
        self.ttable.setObjectName("ttable")
        self.ttable.setColumnCount(0)
        self.ttable.setRowCount(0)
        self.gridLayout.addWidget(self.ttable, 3, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.key_chk_button = QtWidgets.QPushButton(self.layoutWidget)
        self.key_chk_button.setObjectName("key_chk_button")
        self.gridLayout.addWidget(self.key_chk_button, 2, 1, 1, 1)
        self.key = QtWidgets.QLineEdit(self.layoutWidget)
        self.key.setEchoMode(QtWidgets.QLineEdit.Password)
        self.key.setDragEnabled(True)
        self.key.setObjectName("key")
        self.gridLayout.addWidget(self.key, 2, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)
        self.scr = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.scr.setObjectName("scr")
        self.gridLayout_2.addWidget(self.scr, 1, 0, 1, 2)
        self.return_button = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.return_button.setFont(font)
        self.return_button.setStyleSheet("color:\"dark red\"")
        self.return_button.setObjectName("return_button")
        self.gridLayout_2.addWidget(self.return_button, 2, 0, 1, 1)
        self.assertain = QtWidgets.QCheckBox(self.layoutWidget1)
        self.assertain.setObjectName("assertain")
        self.gridLayout_2.addWidget(self.assertain, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Dialog)
        self.integrate_functinality()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def integrate_functinality(self,user = 'admin'):
        from ems_core import ems_core
        self.lib = ems_core('ems',user)
        self.current = None
        self.__auth = 1
        self.intr = 0
        # Table Config
        self.ttable.setAlternatingRowColors(True)
        self.search()
        self.tid.textChanged.connect(lambda: self.search(self.tid.text()))
        self.return_button.clicked.connect(self.commit_return)

    def search(self,hkey= ''):
        # TODO:
        # 1. Get Search Target
        print("Executing Search Routine!")
        noaccess = self.__access()
        if self.internal.isChecked() and not noaccess:
            key = self.key.text()
            def decrypt(enc):
                dec = []
                enc = base64.urlsafe_b64decode(enc).decode()
                for i in range(len(enc)):
                    key_c = key[i % len(key)]
                    dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
                    dec.append(dec_c)
                return "".join(dec)

            self.lib.lmm.cursor.execute('SELECT checksum from config_checksum WHERE timestamp LIKE (?) LIMIT 3000',
            (hkey+'%',))
            rows = self.lib.lmm.cursor.fetchall()
            if not rows:
                self.ttable.setRowCount(0)
                return
            self.data = []
            print()
            for i in rows[0]:
                if len(i) > 2:
                    self.data.append(decrypt(i).strip('\n').split('&sep'))

        else:
            # Incase it's not an internal search
            self.data = self.lib.lmm.search(str(hkey))

        self.ttable.setRowCount(0)
        self.ttable.setColumnCount(0)
        self.ttable.setColumnCount(6)
        self.ttable.setRowCount(len(self.data))
        self.table_headers = ['Transac Id','Time','Customer Id','Amount','Products','Sold By']
        self.ttable.setHorizontalHeaderLabels(self.table_headers)
        self.ttable.setAlternatingRowColors(True)
        self.ttable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ttable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ttable.itemSelectionChanged.connect(self.pull_up)

        for i in range(0,len(self.data)):
            self.data_widgets = [QtWidgets.QTableWidgetItem(str(j)) for j in self.data[i] ]
            for j,k in enumerate(self.data_widgets):
                self.ttable.setItem(i,j,k)

    def pull_up(self):
        if not(self.internal.isChecked()) or self.__auth: # If the search is normal
            self.label_2.setText("Details for the transaction")
            self.intr = 0
            index = [i.row() for i in self.ttable.selectionModel().selectedRows()][0]
            self.current = [self.ttable.item(index,i).text() for  i in range(self.ttable.columnCount())]
            self.lib.lmm.cursor.execute('select pt from hmm where T_id = (?)',(self.current[0],))
            self.pt = self.lib.lmm.cursor.fetchall()
            self.current.append(self.pt[0][0])
            with open('resources/recipt_popup_format.html') as f:
                o = f.read()
            header_text = o%(self.current[0],self.current[1],self.current[2],self.current[3],self.current[-2])
            k = [[j for j in i.split('|') if all(j)][:-1] for i in self.current[-3].split(',') if all(i)]
            l = '<tr><td>'+'</td></tr><tr><td>'.join([ '</td><td>'.join(i) for i in k])+'</td></tr>'
            self.row_data = header_text+l+'</table></body></html>'
            self.scr.setHtml(self.row_data)
        else:
            self.intr = 1
            self.label_2.setText("Details for the INTERNAL transaction")
            index = [i.row() for i in self.ttable.selectionModel().selectedRows()][0]
            self.current = [self.ttable.item(index,i).text() for  i in range(self.ttable.columnCount()) if self.ttable.item(index,i)]
            with open('resources/recipt_popup_format2.html') as f:
                o = f.read()
            header_text = o%(self.current[0],self.current[2],self.current[1],self.current[3])
            k = [[j for j in i.split('|') if all(j)] for i in self.current[4].split(',') if all(i)]
            l = '<tr><td>'+'</td></tr><tr><td>'.join([ '</td><td>'.join(i) for i in k])+'</td></tr>'
            self.row_data = header_text+l+'</table></body></html>'
            self.scr.setHtml(self.row_data)

    def __access ( self ):
        import hashlib,base64
        key = self.key.text()
        self.__key_hash = '04a11c0ac3d39a7d59c2ee0cdcdcabb4' #emscustom
        key_md5 = hashlib.md5(key.encode('utf-8')).hexdigest()
        if key_md5 == self.__key_hash:
            print("Access")
            self.__auth = 0
            return(0)
        else:
            self.__auth = 1
            return 1

    def commit_return(self):
        '''
        * Check if "Sure" checkbox is checked
        * Determine what kind of transaction are we returning
        * If it's a simple transaction
            > Delete Record from HMM (Thus deleting Total Amount thingy automatically)
            > Deduct Profit , Tax from Stats
            > Update CMM for customer net transaction Deduction
            > Append the inventory A/c to the list
        * If it's a Internal Transaction
            > Delete Record from Config Integrity
            > Not Sure  if an internal transaction logs the amount in CMM or not
            > Deduct Profit from Stats (Key Column)
            > Append the inventory A/c to the list
        '''
        if not(self.assertain.isChecked()):
            return

        if self.intr: # Meaning It's an Internal Sale
            '''
            TODO:
            * Gather the whole list of internal sales
            * Delete the specific Transaction from that list
            * Taylor the writing algorithm to write all the lines togather form a list
            * Write Deduct Profit from Stats
            * Do the Inventory Restocking magic
            '''

            #print("Internal Sale Return\n",self.current)

            # Deleting the transaction details from the list
            self.lib.lmm.cursor.execute('delete from config_checksum where timestamp = (?)',(self.current[0],))
            self.lib.lmm.server.commit()


            # Reducing the profit from that key thing
            profit, tax = self.current[-1].split(',')
            print("Profit %f and tax %f"%(float(profit) , float(tax) ))
            t = self.current[2]
            print("The t is : %s"%t)
            date,month,year = t[8:10],t[4:7],t[-4:]
            print(date,month,year)
            self.lib.lmm.cursor.execute("UPDATE stats SET `key` = `key` - \'%s\' WHERE Date=\'%s\' AND Month=\'%s\' AND Year=\'%s\'"%(profit,date,month,year))
            self.lib.lmm.server.commit()

        else:  # Meaning it's Normal Sale
            # Format for data
            # ['1557981425.0', 'Thu May 16 10:07:05 2019', 'Random', '72.0', 'Magenta Dark|1.000|60.000|12.000|41.000:12.000', 'nouman', '19.000,12.000']
            print("Normal Transaction Return\n",self.current)
            print("Self.current is: \n",self.current)
            self.lib.lmm.delete(self.current[0]) # Deleting Record from the HMM

            # Handles Updating CMM for the deduction
            customer_id = self.lib.cmm.client_to_id(self.current[2])
            self.lib.cmm.cursor.execute('UPDATE cmm SET Net_Transactions = Net_Transactions - (?) WHERE C_id = (?)',
                                                    (self.current[3] , customer_id ))
            self.lib.cmm.server.commit()
            
            # Updating Stats to reduce profit and tax from the log
            
            profit, tax = self.current[-1].split(',')
            t = self.current[1]
            date,month,year = t[8:10],t[4:7],t[-4:]
            self.lib.lmm.cursor.execute("UPDATE stats SET `Profit Salewise` = `Profit Salewise` - \'%s\' , Tax = Tax - \'%s\' WHERE Date=\'%s\' AND Month=\'%s\' AND Year=\'%s\'"%(profit,tax,date,month,year))
            self.lib.lmm.server.commit()

        


        items = self.current[4]
        for i in items.split(','): # Here i is a specific item
            print("Processing:",i,'\n')
            i = i.split('|')
            pid = i[0]
            modrate = i[4].split('%20')
            qty = float(i[1])
            self.lib.lmm.cursor.execute("UPDATE ivn SET Quantity = Quantity + (?) WHERE P_id = (?)",(qty,pid))
            self.lib.lmm.server.commit()
            modrate = { float(i.split(':')[0]):float(i.split(':')[1]) for i in modrate if i}
            last_mod_rate = 0
            for i in modrate: # "i" is price here
                if modrate[i] >= qty: #If partial Stock > Demand
                    print("Partial Stock Quantity Fills %s : Qty: %.1f , PStq: %.1f "%(pid,qty,modrate[i]))
                    self.update_stk(pid, i, qty)
                    qty = 0
                    break
                else:
                    print("Partial Stock is less than %s , Qty:%.1f , PStq: %.1f"%(pid,qty,modrate[i]),'\n')
                    self.update_stk(pid, i, modrate[i])
                    last_mod_rate = i
                    qty -= modrate[i]
            if qty > 0.001:
                self.update_stk(pid, last_mod_rate, qty)
        # Re-stocking the inventory us same for both the cases given nothing bad happens the inventory will be 
        # Restocked


        print("Done!")
        self.assertain.setChecked(False)
        self.scr.setHtml("<h1 align='center'> Item Return Sucesss!! </h1>")
        self.current = []
        self.search()

    def update_stk(self,p_id,rate,qty):
        modrate = self.lib.imm.get_mod_rate(p_id)
        modrate = { float(i.split(':')[0]):float(i.split(':')[1]) for i in modrate if i}
        qty,rate = float(qty),float(rate)
        if not modrate: # {25:30,27:60} There isn't a modrate Log
            #Get the value and create modrate
            #modrate.append('%.3f:%.3f'%(float(rate),float(qty)))
            modrate[rate] = qty

        else:
            # The modrates are present
            '''
             > Check if the same mod rate is present and increment
             > Else add the new mod rate and be happy with it
             '''
            try: # If this dosent fails then it means whe have 
                val = modrate[rate]
                modrate[rate] += qty
            except:
                # The rate value ins't present in the dict
                modrate[rate] = qty

        modrate = [ ':'.join(map(str,[i,modrate[i]])) for i in modrate.keys() ]
        modrate = ','.join(modrate)
        self.lib.imm.update(p_id,'mod_rate',[modrate])

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "EMS | Return Facility", None))
        self.internal.setText(_translate("Dialog", "Internal", None))
        self.tid.setPlaceholderText(_translate("Dialog", "Enter Transaction Id", None))
        self.label.setText(_translate("Dialog", "Enter Transaction Id:", None))
        self.key_chk_button.setText(_translate("Dialog", "Key", None))
        self.key.setPlaceholderText(_translate("Dialog", "Search By key (*Advance)", None))
        self.label_2.setText(_translate("Dialog", "Details for the transaction", None))
        self.return_button.setText(_translate("Dialog", "Register Return", None))
        self.assertain.setText(_translate("Dialog", "Sure???", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

