# Python com FastApi
Projeto desenvoldo para pratica de desenvolvimento com python

## Tecnologias

* Python
* SQLAlchemy
* FastApi
* Docker

## Preparando o ambiente
  A versão do python utilizada foi a 3.12

  Ambiente virtual
  ```bash
    python3 -m venv venv ;
    source venv/bin/activate ;
    pip install -r ./requirements.txt ;
  ```

  Container
  Nescessario um banco Postgres na maquina local, recomendamos o uso do docker.

  Altere o arquivo core/configs com usuario, senha, intancia de banco e porta

  Criando tabelas
  ```bash
    python criar_tabelas.py
  ```

  Lista de pacotes utilizados
  * pip install fastapi==0.75.2
  * pip install psycopg2-binary==2.9.3
  * pip install SQLAlchemy==1.4.36 
  * pip install asyncpg
  * pip install uvicorn==0.17.6
  * pip install python-jose[cryptography]
  * pip install pytz==2022.01 
  * pip install passlib==1.7.4
  * pip install python-multipart==0.0.5
  * pip install pydantic[email]


  Apos todas as depedencias reinstaladas rode o comando 
 ```bash
    python main.py
```