# djangoProject
Projeto onde podes inserir notícias, ver todas as notícias guardas e filtrar por tag. A base de dados usada é o mongoDB. 

# packages utilizadas
asgiref             3.5.0
certifi             2021.10.8
cffi                1.15.0
charset-normalizer  2.0.12
cryptography        36.0.1
defusedxml          0.7.1
Django              2.2
django-allauth      0.48.0
django-crispy-forms 1.14.0
djongo              1.3.6
idna                3.3
oauthlib            3.2.0
pip                 22.0.3
pycparser           2.21
PyJWT               2.3.0
pymongo             3.12.1
python3-openid      3.2.0
pytz                2021.3
requests            2.27.1
requests-oauthlib   1.3.1
setuptools          60.6.0
sqlparse            0.2.4
urllib3             1.26.8
wheel               0.37.1

Podes instalar a partir do pip
Podes criar uma variável para guardar as configurações ou instalar globalamente

# criar collections na base de dados
python manage.py migrate
python manage.py makemigrations

# correr o site
python manage.py runserver
