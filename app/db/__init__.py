from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g
import os

load_dotenv()# Load environment variables from .env file

# connect to database using env variable
engine = create_engine(f"postgresql+psycopg2://postgres:{os.getenv('DB_PW')}@localhost/python_news_db")
# engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)

Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db(app):
  Base.metadata.create_all(engine)

  app.teardown_appcontext(close_db)

def get_db():
  if 'db' not in g:
    # store db connection in app context
    g.db = Session()

  return g.db

def close_db(e=None):
  db = g.pop('db', None)

  if db is not None:
    db.close()