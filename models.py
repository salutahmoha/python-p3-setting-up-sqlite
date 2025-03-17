from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey
from typing import List,Optional

class Base(DeclarativeBase):
    pass

class Course(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(unique=True, autoincrement=True)
    coursename: Mapped[str] = mapped_column(nullable=False)
    course_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    students: Mapped[List["Student"]] = relationship(back_populates="course")

    def __repr__(self):
        return f"Course(id={self.id}, coursename={self.coursename}, course_id = {self.course_id})"

class Student(Base):
    __tablename__ = "students"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    studentname: Mapped[str] = mapped_column(nullable=False)
    regNo: Mapped[str] = mapped_column(unique=True, nullable=False)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.course_id"))

    course: Mapped[Optional["Course"]] = relationship(back_populates="students")

    def __repr__(self):
        return f"Student(id={self.id}, studentname = {self.studentname}, regNo = {self.regNo}, course_id = {self.course_id})"