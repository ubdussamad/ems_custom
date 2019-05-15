import base64,hashlib
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
        self.handleOpen(os.path.abspath("recipt_dup.html"))
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

class detail_diag(QtGui.QDialog):
    def __init__(self,d, parent=None):
        super(detail_diag, self).__init__(parent)
        self.setWindowTitle(_translate("MainWindow", "Details for Tid: %s"%(d[0],), None))
        #Format
        #['1551352557.0', 'Thu Feb 28 16:45:57 2019', 'Random', '544.5799999999999', 'GREEN_NORMAL|10.000|25.000|13.000|,RED_NORMAL|9.750|24.000|12.000|']
        with open('resources/recipt_popup_format2.html') as f:
            o = f.read()
        header_text = o%(d[0],d[2],d[1],d[3])#,d[-1])
        k = [[j for j in i.split('|') if all(j)][:3] for i in d[-1].split(',') if all(i)]
        l = '<tr><td>'+'</td></tr><tr><td>'.join([ '</td><td>'.join(i) for i in k])+'</td></tr>'
        self.textBrowser = QtGui.QTextBrowser(self)
        self.row_data = header_text+l+'</table></body></html>'
        self.textBrowser.setHtml(self.row_data)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.textBrowser)
        self.print_button = QtGui.QPushButton(self)
        self.print_button.setText("Print Recipt")
        self.verticalLayout.addWidget(self.print_button)
        self.print_button.clicked.connect(self.print_duplicate_recipt)
    def print_duplicate_recipt(self):
        with open('recipt_dup.html','w',encoding='utf-8') as fobj:
            fobj.write(self.row_data)
        p = Printer()
        p.exec_()


