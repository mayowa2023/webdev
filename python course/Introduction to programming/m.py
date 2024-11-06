class person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def showinfo(self):
        print("My name is", self.name,"I am of the gender", self.gender)

class student(person):
    def __init__(self,name,gender,grade,age):
        self.grade=grade
        self.age=age
        person.__init__(self,name,gender)
student1=student("Faith", "Female", "10", "12")

student1.showinfo()

print("I am in grade", student1.grade)