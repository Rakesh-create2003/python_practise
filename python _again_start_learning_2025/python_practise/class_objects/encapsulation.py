class order:
    def __init__(self,customer_name,items,total_amount,discount):
        self.coustomer_name = customer_name                   #public
        self.items = items                                     #public
        self.__private_total_amount = total_amount            #private
        self.__private_discount = discount                     #private


    def __calculate_total(self):                #private helper method
        return self.__private_total_amount -  self.__private_discount

    def _get_admin_view(self):
        return {
            "customer_name": self.coustomer_name,
            "items": self.items,
            "total_amount": self.__private_total_amount,
            "discount": self.__private_discount,
            "final_amount": self.__calculate_total()
        }

    def _get_customer_view(self):
        return {
            "customer_name": self.coustomer_name,
            "items": self.items,
            "final_amount": self.__calculate_total()
        }
    

class adminportal:
    def show_order(self,order):
        return order._get_admin_view()             #allowed but protected

class customerportal:
    def show_customer_order(self, order):
        return order._get_customer_view()          #safe public method
    

order = order(customer_name="rakesh", items=["item1", "item2"], total_amount=100, discount=10)

admin = adminportal()
customer = customerportal()


print("admin view")
print(admin.show_order(order))

print("customer view")
print(customer.show_customer_order(order))  