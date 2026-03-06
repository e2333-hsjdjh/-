import pdfplumber
import os

base_path = "/Users/zzzzzz/Desktop/大创选题确定/papers/"
output_file = "/Users/zzzzzz/Desktop/大创选题确定/utils/pdf_summaries_raw_v2.txt"

files = os.listdir(base_path)
pdf_files = [f for f in files if f.endswith('.pdf')]
pdf_files.sort()

with open(output_file, 'w', encoding='utf-8') as out:
    for pdf_file in pdf_files:
        full_path = os.path.join(base_path, pdf_file)
        out.write(f"\n====================\nFILE: {pdf_file}\n====================\n")
        try:
            with pdfplumber.open(full_path) as pdf:
                if len(pdf.pages) > 0:
                    # Extract first 3 pages just to be safe (sometimes title page is separate)
                    num_pages = min(3, len(pdf.pages))
                    for i in range(num_pages):
                        page = pdf.pages[i]
                        text = page.extract_text()
                        if text:
                            out.write(f"--- PAGE {i+1} ---\n{text}\n")
                else:
                    out.write("No pages found.\n")
        except Exception as e:
            out.write(f"Error extracting {pdf_file}: {e}\n")

print(f"Done. Processed {len(pdf_files)} PDF files.")
