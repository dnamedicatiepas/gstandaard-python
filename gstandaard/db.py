from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base
from config import database

engine = create_engine('sqlite:///%s' % database, echo=False)

Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
session.commit()
