class Student :
    def __init__(self,name,age,gender,level,grades):
        self.name = name
        self.age = age
        self.gender = gender
        self. level = level
        self.grades = grades

    def display(self):
        print ( self.name,
                self.age,
                self.gender,
                self.level,
                self.grades)

John = Student("John",15, 'boy' , 3, 'Good')

John.display()