from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Numeric, Table, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://christopherhoudlette:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
	__tablename__ = "items"
	
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	description = Column(String)
	start_time = Column(DateTime, default=datetime.utcnow)
	
	seller_id = Column(Integer, ForeignKey('User.id'),)
	
class User(Base):
	__tablename__ = "users"
	
	id = Column(Integer, primary_key=True)
	username = Column(String, nullable=False)
	password = Column(String, nullable=False)
	
	sellitem = relationship('Item', uselist=False, backref='User',)
		
class Bid(Base):
	__tablename__ = "bids"
	id = Column(Integer, primary_key=True)
	price = Column(Numeric, nullable=False)

	
Base.metadata.create_all(engine)