import argparse
from .pdf_extrai import extract_data_from_pdf
from .processa_dados import process_extracted_data
 
def main():
    parser = argparse.ArgumentParser(description='Processador de PDF para estruturação de dados')
    
    parser.add_argument('input', help='Caminho do arquivo PDF de entrada')
    parser.add_argument('-o', '--output', help='Caminho do arquivo de saída (JSON/CSV)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Modo verboso')
    
    args = parser.parse_args()
    
    # Processamento
    raw_data = extract_data_from_pdf(args.input)
    structured_data = process_extracted_data(raw_data)
    
    # Saída
    if args.output:
        save_output(structured_data, args.output)
    else:
        print(structured_data)

def save_output(data, output_path):
    # Implemente a lógica para salvar em JSON, CSV, etc.
    pass

if __name__ == '__main__':
    main()