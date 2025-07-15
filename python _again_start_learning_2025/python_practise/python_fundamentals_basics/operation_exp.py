#x=10
#print(x)


#Arithmetic
a=10
b=3
print(a+b)   #add
print(a-b)   #sub
print(a*b)   #multiplication
print(a/b)   #division
print(a%b)   #module
print(a**b)  #exponentiation
print(a//b)  #floor division

#comparison
x=5
y=10
print(x==y)
print(x!=y)
print(x>y)
print(x<y)

#Logical
g=True
h=False
print(g and h)
print(g or h)
print(not g)
print(not h)

#experission
amount=1200
tax=amount*0.18
print(tax)
total=amount+tax
print(total)

if total >1000:
    discount=total*0.10
    c=total-discount
    print(c)

####
age=50
student="no"
if age>=65 or student=="yes":
    print("yes discount")
else:
    print("no discount")

####
age=60
student="yes"

if age>=60 or student==("no"):
    print("yes discount")
else:
    ("no discount")


