# Estruturador PDF - Documentação

## Visão Geral

O PDF Data Processor é uma ferramenta de linha de comando (CLI) desenvolvida em Python para extrair, estruturar e processar dados de arquivos PDF. O software é capaz de: 

- Extrair texto bruto de PDFs
- Capturar metadados do documento
- Identificar e extrair tabelas
- Estruturar os dados em um formato organizado 
- Exportar resultados em JSON ou exibir no terminal

## Pré-requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)

## Instalação

**1. Clone o repositório ou baixe os arquivos do projeto:**

```bash
git clone https://github.com/seu-usuario/pdf-data-processor.git
```
Depois:

```bash
cd pdf-data-processor
```

**2. Crie um ambiente virtual (recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

## Dependências

O projeto utiliza as seguintes bibliotecas principais:

- PyPDF2: Para extração básica de texto e metadados

- pdfplumber: Para extração precisa de tabelas e texto

- argparse: Para processamento de argumentos de linha de comando

## Arquitetura do Projeto
```

pdf-data-processor/
├── main.py              # Ponto de entrada principal
├── cli.py               # Lógica de interface de linha de comando
├── pdf_parser.py        # Extração de conteúdo de PDFs
├── data_processor.py    # Processamento e estruturação de dados
├── utils.py             # Funções auxiliares compartilhadas
├── requirements.txt     # Dependências do projeto
├── outputs/             # Diretório para arquivos processados
│   ├── json/            # Saídas no formato JSON
│   └── csv/             # Saídas no formato CSV
└── README.md            # Documentação do projeto
```

**Fluxo de Processamento**

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
- Exportação para arquivo

## Uso Básico

**Sintaxe do Comando**

```bash
python main.py <arquivo.pdf> [opções]

```

**Exemplos**


**1. Processar um PDF e exibir resultados no terminal:**

```bash
python main.py documento.pdf

```

**2. Processar um PDF e salvar em arquivo JSON:**

```bash
python main.py documento.pdf -o resultado.json
```

**3. Processar em modo verboso (mostra detalhes do processamento):**

```bash
python main.py documento.pdf -v
```

## Comandos Básicos

**1. Processar um arquivo PDF e mostrar resultado no terminal:**

```bash
python main.py documento.pdf
```

**2. Processar e salvar em JSON:**

```bash
python main.py documento.pdf -o resultado.json
```

**3. Processar em modo verboso (mostra detalhes):**

```bash
python main.py documento.pdf -v
```

## Comandos Avançados
**1. Processar TODOS os PDF's de uma pasta:**

```bash
for arquivo in *.pdf; do python main.py "$arquivo" -o "${arquivo%.pdf}.json"; done
```

**2. Processar apenas páginas específicas (ex: pág 1 a 5):**

```bash
python main.py relatorio.pdf --pages 1-5
```

**3. Extrair só tabelas para CSV:**

```bash
python main.py dados.pdf --tables-only -o tabelas.csv
```

**4. Modo silencioso (só mostra erros):**

```bash
python main.py contrato.pdf --quiet tabelas.csv
```

## Opções Disponíveis

| Comando          | Atalho | Descrição                                      | Exemplo de Uso                     |
|------------------|--------|-----------------------------------------------|------------------------------------|
| `--output`       | `-o`   | Salva em arquivo (JSON/CSV)                   | `python main.py doc.pdf -o saida.json` |
| `--verbose`      | `-v`   | Modo detalhado (mostra processamento interno) | `python main.py doc.pdf -v`        |
| `--pages`        |        | Processa páginas específicas                  | `python main.py doc.pdf --pages 1,3-5` |
| `--tables-only`  |        | Extrai APENAS tabelas                         | `python main.py doc.pdf --tables-only` |
| `--text-only`    |        | Extrai APENAS texto                           | `python main.py doc.pdf --text-only` |
| `--metadata`     |        | Mostra APENAS metadados do PDF                | `python main.py doc.pdf --metadata` |
| `--quiet`        |        | Modo silencioso (mostra apenas erros)         | `python main.py doc.pdf --quiet`    |

### Dicas:
- Combine opções: `-v -o saida.json` (verboso + salva em arquivo)
- Use `--` para valores que começam com `-`: `--pages -- -1` (página especial)
## Opções Disponíveis

| Opção         | Descrição                                      | Exemplo               |
|---------------|-----------------------------------------------|-----------------------|
| `-o`, `--output` | Salva a saída em um arquivo (JSON ou CSV)     | `-o resultado.json`   |
| `-v`, `--verbose` | Ativa modo verboso para detalhes de processo  | `-v`                  |
| `-h`, `--help`   | Mostra mensagem de ajuda                      | `-h`                  |

## Saída do Programa

O programa gera um objeto JSON estruturado com três seções principais:

**1. metadata:** Informações do documento (autor, título, etc.)

**2. sections:** Texto do documento dividido em seções

**3. tables:** Tabelas extraídas com seus dados

**Exemplos de Saída:**

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
        ["1", "2", "R$ 10,00"],
        ...
      ]
    }
  ]
}
```

## Processamento Avançado

**Formatos de Saída**

O programa suporta diferentes formatos de saída:

**1. JSON** (padrão): **`-o saida.json`**

**2. CSV** (para tabelas): **`-o tabelas.csv`**

**Processamento em Lote**

Para processar vários arquivos de uma vez:

```bash
for file in *.pdf; do python main.py "$file" -o "${file%.pdf}.json"; done
```

## Limitações Conhecidas

1. PDFs digitalizados (imagens) requerem OCR não implementado

2. Layouts complexos podem afetar a extração de texto

3. Tabelas com células mescladas podem não ser extraídas corretamente

## Solução de Problemas

**Erro: "File not found"**

- Verifique se o caminho do arquivo está correto
- Use caminhos absolutos se necessário

**Erro: "PDF is encrypted"**

- O PDF está protegido por senha (não suportado atualmente)

**Extração incompleta**
- Experimente usar o modo verboso (-v) para identificar problemas
- Para PDFs complexos, considere pré-processar com outras ferramentas

## Roadmap e Melhorias Planejadas

1. Suporte a PDFs protegidos por senha
2. Integração com OCR para documentos digitalizados
3. Exportação para formatos adicionais (XML, SQL)
4. Reconhecimento automático de tipos de documento (faturas, contratos)
5. Interface web/REST opcional

## Contribuição

Contribuições são bem-vindas! Siga os passos:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/incrivel`)
3. Faça commit das mudanças (`git commit -am 'Adiciona feature incrível'`)
4. Faça push para a branch (`git push origin feature/incrivel`)
5. Abra um Pull Request

## Contato

Para dúvidas ou sugestões, entre em contato com:

**Nome:** Bruno

**Email:** brunorochape.contato@gmail.com

**Issues:** https://github.com/bruno-pereira7/python_estruturador-pdf/issues
