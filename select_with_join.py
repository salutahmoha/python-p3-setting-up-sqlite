# from main import session
# from models import Course, Student
# from sqlalchemy import select

# joining = select(Student).join(Student.course).where (
#     Course.coursename == 'python'
# ).where(
#     Student.studentname == 'Brian'
# )

# result = session.scalars(joining).all()

# print(result)

# # select studentname, coursename from students INNER JOIN courses ON courses.course_id = students.course_id