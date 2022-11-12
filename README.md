# Django Funcionarios

# Sobre o projeto

https://django-funcionarios.herokuapp.com/

O projeto funcionarios é uma aplicação web full stack desenvolvida em django.

A aplicação consiste em um CRUD de funcionarios e seus respectivos departamentos.

A página principal exibe uma lista completa de funcionarios cadastrados no sistema, também possui links para uma página detalhada do funcionario selecionado, link para edição de dados e exclusão de funcionario.


## Layouts

#### Home
![web_home](https://github.com/Vinicius-Bitencourt-Pereira/project-assets/blob/main/funcionarios/imgs/home.PNG)

#### Detalhes
![web_datail](https://github.com/Vinicius-Bitencourt-Pereira/project-assets/blob/main/funcionarios/imgs/detail.PNG)

#### Adicionar
![web_create](https://github.com/Vinicius-Bitencourt-Pereira/project-assets/blob/main/funcionarios/imgs/create.PNG)

#### Atualizar
![web_update](https://github.com/Vinicius-Bitencourt-Pereira/project-assets/blob/main/funcionarios/imgs/update.PNG)

#### Deletar
![web_delete](https://github.com/Vinicius-Bitencourt-Pereira/project-assets/blob/main/funcionarios/imgs/delete.PNG)


## Modelo conceitual

![diagram](https://github.com/Vinicius-Bitencourt-Pereira/project-assets/blob/dba586c521e2fc4b38b2a9ed417d7c1de067de0e/funcionarios/imgs/diagram.PNG)


# Tecnologias utilizadas

## Back end
- Python
- Django
- Postgre
- Sqlite3

## Front end
- HTML 5
- CSS 3
- Javascript
- Bootstrap 4

# Implatação em produção
- Heroku

# Como executar o projeto

Pré-requisitos: Python > 3.7

``` bash
# clonar repositório
git clone git@github.com:Vinicius-Bitencourt-Pereira/django-funcionario.git

# entrar na pasta do projeto
cd django-funcionario/

# criar um venv na raiz do projeto e ativar
    # Windows
    python -m venv venv
    source venv/script/activate

    # Linux
    python3 -m venv vevn
    source venv/bin/activate

# instalar as dependências
pip install -r requirements.txt

# fazer as migrações para o banco
python manage.py migrate

# criar um super usuario
python manage.py createsuperuser

# Exemplo...
    # usuario
    admin
    # email
    admin@email.com
    # senha
    admin
    # repetir senha
    admin

# rodar o servidor
python manage.py runserver

# Entrar na area administrativa e adicionar os departamentos por lá
http://127.0.0.1:8000/admin

# voltar para a home 
http://127.0.0.1:8000/
```

# Autor

Vinícius Bitencourt Pereira

https://www.linkedin.com/in/vin%C3%ADcius-bitencourt-pereira-2b666b221/
