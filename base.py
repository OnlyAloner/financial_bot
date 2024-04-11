""" Module to describe database structure """

import os
from dotenv import load_dotenv

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Date, Numeric
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
load_dotenv()

class Transaction(Base):
    """ Class to represent the transactions table """
    __tablename__ = 'transactions'
    id = Column(UUID, primary_key=True)
    category = Column(String)
    amount = Column(Numeric(14, 2))
    note = Column(String)
    created_at = Column(Date)

def create_tables(engine):
    """ Create tables in the database """
    Base.metadata.create_all(engine)
    print('Tables created successfully!')

def get_engine():
    """ Get database engine """
    user = os.getenv('PSQL_USER')
    pwd = os.getenv('PSQL_PWD')
    host = os.getenv('PSQL_HOST')
    port = os.getenv('PSQL_PORT')
    db = os.getenv('PSQL_DB')

    print(f'postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}')
    engine = create_engine(
        f'postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}'
    )
    print('Create engine')

    create_tables(engine)
    return engine
