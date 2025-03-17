from main import session

from models import Student

John = session.query(Student).filter(Student.studentname == 'John Doe').first()
print(John)