import os
import json
import csv
from typing import Union, Dict, List
from pathlib import Path

def validate_pdf_path(file_path: str) -> bool:
    """Verifica se o caminho do PDF é válido"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado")
    if not file_path.lower().endswith('.pdf'):
        raise ValueError("O arquivo deve ter extensão .pdf")
    return True

def save_as_json(data: Union[Dict, List], output_path: str) -> None:
    """Salva os dados estruturados em um arquivo JSON"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_as_csv(data: Union[Dict, List], output_path: str) -> None:
    """Salva os dados estruturados em um arquivo CSV"""
    # Implementação básica - pode precisar de ajustes dependendo da estrutura dos dados
    if isinstance(data, dict):
        data = [data]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def create_output_dir(dir_name: str = 'outputs') -> str:
    """Cria o diretório de saída se não existir"""
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    return dir_name

def clean_text(text: str) -> str:
    """Remove espaços extras e caracteres especiais do texto"""
    if not text:
        return text
    
    # Remove múltiplos espaços/tabs/newlines
    text = ' '.join(text.split())
    
    # Remove caracteres não-ASCII (opcional)
    text = text.encode('ascii', 'ignore').decode('ascii')
    
    return text.strip()

def get_file_name_without_extension(file_path: str) -> str:
    """Extrai o nome do arquivo sem extensão do caminho"""
    return Path(file_path).stem

def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    """Imprime uma barra de progresso no terminal"""
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total: 
        print()

def measure_execution_time(func):
    """Decorator para medir tempo de execução de funções"""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time() 
        print(f"\nTempo de execução de {func.__name__}: {end_time - start_time:.2f} segundos")
        return result
    return wrapper