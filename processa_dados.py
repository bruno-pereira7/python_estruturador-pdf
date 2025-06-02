import re
from typing import Dict, Any

def process_extracted_data(raw_data: Dict[str, Any]) -> Dict[str, Any]:   
#    Estrutura os dados extraídos do PDF em um formato mais organizado

    processed = {
        'metadata': process_metadata(raw_data['metadata']),
        'sections': extract_sections(raw_data['text']),
        'tables': process_tables(raw_data['tables'])
    }
    
    return processed

def process_metadata(metadata):
    # Processa metadados do PDF
    return {k: v for k, v in metadata.items() if v}

def extract_sections(text):
    # Implemente lógica para dividir o texto em seções
    sections = {}
    # Exemplo simples - dividir por quebras de linha duplas
    parts = re.split(r'\n\s*\n', text)
    for i, part in enumerate(parts):
        if part.strip():
            sections[f'section_{i}'] = part.strip() 
    return sections 

def process_tables(tables):
    # Processa tabelas extraídas
    return [{'rows': len(table), 'data': table} for table in tables]