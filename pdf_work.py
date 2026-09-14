from pypdf import PdfReader

class PdfWorks:

    def load_pdf():
        pdf = PdfReader("nota.pdf")
        page = pdf.pages[0]
        text = page.extract_text()
        print(text)
