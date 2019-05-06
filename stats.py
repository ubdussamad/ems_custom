# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stats.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random,hashlib
from ems_core import *
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
some = ems_core('ems','admin')
class Ui_MainWindow(object):
    def __init__(self):
        self.auth = 1
    def add_expense_routine(self):
        amount = self.addexp.text()
        try:
            float(amount)
        except:
            return
        t = time.ctime()
        date,month,year = t[8:10],t[4:7],t[-4:]
        some.lmm.cursor.execute( "SELECT * FROM stats WHERE Date=\'%s\' AND Month=\'%s\' AND Year=\'%s\' "%(date,month,year) )
        is_existant = some.lmm.cursor.fetchall()

        if is_existant:
            some.lmm.cursor.execute("UPDATE stats SET `Expense` = `Expense` + \'%s\' WHERE Date=\'%s\' AND Month=\'%s\' AND Year=\'%s\'"%(amount,date,month,year))
        else:
            some.lmm.cursor.execute("INSERT INTO stats (`Year`,`Month`,`Date`,`Expense`,`Profit Salewise`,`Tax`,`Key`) VALUES (?,?,?,?,?,?,?)",
                                        (year,month,date,amount,'0','0','0'))
        some.lmm.server.commit()
        self.addexp.clear()
    def __auth(self):
        key = self.pwd.text()
        self.__key_hash = '04a11c0ac3d39a7d59c2ee0cdcdcabb4'
        key_md5 = hashlib.md5(key.encode('utf-8')).hexdigest()
        if key_md5 == self.__key_hash:
            self.auth = 0
            print("Access")
        else:
            self.auth = 1

    def calc_profit(self):
        self.plot()
        isday,ismonth,isyear = [i.isChecked() for i in [self.isday,self.ismonth,self.isyear]]
        internal = not(self.auth) and self.internal.isChecked()
        day,month,year = self.day.currentText(),self.month.currentText(),self.year.currentText()
        half_query = 'SELECT `Expense`,`Profit Salewise`,`Tax`,`key` FROM stats WHERE '
        const = str('Date = \'%s\' AND '%day if isday else '') + str('Month = \'%s\' AND '%month if ismonth else '')
        const += 'Year = \'%s\''%year
        query = half_query + const
        #print(query)
        some.lmm.cursor.execute(query)
        data = some.lmm.cursor.fetchall()
        profit,tax,expense,hp = 0,0,0,0
        for i in data:
            profit+=float(i[1])
            tax+=float(i[2])
            expense+=float(i[0])
            hp+=float(i[3])
        #print(internal)
        #print("Profit: %f"%profit)
        #print("Tax: %f"%tax)
        #print("Expense: %f"%expense)
        #print("Hidden: %f\n\n"%hp)
        self.extraexpenses.setText(str(expense))
        self.profit.setText(str(profit))
        self.label_4.setText(_translate("MainWindow", "Stats for the Period", None))
        if internal:
            self.profit.setText(str(hp))
            self.tax.setText('0.0')
            self.label_4.setText('Stats for Internal Sales')
            return
        self.tax.setText(str(tax))
        return


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(651, 497)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_2.addWidget(self.label_9)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))

        # expense additoon bar
        self.addexp = QtGui.QLineEdit(self.centralwidget)
        self.addexp.setObjectName(_fromUtf8("addexp"))
        self.horizontalLayout_3.addWidget(self.addexp)

        # Expense addition button
        self.appendexp = QtGui.QPushButton(self.centralwidget)
        self.appendexp.setObjectName(_fromUtf8("appendexp"))
        self.appendexp.clicked.connect(self.add_expense_routine)

        self.horizontalLayout_3.addWidget(self.appendexp)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        # PWD field
        self.pwd = QtGui.QLineEdit(self.centralwidget)
        self.pwd.setObjectName(_fromUtf8("pwd"))
        self.pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.horizontalLayout_4.addWidget(self.pwd)

        # Chk pwd Button
        self.chkpwd = QtGui.QPushButton(self.centralwidget)
        self.chkpwd.setObjectName(_fromUtf8("chkpwd"))
        self.chkpwd.clicked.connect(self.__auth)
        self.horizontalLayout_4.addWidget(self.chkpwd)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        # Stats type
        self.normal = QtGui.QRadioButton(self.centralwidget)
        self.normal.setObjectName(_fromUtf8("normal"))
        self.horizontalLayout_5.addWidget(self.normal)
        # stats type
        self.internal = QtGui.QRadioButton(self.centralwidget)
        self.internal.setObjectName(_fromUtf8("internal"))
        self.horizontalLayout_5.addWidget(self.internal)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout.addWidget(self.line_5)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(48)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        # is Day
        self.isday = QtGui.QCheckBox(self.centralwidget)
        self.isday.setObjectName(_fromUtf8("isday"))
        self.horizontalLayout_2.addWidget(self.isday)
        # Is month
        self.ismonth = QtGui.QCheckBox(self.centralwidget)
        self.ismonth.setObjectName(_fromUtf8("ismonth"))
        self.horizontalLayout_2.addWidget(self.ismonth)
        # Is year
        self.isyear = QtGui.QCheckBox(self.centralwidget)
        self.isyear.setObjectName(_fromUtf8("isyear"))
        self.horizontalLayout_2.addWidget(self.isyear)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        # Day select
        self.day = QtGui.QComboBox(self.centralwidget)
        self.day.setObjectName(_fromUtf8("day"))
        self.horizontalLayout.addWidget(self.day)
        some.lmm.cursor.execute("SELECT Date FROM stats")
        days = sorted(set(some.lmm.cursor.fetchall()))
        self.day.clear()
        for text in days:
            self.day.addItem(str(text[0]))
        #self.comboBox.currentIndexChanged.connect(self.customer_change)


        # Month select
        some.lmm.cursor.execute("SELECT Month FROM stats")
        months = set(some.lmm.cursor.fetchall())
        self.month = QtGui.QComboBox(self.centralwidget)
        self.month.clear()
        for text in months:
            self.month.addItem(str(text[0]))
        self.month.setObjectName(_fromUtf8("month"))
        self.horizontalLayout.addWidget(self.month)



        # Year select
        some.lmm.cursor.execute("SELECT Year FROM stats")
        years = sorted(set(some.lmm.cursor.fetchall()))
        self.year = QtGui.QComboBox(self.centralwidget)
        self.year.clear()
        for text in years:
            self.year.addItem(str(text[0]))
        self.year.setObjectName(_fromUtf8("year"))


        self.horizontalLayout.addWidget(self.year)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 17))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout.addWidget(self.line_6)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        # Expenses label
        self.extraexpenses = QtGui.QLabel(self.centralwidget)
        self.extraexpenses.setObjectName(_fromUtf8("extraexpenses"))
        self.gridLayout.addWidget(self.extraexpenses, 0, 1, 1, 1)
        # Tax label
        self.tax = QtGui.QLabel(self.centralwidget)
        self.tax.setObjectName(_fromUtf8("tax"))
        self.gridLayout.addWidget(self.tax, 2, 1, 1, 1)
        # Profit Label
        self.profit = QtGui.QLabel(self.centralwidget)
        self.profit.setObjectName(_fromUtf8("profit"))
        self.gridLayout.addWidget(self.profit, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        # Update button
        self.update = QtGui.QPushButton(self.centralwidget)
        self.update.setObjectName(_fromUtf8("update"))
        self.gridLayout.addWidget(self.update, 3, 0, 1, 1)
        self.update.clicked.connect(self.calc_profit)
        # Back button
        self.back = QtGui.QPushButton(self.centralwidget)
        self.back.setObjectName(_fromUtf8("back"))
        #self.back.clicked.connect(exit)
        self.gridLayout.addWidget(self.back, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_6.addWidget(self.line)


        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.centralwidget)
        self.verticalLayout_s = QtGui.QVBoxLayout()
        self.horizontalLayout_6.addLayout(self.verticalLayout_s)

        self.verticalLayout_s.addWidget(self.graphicsView)
        self.verticalLayout_s.addWidget(self.canvas)
        self.verticalLayout_s.addWidget(self.toolbar)
        #self.horizontalLayout_6.addWidget(self.canvas)
        #self.horizontalLayout_6.addWidget(self.graphicsView)
        #self.horizontalLayout_6.addWidget(self.toolbar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def plot(self):
        ismonth,isyear = [i.isChecked() for i in [self.ismonth,self.isyear]]
        day,month,year = self.day.currentText(),self.month.currentText(),self.year.currentText()
        half_query = "select (`Profit Salewise` + `key`) as Total from stats " + ('WHERE ' if ismonth or isyear else '')
        const = str('`Month` = \'%s\' AND '%month if ismonth else '')
        const += '`Year` = \'%s\''%year if isyear else ''
        query = half_query + const
        #print(query)
        
        some.lmm.cursor.execute(query)
        data = some.lmm.cursor.fetchall()
        data = [int(i[0]) for i in data]
        #print(data)
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.set_xlabel('Relative Timeline')
        ax.set_ylabel('Relative Profit')
        #ax.set_rcParams["figure.figsize"] = (20,3)
        ax.plot(data)
        self.canvas.draw()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "EMS | STATS", None))
        self.label_9.setText(_translate("MainWindow", "Add Expense", None))
        self.appendexp.setText(_translate("MainWindow", "Add", None))
        self.chkpwd.setText(_translate("MainWindow", "Check", None))
        self.label_5.setText(_translate("MainWindow", "Calculation Method", None))
        self.normal.setText(_translate("MainWindow", "Precision", None))
        self.internal.setText(_translate("MainWindow", "Celling", None))
        self.label_8.setText(_translate("MainWindow", "Calculate Data For", None))
        self.isday.setText(_translate("MainWindow", "Day", None))
        self.ismonth.setText(_translate("MainWindow", "Month", None))
        self.isyear.setText(_translate("MainWindow", "Year", None))
        self.label_4.setText(_translate("MainWindow", "Stats for the Period", None))
        self.label.setText(_translate("MainWindow", "Extra Expenses", None))
        self.label_2.setText(_translate("MainWindow", "Profit", None))
        self.extraexpenses.setText(_translate("MainWindow", "0.0", None))
        self.tax.setText(_translate("MainWindow", "0.0", None))
        self.profit.setText(_translate("MainWindow", "0.0", None))
        self.label_3.setText(_translate("MainWindow", "Tax", None))
        self.update.setText(_translate("MainWindow", "Update", None))
        self.back.setText(_translate("MainWindow", "Back", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
