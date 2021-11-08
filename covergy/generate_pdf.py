import pdfkit
class PdfGenerator:
    """Generate pdf file from html"""
    def __init__(self, html_file):
        self.html_file = html_file
        self.pdf_file = html_file.replace('.html', '.pdf')

    def generate(self):
        """Generate pdf file"""
        import pdfkit
        pdfkit.from_file(self.html_file, self.pdf_file)
        print('PDF file generated:', self.pdf_file)