import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton
from PyQt5.QtGui import QIcon


from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        uploadBtn = QPushButton('Upload', self)
        uploadBtn.setToolTip('This is an example button')
        uploadBtn.move(100,400)
        uploadBtn.clicked.connect(self.openFileNameDialog)
        saveBtn = QPushButton('Save Location', self)
        saveBtn.setToolTip('This is an example button')
        saveBtn.move(200,400)
        saveBtn.clicked.connect(self.saveFileDialog)
        convertBtn = QPushButton('Convert', self)
        convertBtn.setToolTip('This is an example button')
        convertBtn.move(310,400)
        convertBtn.clicked.connect(self.make_certificate_pdf)
        
        self.show()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.uploadFilePath, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if self.uploadFilePath:
            print(self.uploadFilePath)

    
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.saveFilePath, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if self.saveFilePath:
            print(self.saveFilePath)


    def make_certificate_pdf(self):        
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(40)
        can.setFont('Helvetica-Bold', 36)
        string = "keerthan"
        string = string.upper()
        can.drawString(100, 357, string)
        can.save()
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        existing_pdf = PdfFileReader(open(self.uploadFilePath, "rb"))
        output = PdfFileWriter()
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        path = self.saveFilePath
        outputStream = open(path, "wb")
        output.write(outputStream)
        outputStream.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())