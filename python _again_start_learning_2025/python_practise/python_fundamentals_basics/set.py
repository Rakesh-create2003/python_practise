# a=[1,2,3]
# print(type(a))  # Output: <class 'list'>
# print(a)  # Output: [1, 2, 3]

# b=set(a)    
# print(b)  # Output: {1, 2, 3}
# print(type(b))  # Output: <class 'set'> 


# uber_cities={"chennai", "bangalore", "mumbai", "delhi","chennai"}  # Duplicates are ignored in sets
# print(uber_cities)  # Output: {'chennai', 'bangalore', 'mumbai', 'delhi'}
# print(type(uber_cities))  # Output: <class

# unique_cities=set(uber_cities)  # Converting list to set to remove duplicates 'set'>
# print(unique_cities)  # Output: {'chennai', 'bangalore', 'mumbai', 'delhi'}
# print(type(unique_cities))  # Output: <class 'set'>


# uber_cities1={"chennai", "bangalore", "mumbai"}

# uber_cities2={"delhi", "pune", "hyderabad", "bangalore", "chennai"}

# print(uber_cities1.union(uber_cities2))  # Merging two sets


# print(uber_cities1.intersection(uber_cities2))  # Finding common elements

# print(uber_cities1.difference(uber_cities2))  # Finding elements in
# print(uber_cities2.difference(uber_cities1))  # Finding elements in uber_cities2 that are not in uber_cities1   

# uber_cities1.add("kolkata")  # Adding an element to the set
# print(uber_cities1)  # Output: {'chennai', 'bangalore', 'mumbai', 'kolkata'}
# print(type(uber_cities1))  # Output: <class 'set'>

# uber_cities1.remove("mumbai")  # Removing an element from the set
# print(uber_cities1)  # Output: {'chennai', 'bangalore', 'kolkata'}
# print(type(uber_cities1))  # Output: <class 'set        

# my_set = {1, 2, 3, 4, 5}
# print(my_set)  # Output: {1, 2, 3, 4, 5}
# my_set.remove(3)  # Removing an element from the set
# print(my_set)  # Output: {1, 2, 4, 5}
# my_set.add(6)  # Adding an element to the set   
# print(my_set)  # Output: {1, 2, 4, 5, 6}



my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
my_set.discard(3)  # Discarding an element from the set
print(my_set)  # Output: {1, 2, 4, 5}
