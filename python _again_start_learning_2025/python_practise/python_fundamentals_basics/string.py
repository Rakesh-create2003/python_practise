driver_name="rakesh"

print(driver_name)
print (driver_name.lower())
print(driver_name.upper())
print(driver_name.capitalize())
print(driver_name.isupper())
print(driver_name.islower())

mobile="6369899575"
masked=mobile[:2]+"******"+mobile[-2:]
print(masked)

song="shape OF you"
artist="RAKESH mr"
formated=f"{song.title()} - {artist.title()}"
print(formated)

location="chennai central"
fixed_location=location.replace("chennai central","Thambaram")
print(fixed_location)

message="your uber booking id is:ub12345.please keep it safe"
booking_id=message.split(":")[1] .split(".")[0].strip()
print(booking_id)

promo_message="use zomoto100 to get 100 off on your first order"
if "zomoto100" in promo_message:
    print("offered applied")


feedback="the driver was polite and the ride was smooth"
print("position is:",feedback.find("polite"))

name="Rakeshwar Ramesh"
initials="".join([word[0].upper() for word in name.split()])
print(initials)

dirty_input=" airport  "
clean=dirty_input.strip()
print(clean)

word1="the trip was amazing and the car was clean "
word_count=len(word1.split())
print(word_count)