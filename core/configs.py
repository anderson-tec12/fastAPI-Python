from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
   API_V1_STR: str = '/api/v1' 
   DB_URL:str = 'postgresql+asyncpg://docker:docker@localhost:5432/apisolid'
   DBBaseModel = declarative_base()

   JWT_SECRET: str = 'B3bF7Z_5rcsJfnqWDGS7kBPqMoJrtrH1oIAFtesM5Kk'

   """ JWT_SECRET gerado via terminal python
    import secrets
    token: str = secrets.token_urlsafe(32)
   """
   ALGORITHM: str = 'HS256'
   ACCESS_TOKEN_EXPIRE_MINUTES:int = 60 * 24 * 7  #valido por uma semana


   class Config:
      case_sensitive = True 

settings:Settings = Settings()