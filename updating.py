from main import session
from models import Course, Student

course = session.query(Course).filter_by(id=5).first()
course.coursename = 'Sqlalchemy'

session.commit()