from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.dialects.mysql.base import VARCHAR, LONGTEXT, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
def db_starter():
	engine = create_engine('mysql://root:FlickHub123@localhost:3306/flickhub', convert_unicode=True, echo=False)
	connection = engine.connect()
	
	Session = sessionmaker(bind=engine)
	session = Session()
	Base = declarative_base()
	metadata = MetaData()
	return (connection)
