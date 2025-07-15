import sys

full_name=sys.argv[1]

#format the name
email = full_name.lower().replace(_old: " ", _new:" .") + "@company.com"

#output
print("\n --- your profile ---")
print("Full Name:", full_name)
print("Generated Email:", email)