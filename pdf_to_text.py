import pytesseract
import os
import fitz
class PdfToText():
    def __init__(self,file_name):
        self.file_name = file_name
        self.pages = {}
    
    def extract_text(self):
        if not self.file_name.lower().endswith(".pdf"):
            print("Not a valid file type, only pdf accepted here !!!")
            return None
        if not os.path.isfile(self.file_name) :
            print("File does not exist!!!")
            return None
        doc = fitz.open(self.file_name)
        for page_num,page in enumerate(doc,start = 1):
            txt = page.get_text()
            self.pages[page_num] = txt
        doc.close()
        return self.pages
