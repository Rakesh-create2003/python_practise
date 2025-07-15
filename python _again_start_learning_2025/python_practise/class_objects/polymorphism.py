# polymorphism is a concept in object-oriented programming where objects of different classes can be used interchangeably,
# and the behavior of the objects is determined by the class they belong to.
# polymorphism is also known as over riding and over loading in other programming languages
#polymorphism is a small concept in python.
#it is a over riding
class dad:  #parent class
    def house(self):
        print(("red house"))

class daughter(dad):  #child class
    def factory(self):
        print(("blue factory"))

    def house(self):
        print(("yellow class"))


d=daughter()
d.house()       
d.factory()  # calling the factory method from daughter class