from pdfminer.high_level import extract_text

def extract_pdf_text(uploaded_file):
    try:
        return extract_text(uploaded_file)
    except Exception:
        return ""
