# CMPaaS
Repositório Oficial do Projeto CMPaaS

### Instruções para rodar o projeto

* Baixe os arquivos do repositório
* Crie um *virtual enviroment* (virtualenv)

```
python3 -m venv env
```

* Ative o virtualenv

```
source env/bin/activate
```

* Instale as depêndencias

```
pip install -r requirements.txt
```

* Crie seu usuario

```
python manage.py createsuperuser
```

* Crie o banco de dados

```
python manage.py makemigrations
python manage.py migrate
```

* Rode o servidor na porta 8000

```
python manage.py runserver 0.0.0.0:8000
```

* Abra o navegador e acesse o admin (localhost:8000/admin)
