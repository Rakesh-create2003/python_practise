####
age=18
if age>20:
    print("you are major")
else:
    print("you are minor")

####
age=15
if age>= 18:
    print("you can vote")
else:
    print("you can't vote")

######
marks=30
if marks>=90:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("Fail")


######
age=17
has_license="no"
if age>=18:
    if has_license == "yes":
        print("you can drive")
    else:
        print("go and take license")
else:
    print("you are too young drive")

#####
mark=80
attendance=50
if mark>=55 and attendance>=70:
    print("Alloweded for exam")
else:
    print("not alloweded")

######
recharge_amount=399
data_balance=1.5
if recharge_amount >= 399 and data_balance >= 1.5:
    print("you are eligible for bonus")
else:
    print("you are not eligible for bonus")

#####
order_amount=100
days="mon"
membership="no"

if (order_amount>=1000 and days in ["sat","sun"]) or membership=="yes":
    print("20% discount")
else:
    print("no discount")


