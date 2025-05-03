import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    """Extracts text from an uploaded PDF"""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip() if text else "No text found in PDF."
