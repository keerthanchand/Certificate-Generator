

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter



def make_certificate_pdf(name, certificate_id):        
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFontSize(40)
    can.setFont('Helvetica-Bold', 36)
    string = name
    string = string.upper()
    can.drawString(100, 357, string)
    can.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    existing_pdf = PdfFileReader(open("/home/keerthan/Downloads/original.pdf", "rb"))
    output = PdfFileWriter()
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    certificate_id += ".pdf"
    path = "/home/keerthan/Downloads/"
    path += certificate_id
    outputStream = open(path, "wb")
    output.write(outputStream)
    outputStream.close()

make_certificate_pdf("keerthan", "afsdfsd")