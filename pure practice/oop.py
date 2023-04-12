#oop
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def get_grade(self):
        return self.grade
class Course:
    def __init__(self,name,max_student):
        self.name=name
        self.max_student=max_student
        self.student=[]

    def add_student (self,student):
        if len(self.student)<self.max_student:
            self.student.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.student:
          value += student.get_grade()
        return value/len(self.student)
s1=Student("Tim",19,95)
s2=Student("jill",19,75)
s3=Student("Bill",19,65)

course =Course("science",2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.get_average_grade())
