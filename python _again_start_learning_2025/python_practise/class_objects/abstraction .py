from abc  import ABC, abstractmethod


class featureplan(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout2(self):
        pass

    @abstractmethod     
    def checkout(self):
        pass


class webapp(featureplan):
    def login(self):
        print("Login to web application")

    def logout2(self):
        print("Logout from web application")


    def checkout(self):
        print("Checkout in web application")


w=webapp()
w.logout2()
w.login()
w.checkout()