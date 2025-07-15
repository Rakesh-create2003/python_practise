# class student:
#     def __init__(self,fname, age):
#         self.name= fname
#         self.age= age

#     def display(self):
#         print("Name:", {self.name},"Age:", {self.age})
        
# s1=student("Rakesh", 25)
# s1.display()



# class employee:
#     def __init__(self,name,aadhaar):
#         self.name= name
#         self.aadhaar= aadhaar

#     def enter_office(self):
#         print(f"{self.name} entered using aadhaar {self.aadhaar}")

#     def open_bank_account(self):
#         print(f"{self.name} opened a bank account with aadhaar {self.aadhaar}")


# e1=employee("Rakesh", 65550315943)  
# e1.enter_office()  
# e1.open_bank_account()


class mathtool:

    def square(self, num):
        return num * num
    
    def cube(self, num):
        return num * num * num
    
tool = mathtool()
print(tool.square(2))
print(tool.cube(2))