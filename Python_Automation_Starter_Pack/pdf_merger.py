import os
from PyPDF2 import PdfMerger

def merge_pdfs(folder_path,output_name = "merged.pdf"):
    merger = PdfMerger()
    files = sorted([f for f in os.listdir(folder_path) if f.endswith(".pdf")])

    for pdf in files:
        pdf_path = os.path.join(folder_path,pdf)
        merger.append(pdf_path)

    output_path = os.path.join(folder_path,output_name)
    merger.write(output_path)
    merger.close()
    print(f"merged {len(files)} PDFs into '{output_name}'")

# Example usage
# merge_pdfs("path of the folder containing pdfs.", output_name="Final_Merged.pdf")