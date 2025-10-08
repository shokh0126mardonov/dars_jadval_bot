from sqlalchemy import URL,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

from config import DB_HOST,DB_NAME,DB_PASSWORD,DB_PORT,DB_USER

url_object = URL.create(
    "postgresql+psycopg2",
    password=DB_PASSWORD,
    port=DB_PORT,
    host=DB_HOST,
    username=DB_USER,
    database=DB_NAME
)

engine = create_engine(url_object)
LocalSession = sessionmaker(bind=engine)

Base = declarative_base()
