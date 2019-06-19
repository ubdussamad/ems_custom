from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(30, -1, 62, 267)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 1, 2)
        self.chgpwdbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.chgpwdbutton.setObjectName("chgpwdbutton")
        self.gridLayout.addWidget(self.chgpwdbutton, 5, 1, 1, 2)
        self.delusr = QtWidgets.QPushButton(self.layoutWidget)
        self.delusr.setObjectName("delusr")
        self.gridLayout.addWidget(self.delusr, 5, 3, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 6, 1, 1, 3)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.username = QtWidgets.QLabel(self.layoutWidget)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 2, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.pwdcnf = QtWidgets.QLineEdit(self.layoutWidget)
        self.pwdcnf.setObjectName("pwdcnf")
        self.gridLayout.addWidget(self.pwdcnf, 4, 1, 1, 3)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 5, 1)
        self.pwd = QtWidgets.QLineEdit(self.layoutWidget)
        self.pwd.setObjectName("pwd")
        self.gridLayout.addWidget(self.pwd, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.newuser = QtWidgets.QLineEdit(self.layoutWidget)
        self.newuser.setObjectName("newuser")
        self.verticalLayout.addWidget(self.newuser)
        self.newpwd = QtWidgets.QLineEdit(self.layoutWidget)
        self.newpwd.setAutoFillBackground(False)
        self.newpwd.setObjectName("newpwd")
        self.verticalLayout.addWidget(self.newpwd)
        self.registebutton = QtWidgets.QPushButton(self.layoutWidget)
        self.registebutton.setObjectName("registebutton")
        self.verticalLayout.addWidget(self.registebutton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_2.addWidget(self.splitter, 0, 1, 1, 1)
        self.oplist = QtWidgets.QTableWidget(self.centralwidget)
        self.oplist.setObjectName("oplist")
        self.oplist.setColumnCount(0)
        self.oplist.setRowCount(0)
        self.gridLayout_2.addWidget(self.oplist, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EMS | User Maintainance Module"))
        self.chgpwdbutton.setText(_translate("MainWindow", "Change Password"))
        self.delusr.setText(_translate("MainWindow", "Delete User"))
        self.label.setText(_translate("MainWindow", "User Name"))
        self.username.setText(_translate("MainWindow", "Not Selected"))
        self.pwdcnf.setPlaceholderText(_translate("MainWindow", "Enter New Password"))
        self.pwd.setPlaceholderText(_translate("MainWindow", "Enter Last Password"))
        self.label_4.setText(_translate("MainWindow", "Add New User"))
        self.newuser.setPlaceholderText(_translate("MainWindow", "Enter Username"))
        self.newpwd.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.registebutton.setText(_translate("MainWindow", "Register"))
        self.integrate_functionality()

    def integrate_functionality(self):
        import sqlite3
        self.server = sqlite3.connect('data/ems.db')
        self.cursor = self.server.cursor()
        self.update_table()
        self.oplist.itemSelectionChanged.connect(self.update_labels)
        self.delusr.clicked.connect(self.delete_user)
        self.chgpwdbutton.clicked.connect(self.password_change_routine)
        self.registebutton.clicked.connect(self.add_new_user)

    def update_table(self):
        self.cursor.execute("select user from credentials")
        self.data = self.cursor.fetchall()
        if any(self.data):
            # Update the Qt table view as-in
            self.oplist.setRowCount(len(self.data))
            self.oplist.setColumnCount(len(self.data[0]))
            self.table_headers = ['User']
            self.oplist.setHorizontalHeaderLabels(self.table_headers)
            for i in range(0,len(self.data)):
                self.data_widgets = [QtWidgets.QTableWidgetItem(j) for j in self.data[i] ]
                for j,k in enumerate(self.data_widgets):
                    self.oplist.setItem(i,j,k)
        else:
            self.statusbar.showMessage("No Valid Accounts Found!")

    def password_change_routine(self):
        current_password = self.pwd.text()
        new_password = self.pwdcnf.text()

        if not (current_password+new_password):
            self.statusbar.showMessage("Fill the text Fields to Chnage the password!" , 2000)

        indexes = [i.row() for i in self.oplist.selectionModel().selectedRows()]
        usr = self.oplist.item(indexes[0],0).text()

        self.cursor.execute("select password from credentials where user = (?)" , (usr,) )
        self.data = self.cursor.fetchone()

        pwd_hash = self.data[0]
        import hashlib

        if hashlib.md5(current_password.encode('utf-8')).hexdigest() == pwd_hash:
            #There shall be the new password
            self.cursor.execute("UPDATE credentials SET password = (?) where user = (?)" , 
                ( hashlib.md5(new_password.encode('utf-8')).hexdigest() , usr))
            self.server.commit()
            self.statusbar.showMessage("Password Changed Sucessfully!",3000)
            self.pwd.clear()
            self.pwdcnf.clear()

        else:
            self.statusbar.showMessage("Wrong Password!",3000)

    def add_new_user(self):
        self.cursor.execute("INSERT INTO credentials VALUES (?,?)" , 
                (self.newuser.text() ,
                hashlib.md5(self.newpwd.text().encode('utf-8')).hexdigest()))
        self.server.commit()
        self.statusbar.showMessage("User Added Sucessfully!",3000)
        self.newpwd.clear()
        self.newuser.clear()
        return

    def update_labels(self):
        indexes = [i.row() for i in self.oplist.selectionModel().selectedRows()]
        if not any(indexes):
            return
        usr = self.oplist.item(indexes[0],0).text()
        self.username.setText(usr)


    def delete_user(self):

        current_password = self.pwd.text()
        indexes = [i.row() for i in self.oplist.selectionModel().selectedRows()]
        usr = self.oplist.item(indexes[0],0).text()

        self.cursor.execute("select password from credentials where user = (?)" , (usr,) )
        self.data = self.cursor.fetchone()
        pwd_hash = self.data[0]
        
        import hashlib

        if hashlib.md5(current_password.encode('utf-8')).hexdigest() != pwd_hash:
            self.statusbar.showMessage("Please enter the right password to delete!",3000)
            return

        self.cursor.execute("DELETE FROM credentials where user = (?)", (usr,))
        self.server.commit()
        self.update_table()
        self.statusbar.showMessage("User Deleted")
        return



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())