# 📄 Estruturador PDF - Documentação

## 🔍 Visão Geral
O **PDF Data Processor** é uma ferramenta CLI (Command Line Interface) desenvolvida em Python para extrair, estruturar e processar dados de arquivos PDF.

### Funcionalidades Principais:
- Extração de texto bruto
- Captura de metadados
- Extração de tabelas
- Estruturação automática de dados
- Exportação para JSON ou exibição no terminal

## ⚙️ Pré-requisitos
- Python 3.8+
- Pip (gerenciador de pacotes)

## 🚀 Instalação

**Clone o repositório**

```bash
git clone https://github.com/seu-usuario/pdf-data-processor.git
cd pdf-data-processor
```

**Crie um ambiente virtual (recomendado)**

```bash
python -m venv venv
source venv/bin/activate      # Linux/MacOS
venv\Scripts\activate         # Windows
```

**Instale as dependências**
```bash
pip install -r requirements.txt
```

## 📦 Dependências Principais
- **PyPDF2:** Extração básica de texto e metadados

- **pdfplumber:** Extração precisa de texto e tabelas

- **argparse:** Processamento de argumentos CLI

## 🗂 Estrutura do Projeto

```
pdf-data-processor/
├── main.py              # Ponto de entrada principal
├── cli.py               # Interface de linha de comando
├── pdf_parser.py        # Lógica de extração de PDFs
├── data_processor.py    # Processamento de dados
├── utils.py             # Funções auxiliares
├── requirements.txt     # Lista de dependências
├── outputs/             # Pasta de saídas
│   ├── json/            # Resultados em JSON
│   └── csv/             #Resultados em CSV
└── README.md           #Documentação
```

## 🔁 Fluxo de Processamento
**1. Entrada:**
- Arquivo PDF fornecido via argumento CLI

**2. Extração:**

- Metadados via PyPDF2
- Texto e tabelas via pdfplumber

**3. Processamento:**

- Limpeza e normalização de texto
- Identificação de seções

- Estruturação de tabelas

**4. Saída:**

- Exibição no terminal
- Exportação para arquivo (JSON/CSV)

## 🧪 Exemplos de Uso

### Comandos Básicos:

**Exibir resultado no terminal**

```bash
python main.py documento.pdf
```

**Salvar como JSON**

```bash
python main.py documento.pdf -o resultado.json
```

**Modo verboso (detalhado)**
```bash
python main.py documento.pdf -v
```
### Comandos Avançados:

**Processar todos os PDFs da pasta**
```bash
for arq in *.pdf; do python main.py "$arq" -o "${arq%.pdf}.json"; done
```

**Extrair páginas específicas (1-5)**
```bash
python main.py relatorio.pdf --pages 1-5
```

**Extrair apenas tabelas (formato CSV)**
```bash
python main.py dados.pdf --tables-only -o tabelas.csv
```

**Modo silencioso (apenas erros)**
```bash
python main.py contrato.pdf --quiet
```

## ⚙️ Opções Disponíveis

| Opção          | Atalho | Descrição                                      | Exemplo de Uso                     |
|----------------|--------|-----------------------------------------------|------------------------------------|
| `--output`     | `-o`   | Salvar resultado em arquivo (JSON/CSV)        | `python main.py doc.pdf -o saida.json` |
| `--verbose`    | `-v`   | Mostrar detalhes do processamento             | `python main.py doc.pdf -v`        |
| `--pages`      |        | Processar páginas específicas (ex: 1,3-5)     | `python main.py doc.pdf --pages 1-3,5` |
| `--tables-only`|        | Extrair apenas tabelas                        | `python main.py doc.pdf --tables-only` |
| `--text-only`  |        | Extrair apenas texto                          | `python main.py doc.pdf --text-only` |
| `--metadata`   |        | Mostrar apenas metadados                      | `python main.py doc.pdf --metadata` |
| `--quiet`      |        | Ocultar tudo exceto erros                     | `python main.py doc.pdf --quiet`   |
| `--help`       | `-h`   | Exibir ajuda                                  | `python main.py --help`            |

💡 **Dica**: Combine opções como `-v -o saida.json` para modo verboso + exportação

## 🧾 Formato de Saída
```json
{
  "metadata": {
    "author": "John Doe",
    "title": "Relatório Anual 2023",
    "creator": "Microsoft Word"
  },
  "sections": {
    "section_0": "Título do Documento...",
    "section_1": "Introdução...",
    "section_2": "Metodologia..."
  },
  "tables": [
    {
      "rows": 5,
      "data": [
        ["Item", "Quantidade", "Preço"],
        ["1", "2", "R$ 10,00"]
      ]
    }
  ]
}
```

## ⚠️ Limitações Conhecidas
- PDFs digitalizados (sem suporte a OCR)

- Layouts complexos podem afetar extração

- Células mescladas em tabelas podem ter problemas

## 🛠 Solução de Problemas
- **Arquivo não encontrado:** Verifique caminhos absolutos

- **PDF criptografado:** Não suportado atualmente

- **Extração incompleta:** Use -v para depuração

## 🗺 Roadmap Futuro
- Suporte a PDFs protegidos por senha

- Integração com OCR (Tesseract)

- Exportação para XML/SQL

- Interface Web/REST

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/incrivel`)
3. Faça commit das mudanças (`git commit -am 'Adiciona feature incrível'`)
4. Faça push para a branch (`git push origin feature/incrivel`)
5. Abra um Pull Request

## 📬 Contato
Nome: Bruno

Email: brunorochape.contato@gmail.com

Issues: [GitHub Issues](https://github.com/bruno-pereira7/python_estruturador-pdf/issues)
