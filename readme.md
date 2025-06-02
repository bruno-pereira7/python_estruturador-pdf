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

**Issues:** https://github.com/bruno-pereira7/estruturador-pdf/issues
