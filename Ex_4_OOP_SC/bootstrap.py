# =============== Imports
from Course import Course
from Student import Student


# ============== Initialization =============
courseObj = Course()
student = Student(courseObj)

# =============== Driver ================
student.set_name("Ahmed")
# print(student.get_avg())
print(student.get_avg_v2())
