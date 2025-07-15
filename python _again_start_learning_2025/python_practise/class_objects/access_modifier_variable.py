class parent:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__private_var = "I am private"


    def access_from_same_class(self):
        print("Accessing from the same class:")
        print("public:", self.public_var)
        print("protected:", self._protected_var)
        print("private:", self.__private_var)


class child(parent):
    def access_from_sub_class(self):
        print("Inside Child class (subclass):")
        print("public:", self.public_var)
        print("protected:", self._protected_var)

        try:
            print("private:", self.__private_var)
            # print("private:", self._parent__private_var)
        except AttributeError:
            print("private: Cannot access private variable from outside the class")

class stranger:
    def access_from_stranger(self, obj):
        print("Inside Stranger class:")
        print("public:", obj.public_var)
        print("protected:", obj._protected_var) #Not recommended to access protected members from outside the class



        try:
            print("private:", obj.__private_var)
            # print("private:", obj._parent__private_var)   (name mangling)
        except AttributeError:
            print("private: Cannot access private variable from outside the class")            

p=parent()

c=child()

s=stranger()

p.access_from_same_class()

c.access_from_sub_class()

s.access_from_stranger(p)