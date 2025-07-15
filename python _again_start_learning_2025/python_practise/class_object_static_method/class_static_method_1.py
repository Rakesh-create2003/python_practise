class employee:
    company="openAI"      #class level data

    @classmethod
    def change_company(cls,new_name):
        cls.company = new_name          #accessing class variable

    @staticmethod
    def try_change_company(new_name):
        company = new_name


#call both methods
employee.change_company("microsoft")
print("after classmethod:",employee.company)

employee.try_change_company("google")
print("after staticmethod:",employee.company)  # Output: google