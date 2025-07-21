#this code is part of a Python script that handles exceptions
# and performs some calculations related to a restaurant's menu items.  

# Welcome to zomato
# number_of_items=int(input("How many items:"))
# total_price=200*number_of_items
# print(total_price)
# average_price= total_price/number_of_items
# print("average price is",average_price )


## The code below is modified to handle exceptions gracefully
# It will catch exceptions that occur when the user inputs an invalid number of items.
# try:
#     number_of_items = int(input("How many items: "))
#     total_price = 200 * number_of_items
#     print("Total price is:", total_price)
#     average_price = total_price / number_of_items
#     print("Average price is:", average_price)

# except Exception:
#     print("you cannot order 0 items")
# # except FileNotFoundError:
# #     print("File not found error occurred")
# # except ValueError:
#     # print("Invalid input! Please enter a valid number of items.")

# finally:
#     print("Thank you for using our service!")    

# print("Next code Block")        



#if-else only checks known problems
number_of_items=int(input("Enter the value:"))
if number_of_items==0:
    print("cannot divide by zero")
else:
    print(200/number_of_items) 

    
