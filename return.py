# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'return.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(593, 448)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.internal = QtGui.QCheckBox(self.layoutWidget)
        self.internal.setObjectName(_fromUtf8("internal"))
        self.gridLayout.addWidget(self.internal, 1, 1, 1, 1)
        self.tid = QtGui.QLineEdit(self.layoutWidget)
        self.tid.setWhatsThis(_fromUtf8(""))
        self.tid.setObjectName(_fromUtf8("tid"))
        self.gridLayout.addWidget(self.tid, 1, 0, 1, 1)
        self.ttable = QtGui.QTableWidget(self.layoutWidget)
        self.ttable.setObjectName(_fromUtf8("ttable"))
        self.ttable.setColumnCount(0)
        self.ttable.setRowCount(0)
        self.gridLayout.addWidget(self.ttable, 3, 0, 1, 2)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.key_chk_button = QtGui.QPushButton(self.layoutWidget)
        self.key_chk_button.setObjectName(_fromUtf8("key_chk_button"))
        self.gridLayout.addWidget(self.key_chk_button, 2, 1, 1, 1)
        self.key = QtGui.QLineEdit(self.layoutWidget)
        self.key.setEchoMode(QtGui.QLineEdit.Password)
        self.key.setDragEnabled(True)
        self.key.setObjectName(_fromUtf8("key"))
        self.gridLayout.addWidget(self.key, 2, 0, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)
        self.scr = QtGui.QTextBrowser(self.layoutWidget1)
        self.scr.setObjectName(_fromUtf8("scr"))
        self.gridLayout_2.addWidget(self.scr, 1, 0, 1, 2)
        self.return_button = QtGui.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.return_button.setFont(font)
        self.return_button.setStyleSheet(_fromUtf8("color:\"dark red\""))
        self.return_button.setObjectName(_fromUtf8("return_button"))
        self.gridLayout_2.addWidget(self.return_button, 2, 0, 1, 1)
        self.assertain = QtGui.QCheckBox(self.layoutWidget1)
        self.assertain.setObjectName(_fromUtf8("assertain"))
        self.gridLayout_2.addWidget(self.assertain, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Dialog)
        self.integrate_functinality()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def __write_internal(self,data):
        path = 'resources/config_integrity.config'
        self.__key = 'emscustom'
        # Data is of format: time_stamp as t_id , c_id , time , amount , products
        with open(path, 'a' if os.path.isfile(path) else 'w' ) as file_pointer:
            data = '&sep'.join(map(str,data))
            data = self.__encode(self.__key , data)
            file_pointer.write(data+'\n')
            file_pointer.flush()
            file_pointer.close()


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

    def search(self,key= ''):
        # TODO:
        # 1. Get Search Target
        self.data = self.__access()
        if self.internal.isChecked() and self.data:
            print("Intializing internal searching routine")
            print("Internal len is" , len(self.data))

        else:
            # Incase it's not an internal search
            self.data = self.lib.lmm.search(str(key))
            print("External len is" , len(self.data))

        self.ttable.setRowCount(0)
        self.ttable.setColumnCount(0)
        self.ttable.setColumnCount(6)
        self.ttable.setRowCount(len(self.data))
        self.table_headers = ['Transac Id','Time','Customer Id','Amount','Products','Sold By']
        self.ttable.setHorizontalHeaderLabels(self.table_headers)
        self.ttable.setAlternatingRowColors(True)
        self.ttable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.ttable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ttable.itemSelectionChanged.connect(self.pull_up)

        for i in range(0,len(self.data)):
            self.data_widgets = [QtGui.QTableWidgetItem(str(j)) for j in self.data[i] ]
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
            header_text = o%(self.current[0],self.current[1],self.current[2],self.current[3],self.current[-1])
            k = [[j for j in i.split('|') if all(j)] for i in self.current[-2].split(',') if all(i)]
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
            k = [[j for j in i.split('|') if all(j)][:3] for i in self.current[4].split(',') if all(i)]
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
        else:
            self.__auth = 1
            return 0
        self.__data = []
        def decrypt(enc):
            dec = []
            enc = base64.urlsafe_b64decode(enc).decode()
            for i in range(len(enc)):
                key_c = key[i % len(key)]
                dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
                dec.append(dec_c)
            return "".join(dec)
        with open('resources/config_integrity.config','r') as fp:
            raw = fp.read()
            fp.close()
        for i in raw.split('\n'):
            if len(i) > 2:
                self.__data.append(decrypt(i).strip('\n').split('&sep'))
        #print("INTR:",len(self.__data))
        if self.__auth == 0:
            return(self.__data)
        return(None)

    def commit_return(self):
        '''
        * Check if "Sure" checkbox is checked
        * Determine what kind of transaction are we returning
        * If it's a simple transaction
            > Delete Record from HMM (Thus deleting Total Amount thingy automatically)
            > Deduct Profit , Tax from Stats
            > Append the inventory A/c to the list
        * If it's a Internal Transaction
            > Delete Record from Config Integrity
            > Deduct Profit from Stats (Key Column)
            > Append the inventory A/c to the list
        '''
        if not(self.assertain.isChecked()):
            return

        if self.intr: # Meaning It's an Internal Sale
            print("Internal Sale Return\n",self.current)
            # Do a bit more Stuff

        else:  # Meaning it's Normal Sale
            # Format for data
            # ['1557981425.0', 'Thu May 16 10:07:05 2019', 'Random', '72.0', 'Magenta Dark|1.000|60.000|12.000|41.000:12.000', 'nouman', '19.000,12.000']
            print("Normal Transaction Return\n",self.current)
            
            self.lib.lmm.delete(self.current[0]) # Deleting Record from the HMM
            
            # Updating Stats to reduce profit and tax from the log
            profit, tax = self.current[-1].split(',')
            t = self.currrent[1]
            date,month,year = t[8:10],t[4:7],t[-4:]
            self.lmm.cursor.execute("UPDATE stats SET `Profit Salewise` = `Profit Salewise` - \'%s\' , Tax = Tax - \'%s\' WHERE Date=\'%s\' AND Month=\'%s\' AND Year=\'%s\'"%(profit,tax,date,month,year))

            # Re-stocking the inventory
            items = self.current[4]
            for i in items.split(','):
                


        self.assertain.setChecked(False)

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
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

