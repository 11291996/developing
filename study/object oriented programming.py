#object oriented prgramming: easy to manipulate complicated code, but computation takes longer. Example follows
#declarative programming: enhances os, ex: db languages. imperative programming: uses os, ex: python
#oop uses class -> idea, and object -> real thing
#class has method -> action that the object will do, and attributes -> the state of the object
#Use class 'Dog' as an example 

class Dog:

    def __init__(self): #initiate the class, self refers to the obejct itself
        pass #pass does not do anything

ozzy = Dog() #ozzy is an object of class 'Dog' now 

#now put some attributes in this class 

print(ozzy)

class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age #the obect's attributes are the class's attribute 
    
ozzy = Dog('Ozzy', 2)

#then from this Ozzy's attributes can be returned

print(ozzy.name, ozzy.age)

#now put some methods in the class 

class Dog:
    
    def bark(self):
        print('bark bark!')

ozzy = Dog()

ozzy.bark()

#passing attributes to methods 

class Dog:

    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def birthday(self):
        self.age +=1

    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self

#now one can use methods with attributes 

ozzy = Dog("Ozzy", 2)
filou = Dog("Filou", 8)

ozzy.setBuddy(filou)

print(ozzy.buddy.name)
print(ozzy.buddy.age)