class Ui_MainWindow(object):
    def __init__ ( self ):
        self.__auth = 1
        self.__data = []


    def pullup(self):
        row = []
        for i in self.history.selectionModel().selectedIndexes():
            row.append(self.history.item(i.row(), i.column()).text())
        z = detail_diag(row)
        z.exec_()

    def __access(self):
        key = self.key.text()
        self.__key_hash = '04a11c0ac3d39a7d59c2ee0cdcdcabb4' #emscustom
        key_md5 = hashlib.md5(key.encode('utf-8')).hexdigest()
        if key_md5 == self.__key_hash:
            self.__auth = 0
            #print("Access")
        else:
            self.__auth = 1
            self.update_routine()
            return
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
        return
    def update_routine ( self ):
        # Check auth
        # Update the table with Data
        # Pick data from table and sum
        if self.__auth:
            self.history.setRowCount(0);
            self.amount.setText('')
            self.total.setText('')
            return
        self.update_history()
        self.year.clear()
        years = set([ i[2][-4:] for i in self.__data ])
        months = set([ i[2][3:7] for i in self.__data ])
        for i in years:
            self.year.addItem(i)
        self.month.clear()
        for i in months:
            self.month.addItem(i)
        self.calc_total()

    def calc_total ( self ):
        year = self.year.currentText()
        month = self.month.currentText()
        data = [ float(i[3]) if (year in i[2] and month in i[2]) else 0.0 for i in self.__data ]
        total = sum(data)
        self.amount.setText('%.2f'%total)
        self.total.setText('%.2f'%total)
        return
    def update_history(self,key = '' ,kt = 0):
        # kt = 0 (for t_id) , 1 (for customer)
        # Trim the history list here

        def floatify(x):
            try:
                return(str(float(x)))
            except:
                return(x)

        if self.__auth:
            return
        self.history_tuple = sorted(self.__data,key=lambda x:x[0])

        if key:
            if kt==1:
                key = some.cmm.c2id(key.lower())
                
                try:
                    key=key[0][0]
                except:
                    self.history.setRowCount(0)
                    return
            tmp = []
            for i in self.history_tuple:
                if floatify(i[kt]).lower().startswith(str(key).lower()):
                    tmp.append(i)
            self.history_tuple = tmp


        self.history.setColumnCount(0)
        self.history.setRowCount(0)
        self.history.setColumnCount(5)
        self.history_length = len(self.history_tuple)
        self.history.setRowCount(self.history_length)
        self.table_headers = ['Transac Id','Customer Id','Time','Amount','Products']
        self.history.setHorizontalHeaderLabels(self.table_headers)

        self.history.setAlternatingRowColors(True)
        self.history.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.history.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.history.setTextElideMode(QtCore.Qt.ElideRight)
        self.history.setGridStyle(QtCore.Qt.NoPen)
        self.history.resizeColumnsToContents()

        for i in range(0,self.history_length):
            try:
                p_id = QtGui.QTableWidgetItem(str(self.history_tuple[i][0]))
                qty = QtGui.QTableWidgetItem(some.id2c(str(self.history_tuple[i][1])))
                unit = QtGui.QTableWidgetItem(str(self.history_tuple[i][2]))
                rate = QtGui.QTableWidgetItem(str(self.history_tuple[i][3]))
                desc = QtGui.QTableWidgetItem(str(self.history_tuple[i][4]))
                self.history.setItem(i,0,p_id)
                self.history.setItem(i,1,qty)
                self.history.setItem(i,2,unit)
                self.history.setItem(i,3,rate)
                self.history.setItem(i,4,desc)
            except:
                self.history.setRowCount(0)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        #Search by date
        self.date = QtGui.QLineEdit(self.centralwidget)
        self.date.setObjectName(_fromUtf8("date"))
        self.date.textChanged.connect(lambda x:self.update_history(self.date.text(),0))
        self.gridLayout.addWidget(self.date, 0, 0, 1, 1)

        #Search by customer name
        self.cname = QtGui.QLineEdit(self.centralwidget)
        self.cname.setObjectName(_fromUtf8("cname"))
        self.cname.textChanged.connect(lambda x:self.update_history(self.cname.text(),1))
        self.gridLayout.addWidget(self.cname, 0, 1, 1, 1)
        #History Table
        self.history = QtGui.QTableWidget(self.centralwidget)
        self.history.setObjectName(_fromUtf8("history"))
        self.history.setColumnCount(0)
        self.history.setRowCount(0)
        self.history.setSortingEnabled(True)
        self.history.horizontalHeader().setSortIndicatorShown(True)
        self.history.horizontalHeader().setStretchLastSection(True)
        self.history.verticalHeader().setSortIndicatorShown(True)
        self.history.doubleClicked.connect(self.pullup)
        self.gridLayout.addWidget(self.history, 1, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        # Select Month
        self.month = QtGui.QComboBox(self.centralwidget)
        self.month.setObjectName(_fromUtf8("month"))
        self.month.currentIndexChanged.connect(self.calc_total)
        self.horizontalLayout.addWidget(self.month)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        # Select Year
        self.year = QtGui.QComboBox(self.centralwidget)
        self.year.setObjectName(_fromUtf8("year"))
        self.year.currentIndexChanged.connect(self.calc_total)
        self.horizontalLayout.addWidget(self.year)
        # Update button
        self.update = QtGui.QPushButton(self.centralwidget)
        self.update.setObjectName(_fromUtf8("update"))
        self.update.clicked.connect(self.update_routine)
        self.horizontalLayout.addWidget(self.update)
        # Exit Button
        self.back = QtGui.QPushButton(self.centralwidget)
        self.back.setObjectName(_fromUtf8("back"))
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
        #This is key
        self.key = QtGui.QLineEdit(self.centralwidget)
        self.key.setMaximumSize(QtCore.QSize(316, 16777215))
        self.key.setEchoMode(QtGui.QLineEdit.Password)
        self.key.setObjectName(_fromUtf8("key"))
        self.key.textChanged.connect(self.__access)
        self.horizontalLayout_2.addWidget(self.key)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_2.addWidget(self.label_9)
        # Total label
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
        MainWindow.setWindowTitle(_translate("MainWindow", "EMS | Internal Sales Record", None))
        self.date.setPlaceholderText(_translate("MainWindow", "Search  with date", None))
        self.cname.setPlaceholderText(_translate("MainWindow", "Search with customer name", None))
        self.label_4.setText(_translate("MainWindow", "Total Sale For the month:", None))
        self.label_5.setText(_translate("MainWindow", "        and Year:", None))
        self.update.setText(_translate("MainWindow", "Update", None))
        self.back.setText(_translate("MainWindow", "Back", None))
        self.label_6.setText(_translate("MainWindow", "Amount:", None))
        self.amount.setText(_translate("MainWindow", "0.0", None))
        self.label_8.setText(_translate("MainWindow", "Rupees", None))
        self.key.setPlaceholderText(_translate("MainWindow", "Enter Search Key", None))
        self.label_9.setText(_translate("MainWindow", "Total:", None))
        self.total.setText(_translate("MainWindow", "0.0", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
