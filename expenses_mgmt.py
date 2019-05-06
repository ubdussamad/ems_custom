# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Log.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time
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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(705, 540)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.description = QtGui.QLineEdit(self.layoutWidget)
        self.description.setMinimumSize(QtCore.QSize(300, 0))
        self.description.setObjectName(_fromUtf8("description"))
        self.gridLayout_2.addWidget(self.description, 1, 3, 1, 2)
        self.search = QtGui.QLineEdit(self.layoutWidget)
        self.search.setObjectName(_fromUtf8("search"))
        self.gridLayout_2.addWidget(self.search, 3, 0, 1, 4)
        self.add_for = QtGui.QComboBox(self.layoutWidget)
        self.add_for.setMaxVisibleItems(10)
        self.add_for.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.add_for.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.add_for.setObjectName(_fromUtf8("add_for"))
        self.gridLayout_2.addWidget(self.add_for, 1, 1, 1, 2)
        self.qtype = QtGui.QComboBox(self.layoutWidget)
        self.qtype.setObjectName(_fromUtf8("qtype"))
        self.gridLayout_2.addWidget(self.qtype, 3, 4, 1, 1)
        self.log_button = QtGui.QPushButton(self.layoutWidget)
        self.log_button.setObjectName(_fromUtf8("log_button"))
        self.gridLayout_2.addWidget(self.log_button, 2, 2, 1, 3)
        self.red_exp = QtGui.QCheckBox(self.layoutWidget)
        self.red_exp.setObjectName(_fromUtf8("red_exp"))
        self.gridLayout_2.addWidget(self.red_exp, 2, 0, 1, 2)
        self.amount_add = QtGui.QLineEdit(self.layoutWidget)
        self.amount_add.setObjectName(_fromUtf8("amount_add"))
        self.gridLayout_2.addWidget(self.amount_add, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.log = QtGui.QTableWidget(self.layoutWidget)
        self.log.setObjectName(_fromUtf8("log"))
        self.log.setColumnCount(0)
        self.log.setRowCount(0)
        self.log.horizontalHeader().setSortIndicatorShown(True)
        self.log.horizontalHeader().setStretchLastSection(True)
        self.log.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout_2.addWidget(self.log)
        self.update_all = QtGui.QPushButton(self.layoutWidget)
        self.update_all.setObjectName(_fromUtf8("update_all"))
        self.verticalLayout_2.addWidget(self.update_all)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.add_new = QtGui.QLineEdit(self.layoutWidget1)
        self.add_new.setObjectName(_fromUtf8("add_new"))
        self.verticalLayout.addWidget(self.add_new)
        self.add_new_push = QtGui.QPushButton(self.layoutWidget1)
        self.add_new_push.setObjectName(_fromUtf8("add_new_push"))
        self.verticalLayout.addWidget(self.add_new_push)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.name = QtGui.QLabel(self.layoutWidget1)
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.amount = QtGui.QLabel(self.layoutWidget1)
        self.amount.setObjectName(_fromUtf8("amount"))
        self.gridLayout.addWidget(self.amount, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.name_search = QtGui.QLineEdit(self.layoutWidget1)
        self.name_search.setObjectName(_fromUtf8("name_search"))
        self.verticalLayout.addWidget(self.name_search)
        self.name_table = QtGui.QTableWidget(self.layoutWidget1)
        self.name_table.setWordWrap(False)
        self.name_table.setObjectName(_fromUtf8("name_table"))
        self.name_table.setColumnCount(0)
        self.name_table.setRowCount(0)
        self.name_table.horizontalHeader().setCascadingSectionResizes(False)
        self.name_table.horizontalHeader().setStretchLastSection(True)
        self.name_table.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.name_table)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionPrint_Current_Table = QtGui.QAction(MainWindow)
        self.actionPrint_Current_Table.setObjectName(_fromUtf8("actionPrint_Current_Table"))
        self.actionBack = QtGui.QAction(MainWindow)
        self.actionBack.setObjectName(_fromUtf8("actionBack"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint_Current_Table)
        self.menuFile.addAction(self.actionBack)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.integrate_functionality()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "EMS | Expense Maintainance Sheets", None))
        self.description.setPlaceholderText(_translate("MainWindow", "Reason", None))
        self.search.setPlaceholderText(_translate("MainWindow", "Search by", None))
        self.log_button.setText(_translate("MainWindow", "Log", None))
        self.red_exp.setText(_translate("MainWindow", "Reduce Expense", None))
        self.amount_add.setPlaceholderText(_translate("MainWindow", "Amount (Rs)", None))
        self.label.setText(_translate("MainWindow", "ADD Expense", None))
        self.log.setSortingEnabled(True)
        self.update_all.setText(_translate("MainWindow", "Update", None))
        self.label_2.setText(_translate("MainWindow", "Add New Expense Model", None))
        self.add_new.setPlaceholderText(_translate("MainWindow", "Enter Model Name", None))
        self.add_new_push.setText(_translate("MainWindow", "Add", None))
        self.label_3.setText(_translate("MainWindow", "Name", None))
        self.label_4.setText(_translate("MainWindow", "Amount", None))
        self.name.setText(_translate("MainWindow", "Random", None))
        self.amount.setText(_translate("MainWindow", "0.0", None))
        self.name_search.setPlaceholderText(_translate("MainWindow", "Search By Model Name . .  .", None))
        self.name_table.setSortingEnabled(True)
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionPrint_Current_Table.setText(_translate("MainWindow", "Print Current Table", None))
        self.actionPrint_Current_Table.setShortcut(_translate("MainWindow", "Ctrl+P", None))
        self.actionBack.setText(_translate("MainWindow", "Back", None))
        self.actionBack.setShortcut(_translate("MainWindow", "Esc", None))

    def integrate_functionality(self):
        #amount_add (line edit)
        #red_exp (checkbox)
        #add_for (model) (combobox)
        #description (line edit)
        #search (main line edit)
        #log (qtable)
        #log_button
        #qtype (combobox)
        #add_new (line_edit) (model)
        #add_new_push (model)
        #model name (label)
        #amount (label)
        #name_search (line edit) (model)
        #name_table (qtable)
        #update_all (button)
        from ems_core import ems_core
        import time
        self.core = ems_core('ems','admin')

        # Main table things
        self.core.cmm.cursor.execute('select * from expenses')
        self.log_data = self.core.cmm.cursor.fetchall()
        if any(self.log_data):
            self.log.setRowCount(len(self.log_data))
            self.log.setColumnCount(len(self.log_data[0]))
            self.log_headers = ['Model_Name' , 'Time' , 'Amount' ,'Reason']
            self.log.setHorizontalHeaderLabels(self.log_headers)
            for i in range(0,len(self.log_data)):
                data_widgets = [QtGui.QTableWidgetItem(str(j)) for j in self.log_data[i] ]
                for j,k in enumerate(data_widgets):
                    self.log.setItem(i,j,k)

            # Main SearchBox Things
            for i in self.log_headers:
                self.qtype.addItem(i)
            self.search.textChanged.connect(self.search_routine)
            self.name_search.textChanged.connect(self.name_search_routine)
            self.qtype.currentIndexChanged.connect(self.update)


        # Update button, Add button, Log button, Checkbox
        self.update_all.clicked.connect(self.update)
        self.log_button.clicked.connect(self.log_routine)
        self.add_new_push.clicked.connect(self.add_model)
        self.red_exp.toggled.connect(self.update)


        # Model Table things
        self.core.cmm.cursor.execute('select * from expensemodels')
        self.models_data = self.core.cmm.cursor.fetchall()
        self.name_table.setRowCount(len(self.models_data))
        self.name_table.setColumnCount(len(self.models_data[0]))
        self.name_table.setHorizontalHeaderLabels(['Model_Name'])
        self.name_table.itemSelectionChanged.connect(self.update_details)
        self.name_table.itemActivated.connect(self.foo)
        for i in range(0,len(self.models_data)):
            data_widgets = [QtGui.QTableWidgetItem(str(j)) for j in self.models_data[i] ]
            for j,k in enumerate(data_widgets):
                self.name_table.setItem(i,j,k)
        self.update()

    def update_details(self):
        indexes = [i.row() for i in self.name_table.selectionModel().selectedRows()]
        index = indexes[0]
        self.name.setText(self.name_table.item(index,0).text() )
        self.core.cmm.cursor.execute('select Amount from expenses where Model_Name = (?)',(self.name_table.item(index,0).text(),))
        amount = self.core.cmm.cursor.fetchall()
        self.amount.setText(str(sum([i[0] for i in amount])))

    def add_model(self):
        print("Me work")
        if not self.add_new.text():
            self.statusbar.showMessage("Enter the model name to Add" ,2000)
            return
        self.core.cmm.cursor.execute("insert into expensemodels (Name) values (?)",(self.add_new.text(),))
        self.core.cmm.server.commit()
        self.update()
    def foo(self):
        print("Yayyyyyy!")

    def search_routine(self):
        self.search.text()
        query = "select * from expenses where %s like \'%s\'"%(self.qtype.currentText(),self.search.text()+'%')
        self.core.cmm.cursor.execute(query)
        self.log_data = self.core.cmm.cursor.fetchall()
        if not self.log_data:
            self.statusbar.showMessage("No Results",1000)
        self.log.setRowCount(0)
        self.log.setRowCount(len(self.log_data))
        self.log.setColumnCount(len(self.log_data[0]))
        self.log_headers = ['Model_Name' , 'Time' , 'Amount' ,'Reason']
        self.log.setHorizontalHeaderLabels(self.log_headers)
        for i in range(0,len(self.log_data)):
            data_widgets = [QtGui.QTableWidgetItem(str(j)) for j in self.log_data[i] ]
            for j,k in enumerate(data_widgets):
                self.log.setItem(i,j,k)

    def update(self):
        # Placeholders and labels
        self.search.setPlaceholderText("Search by %s"%self.qtype.currentText())
        self.add_new.clear()
        if self.red_exp.isChecked():
            self.label.setText("REDUCE Expense")
        else:
            self.label.setText("ADD Expense")

        # Model Names
        self.core.cmm.cursor.execute('select * from expensemodels')
        self.models_data = self.core.cmm.cursor.fetchall()
        self.name_table.setRowCount(0)
        self.name_table.setRowCount(len(self.models_data))
        for i in range(0,len(self.models_data)):
            data_widgets = [QtGui.QTableWidgetItem(str(j)) for j in self.models_data[i] ]
            for j,k in enumerate(data_widgets):
                self.name_table.setItem(i,j,k)
        self.add_for.clear()
        for i in self.models_data:
            self.add_for.addItem(i[0])

        # Main table update
        self.search.clear()
        self.search_routine()
        return

    def log_routine(self):
        try:
            value = float(self.amount_add.text())
            if self.red_exp.isChecked():
                if value<0:
                    pass
                else:
                    value*=-1
            value = str(value)
        except:
            self.statusbar.showMessage("Please Enter Vaild Data!!" , 2000)
            return
        self.core.cmm.cursor.execute("insert into expenses (Model_Name, Time, Amount, Reason) values (?,?,?,?)",
            (self.add_for.currentText(),time.ctime(),value,self.description.text()) )
        self.core.cmm.server.commit()

        t = time.ctime()
        date,month,year = t[8:10],t[4:7],t[-4:]
        self.core.cmm.cursor.execute( "SELECT * FROM stats WHERE Date=\'%s\' AND Month=\'%s\' AND Year=\'%s\' "%(date,month,year) )
        is_existant = self.core.cmm.cursor.fetchall()

        if is_existant:
            self.core.cmm.cursor.execute("UPDATE stats SET `Expense` = `Expense` + \'%s\' WHERE Date=\'%s\' AND Month=\'%s\' AND Year=\'%s\'"%(value,date,month,year))
        else:
            self.core.cmm.cursor.execute("INSERT INTO stats (`Year`,`Month`,`Date`,`Expense`,`Profit Salewise`,`Tax`,`Key`) VALUES (?,?,?,?,?,?,?)",
                                        (year,month,date,value,'0','0','0'))
        self.core.cmm.server.commit()
        self.update()
        self.amount_add.clear()
        self.description.clear()
        self.red_exp.setChecked(False)
        return

    def name_search_routine(self):
        name = self.name_search.text()
        self.core.cmm.cursor.execute('select * from expensemodels where Name like (?)',(name+'%',))
        self.models_data = self.core.cmm.cursor.fetchall()
        self.name_table.setRowCount(0)
        self.name_table.setRowCount(len(self.models_data))
        for i in range(0,len(self.models_data)):
            data_widgets = [QtGui.QTableWidgetItem(str(j)) for j in self.models_data[i] ]
            for j,k in enumerate(data_widgets):
                self.name_table.setItem(i,j,k)




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

