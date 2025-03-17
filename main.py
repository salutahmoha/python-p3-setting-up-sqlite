from connect import engine
from sqlalchemy.orm import Session

session = Session(bind=engine)