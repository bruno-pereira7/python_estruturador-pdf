from PyPDF2 import PdfReader
import pdfplumber

def extract_data_from_pdf(pdf_path):
    """
    Extrai texto e metadados de um arquivo PDF
    """
    data = {
        'text': '',
        'metadata': {},
        'tables': []
    }
    
    # Extrai texto básico e metadados
    with open(pdf_path, 'rb') as file:
        pdf = PdfReader(file)
        data['metadata'] = pdf.metadata
        
        for page in pdf.pages: 
            data['text'] += page.extract_text() + '\n'
    
    # Extrai tabelas (usando pdfplumber para melhor precisão)
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            if tables:
                data['tables'].extend(tables)
    
    return data