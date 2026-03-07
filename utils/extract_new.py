import pdfplumber
import zipfile
import re
import os

pdf_path = "/Users/zzzzzz/Desktop/大创选题确定/papers/zmx003.pdf"
docx_path = "/Users/zzzzzz/Desktop/大创选题确定/papers/情绪传播.docx"

print("START_PDF")
try:
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            if i >= 3: break
            text = page.extract_text()
            if text:
                print(f"--- PAGE {i+1} ---")
                print(text)
except Exception as e:
    print(f"Error reading PDF: {e}")
print("END_PDF")

print("START_DOCX")
try:
    with zipfile.ZipFile(docx_path) as z:
        xml_content = z.read('word/document.xml')
        # Extract text from XML
        text = re.findall(r'<w:t[^>]*>(.*?)</w:t>', xml_content.decode('utf-8'))
        print("".join(text))
except Exception as e:
    print(f"Error reading DOCX: {e}")
print("END_DOCX")