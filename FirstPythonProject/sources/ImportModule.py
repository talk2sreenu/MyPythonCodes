'''
Created on Apr 20, 2020

@author: talk2
'''
from sources import MyFirstClass

p1 = MyFirstClass.Person("Hello", 45)

print("From Module : "+ p1.printNameAge())

p2 = MyFirstClass.Student("How are you", 50)

print("From Module : "+ p2.printNameAge())