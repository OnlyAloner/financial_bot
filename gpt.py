""" Module to integrate the llm model with the API """

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit

from base import get_engine

load_dotenv()

llm = ChatOpenAI(
  openai_api_key=os.getenv('OPENAI_API_KEY'),
  organization=os.getenv('OPENAI_ORGANIZATION_ID'),
  model_name='gpt-4-turbo-preview',
  temperature=0
)

engine = get_engine()

db = SQLDatabase(engine=engine)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

db_agent_toolkit = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
)
