from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Paritosh Pal"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, description="CGPA must be between 0 and 10", default=5)




new_student = {'age': '25', 'email': "avvc@gmail.com"}

student = Student(**new_student)

student_dict = dict(student)
student_json = student.model_dump_json()

print(student_dict['age'])