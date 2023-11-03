
(OBSERVAÇÃO: GITHUB TEMPORÁRIO, SERÁ TRANSFERIDO PARA O "PRINCIPAL", TIVE UM PROBLEMA DE ACESSO PARA ATUALIZAR OS ARQUIVOS E NÃO DARÁ TEMPO DE RESOLVER ANTES DA ATIVIDADE FECHAR)

# Prática TDD - Projeto de Cadastro de Livros

Este é um projeto de desenvolvimento web que inclui um sistema de cadastro de livros, com ênfase na prática do Desenvolvimento Orientado a Testes (TDD). O projeto foi desenvolvido como parte dos desafios da disciplina "Desenvolvimento Web 3" e "Qualidade e Teste de Software".

## Requisitos da Sprint 1

- Cadastro de livros com campos: Título e Editora.
- Rota raiz (/) com botões para acessar cadastro e listagem.
- Rota para listar os livros (/listar).
- Testes unitários que passam e sistema funcional para a primeira sprint.

## Requisitos da Sprint 2

Nesta segunda sprint, foram implementadas as seguintes melhorias:

- Novos campos para livros: Autor, ISBN, Número de Páginas, Ano em que a obra foi escrita.
- Validação dos campos de acordo com as regras definidas:
  - Título: Pelo menos 3 caracteres.
  - Editora: Pelo menos 3 caracteres.
  - Autor: Pelo menos 10 caracteres.
  - ISBN: Exatos 13 caracteres numéricos.
  - Número de Páginas: Entre 1 e 3 caracteres numéricos.
  - Ano: Exatos 4 caracteres numéricos.
- Todos os campos mencionados acima se tornaram obrigatórios.
- Ajustes nos testes para acomodar os novos requisitos.

## Pré-requisitos

Certifique-se de ter o ambiente configurado corretamente antes de executar o projeto. Você pode seguir as instruções fornecidas no início deste README para configurar o ambiente no Linux ou no Windows.

## Como Executar o Projeto

### No ambiente Linux:

1. Clone o repositório:
git clone https://github.com/orlandosaraivajr/Pratica_TDD_1.git
cd Pratica_TDD_1/

2. Configure o ambiente virtual:
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt

3. Navegue até a pasta `biblioteca`:
cd biblioteca/

4. Realize as migrações e execute os testes:
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test
coverage html

5. Inicie o servidor:
python manage.py runserver

### No ambiente Windows:

1. Clone o repositório:
git clone https://github.com/orlandosaraivajr/Pratica_TDD_1.git
cd Pratica_TDD_1/

2. Configure o ambiente virtual:
virtualenv venv
cd venv
cd scripts
activate.bat
cd ..
cd ..
pip install -r requirements.txt

3. Navegue até a pasta `biblioteca`:
cd biblioteca/

4. Realize as migrações e execute os testes:
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test
coverage html

5. Inicie o servidor:
python manage.py runserver

## Uso
- Acesse a rota raiz (/) para acessar as opções de cadastro e listagem de livros.
- Para cadastrar um livro, acesse a rota de cadastro (/cadastro) e preencha os campos obrigatórios e os novos campos conforme as regras de validação.
- Use a rota de listagem (/listar) para verificar os livros cadastrados.

## Contribuição
Este projeto foi desenvolvido como parte de um desafio acadêmico. Contribuições são bem-vindas, mas lembre-se de manter a prática de TDD e aderir às regras de validação estabelecidas.
