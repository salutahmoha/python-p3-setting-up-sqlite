from models import Base

from connect import engine

print("Creating tables......")

Base.metadata.create_all(bind=engine)