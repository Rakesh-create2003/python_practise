# # # ####
# # names =["gowtham","Rakesh","anu","lakshana","madesh"]
# # print(names)
#
# # # ####
# # for test in names:
# #    print(test.upper())
#
# # # ####
#
# # correct_pin="6369899575"
# # entered_pin=""
# # while entered_pin!=correct_pin:
# #    entered_pin=input("enter your correct pin:")
# # print("access granted")
#
# # # ########
#
# fruits=["apple","banana","orange","mango"]
# for fruit in fruits:
#    print(fruit)
#
# # ########
#
# for i in range(10):
#    print(i)
#
# # ###########################
# #
# for i in range(10):
#    if i==7:
#       break
#    print(i)

# ############
# numbers=[1,2,3,4,5,6,8,7,10]
# for i in numbers:
#    if i==5:
#       break
#    print(i)
#
# ###############
# numbers=[10,9,-2,5,-7]
# for num in numbers:
#     if num > 0:
#        continue
#     print(num)
#
# numbers=[10,5,-2,8,-3]
# for num in numbers :
#    pass #future logic implementation.

# count=10
#
# while count > 5:
#    print(f"countdown: {count}")
#    count -=1
# print("time's up!")

items=[]

while True:
    item = input("Add item type done to finish: ")
    if item.lower()=="success":

        break
    items.append(item)
print("Items in cart :", items)






