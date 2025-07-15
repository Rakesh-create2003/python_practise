#instance_method    instanceor object 
# class_method
# static_method

class my_class:

    def instance_method(self):
        # instance method can access instance variables
       print("called instance method")

    @classmethod
    def class_method(cls):
        # class method can access class variables
        print("called class method")

    @staticmethod
    def static_method():
        # static method cannot access instance or class variables
        print("called static method")



obj = my_class()
obj.instance_method()  # Calling instance method
my_class.class_method()  # Calling class method     
my_class.static_method()  # Calling static method   


'''
#class method
class Employee:
    company_name = "openAI"      #class level data

@classmethod
def change_company(cls,new_name):
    cls.company_name = new_name


Employee.change_company("new_openAI")  # Changing class variable
print(Employee.company_name)  # Output: new_openAI  

'''


'''
#static method
class math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y
        
print(math.add(5, 3))        # Output: 8
print(math.subtract(5, 3))   # Output: 2

'''