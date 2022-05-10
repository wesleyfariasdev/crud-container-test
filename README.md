# Desafio
O sistema deverá ser uma aplicação WEB, conter um banco de dados estruturado (SQL) e tecnologias e ferramentas utilizados ficam a critério do(a) candidato(a).
O processo de desenvolvimento deverá ser gravado e não apenas a apresentação do produto final.

São requisitos funcionais da aplicação:
# Crud Cliente
- Email
- Nome
- CNPJ

# Crud de Contêiner
- Cliente
- Número do contêiner (4 letras e 7 números. Ex: TEST1234567)
- Tipo: 20 / 40
- Status: Cheio / Vazio
- Categoria: Importação / Exportação 

# Crud de Movimentações
- Tipo de Movimentação (embarque, descarga, gate in, gate out,
reposicionamento, pesagem, scanner)
- Data e Hora do Início
- Data e Hora do Fim

# Relatório
- Relatório com o total de movimentações agrupadas por cliente e tipo de movimentação.
- No final do relatório deverá conter um sumário com o total de importação / exportação.

# Premissas para todos os artefatos:
- O leiaute dos controles de manutenção dos dados não precisa ser de um CRUD padrão.
- Pode sentir-se à vontade para criar mecanismos de interação mais criativos e funcionais.
- Validações
- Ordenações
- Filtros

# Sobre o projeto

## Como rodar:
Clone ou faça download do projeto

```sh
https://github.com/Ssousuke/crud-container.git
```


Pelo Terminal, dentro da pasta do projeto, crie um ambiente virtual

```sh
Windows: python -m venv venv
Linux: python3 -m venv venv
```

Ative o ambiente virtual
```sh
Windows: venv\Scripts\Activate
Linux: source ./venv/bin/activate
```
Instale as dependencias
```sh
pip install -r requirements.txt
```

## Migrações

Após a configuração do ambiente, você pode em seguida fazer o processo de migração.
```sh
python manage.py makemigrations
python manage.py migrate
```
