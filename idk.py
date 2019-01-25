# class Student:
#     name = ""
#     grade = 0
#     attendance = 2
#
#     def printAll(self):
#         print(self.name, self.grade, self.attendance)
#
# newStudent1 = Student()
# newStudent2 = Student()
# newStudent1.name = "Kenn"
# # newStudent2.name = "Kevin"
# newStudent1.blah = "Something?"
#
# # print(newStudent1.name)
# # print(newStudent2.grade)
# newStudent1.printAll()
# # newStudent2.printAll()

class Car:

        def __init__(self, year=0, make="", model=""):
            self.make = make
            self.model = model
            self.year = year


        def __str__(self):
            return(f"The car is a {self.year} {self.make} {self.model}")

newCar1 = Car()
newCar2 = Car(2010)
newCar3 = Car(2010, "Ford")
newCar4 = Car(2010, "Ford", "F150")

print(newCar1)
print(newCar2)
print(newCar3)
print(newCar4)