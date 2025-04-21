import fitz  # PyMuPDF
'''Time for historical lesson fitz is also known as PyMuPDF dur to historical reasons, i don't know why but it is 😊 
                                                {just for fact i had to search for this smiley face , then i had to paste it}'''

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF resume."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")  # Extract text from each page
    return text.strip()
