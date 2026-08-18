# Implement the Person class
# code here
class Person():
    def __init__(self,name="Geeks",age=10):
        self.__name=name
        self.__age=age
    def set_name(self,newname):
        self.__name=newname
    def set_age(self,age):
        self.__age=age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
        
person=Person()
person.get_name()
person.set_name("John")
person.set_age(21)
person.get_name() 
person.get_age()