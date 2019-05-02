import sys, os
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Document Printer')
        self.editor = QtGui.QTextEdit(self)
        self.editor.textChanged.connect(self.handleTextChanged)
        #self.buttonOpen = QtGui.QPushButton('Open', self)
        #self.buttonOpen.clicked.connect(self.handleOpen)
        self.buttonPrint = QtGui.QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QtGui.QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        self.handleOpen(QtCore.QString(os.path.abspath("recipt.html")))
        #layout.addWidget(self.buttonOpen, 1, 0)
        layout.addWidget(self.buttonPrint, 1, 0)
        layout.addWidget(self.buttonPreview, 1, 1)
        self.handleTextChanged()

    def handleOpen(self,path):
        p = path
        # print("that",QtCore.QString(path))
        path = QtGui.QFileDialog.getOpenFileName(
            self, 'Open file', '',
            'HTML files (*.html);;Text files (*.txt)')
        # print("this",path)
        # #path = 'recipt.html'
        print(p)
        print(path)
        assert(p==path)
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

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())
