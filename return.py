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
        QtCore.QMetaObject.connectSlotsByName(Dialog)

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

