# inheritance is a way to form new classes using classes that have already been defined. 
# The new class is a derived class, and the classes it inherits from are base classes.

# class dad:  #parent class
#     def house(self):
#         print(("I am from dad class"))


# # s1 = dad()
# # s1.house()       



# class son(dad):   # child class

#     def factory(self):
#         print("I am from test class")


# s=son()
# s.house()
# s.factory() #single level inheritence


# # t=test()
# t.factory()        



# class app1:
#     def v1(self):
#         print("I am from app1 class")

# class app1_1(app1):
#     def v2(self):
#         print("I am from app1_1 class")


# a=app1_1()
# a.v1()
# a.v2()  #single level inheritence   



# class app1:
#     def v1(self):
#         print("orders")

# class app1_1(app1):
#     def v2(self):
#         print("refund")

#     def v3(self):
#         print("cancel") 

#     def v1(self):
#         print("orders updated")


# a=app1_1()
# a.v1()
# a.v2()        
# a.v3()  #multilevel inheritence 


# class dad:
#     def house(self):
#         print("Red")

# class son(dad):
#     def factory(self):
#         print("Blue")

#     def house(self):
#         print("green")

# # d=dad()
# # d.house()          
# s=son()
# s.factory()
# s.house()  #method overriding   

'''' #correct single level inheritence.
class dad:
    def house(self):
        print("Red")    

# d=dad()
# d.house()  #parent class method       


class son(dad):  # child class
    def factory(self):
        print("Blue")

s=son()
s.factory()  # child class method
s.house()  # inherited method from parent class 
'''
'''# Example of multilevel inheritance

# class grandfather():
#     def land(self):
#         print("I have a big land")

# class father(grandfather):
#     def house(self):
#         print("I have a small house")       

# class son(father):
#     def factory(self):
#         print("I have a very small factory")   

# s=son()
# s.factory()  # method from son class
# # s.house()    # inherited method from father class
# # s.land()     # inherited method from grandfather class      
'''

'''
#hierarchy
class dad:
    def house (self):
        print("house white")

class son1(dad):
    def factory (self):
        print("factory red")

class son2(dad):
    def apartment(self):
        print("apartment black")



s1=son1()
s1.factory()
s1.house()        


s2=son2()
s2.apartment()
s2.house()

'''


#multiple inheritence

class dad:
    def house (self):
        print("house white")

class mom:
    def factory (self):
        print("factory red")

class daughter(dad,mom):
    def apartment(self):
        print("apartment black")


d=daughter()
d.apartment()
d.factory()
d.house()



'''

a
b(a)
c(b) ----->multilevel inheritence



a
b
c(a,b)----->multiple inheritence

'''










