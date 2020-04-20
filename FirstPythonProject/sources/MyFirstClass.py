'''
Created on Apr 20, 2020

@author: talk2
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printNameAge(self):
        print(self.name+","+str(self.age))
        return self.name+","+str(self.age)
    def exceptionHandling(self):
        try:
            #print(x)
            print('Hello')
        except:
            print("An Exception Occured")
        else:
            print("No Exception")
class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
        #super().__init__(name, age)

nameVal = input("Enter User Name")
ageVal = input("Enter Age Value")
#p1 = Person("Srinu", 30)
p1 = Person(nameVal, ageVal)
nameVal = input("Enter User Name")
ageVal = input("Enter Age Value")
#p2 = Student("Amrutha", 25)
p2 = Student(nameVal, ageVal)

print(p1.name)
print(p1.age)
p1.printNameAge()
print("Return value from function : " + p1.printNameAge())
print("Return value from Second Class : " + p2.printNameAge())
p1.exceptionHandling()
p2.exceptionHandling()