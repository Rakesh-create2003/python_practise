class parent:
    def public_method(self):
        print("This is a public method.")

    def _protected_method(self):
        print("This is a protected method.")

    def __private_method(self):
        print("This is a private method.")

    def access_from_same_class(self):
        print("Accessing from the same class:")
        self.public_method()
        self._protected_method()
        self.__private_method()

p = parent()
p.access_from_same_class()


class child(parent):
    def access_from_sub_class(self):
        print("Accessing from the subclass:")
        self.public_method()
        self._protected_method()
        try:
            self.__private_method()
            # self._parent__private_method() # name mangling
        except AttributeError:
            print("private: Cannot access private method from outside the class")

c = child()
c.access_from_sub_class()



class stranger:
    def access_from_other_class(self,obj):
        print("Accessing from the stranger class:")
        obj.public_method()
        obj._protected_method()
        try:
            obj.__private_method()
            # obj._parent__private_method()  #name mangling
        except AttributeError:
            print("private: Cannot access private method from outside the class")

s = stranger()
s.access_from_other_class(p)    