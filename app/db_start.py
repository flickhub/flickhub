from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.dialects.mysql.base import VARCHAR, LONGTEXT, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import database_url
import sqlalchemy
def db_starter():
	engine = create_engine(database_url, convert_unicode=True, echo=False)
	connection = engine.connect()
	
	Session = sessionmaker(bind=engine)
	session = Session()
	Base = declarative_base()
	metadata = MetaData()
	return (connection)
