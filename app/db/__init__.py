from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os





load_dotenv()



# connect to database using env variable
engine = create_engine(f"postgresql+psycopg2://postgres:{os.getenv('DB_PW')}@localhost/python_news_db")
# engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)

Session = sessionmaker(bind=engine)
Base = declarative_base()