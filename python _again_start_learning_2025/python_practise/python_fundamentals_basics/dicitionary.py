trip={
    "trip_id":"uber-12345",
    "driver_name":"John Doe",
    "vehicle_type":"Sedan",
    "status":"Completed",
    "pickup_location":"chennai",
    "dropoff_location":["bangalore","hyderabad","pune","medavakkam"],  # Using a list to allow multiple dropoff locations
    "fare": 1500.75,
    "passenger_count": 2,
    "rating": 4.8,
    "trip_id": "uber-12903345"  # Duplicate key, will not raise an error but will overwrite the previous value 
}

# print(trip)  # Output: {'trip_id': 'uber-12345', 'driver_name': 'John Doe', 'vehicle_type': 'Sedan', 'status': 'Completed', 'pickup_location': 'chennai', 'dropoff_location': 'bangalore', 'fare': 1500.75, 'passenger_count': 2, 'rating': 4.8}
# print(type(trip))  # Output: <class 'dict'>

# print("Trip ID:", trip["trip_id"])  # Accessing value using key
# print(trip.get("driver_name"))  # Accessing value using get method
# print(trip.get(2))  # Accessing value using get method with a non-existent key, returns None

# print(trip.keys())  # Output: dict_keys(['trip_id', 'driver_name', 'vehicle_type', 'status', 'pickup_location', 'dropoff_location', 'fare', 'passenger_count', 'rating'])

# print(trip.values())  # Output: dict_values(['uber-12345', 'John Doe', 'Sedan', 'Completed', 'chennai', 'bangalore', 1500.75, 2, 4.8])

# print(trip.items())  # Output: dict_items([('trip_id', 'uber-12345'), ('driver_name', 'John Doe'), ('vehicle_type', 'Sedan'), ('status', 'Completed'), ('pickup_location', 'chennai'), ('dropoff_location', 'bangalore'), ('fare', 1500.75), ('passenger_count', 2), ('rating', 4.8)]   )

# for key, value in trip.items():
    # print({key: value})  # This will not raise an error because trip is a dictionary, not a list of tuples  


# trip.update({"car_model":"benz"})  # Adding a new key-value pair to the dictionary
# print(trip)  # Output: {'trip_id': 'uber-12345', 'driver_name': 'John Doe', 'vehicle_type': 'Sedan', 'status': 'Completed', 'pickup_location': 'chennai', 'dropoff_location': 'bangalore', 'fare': 1500.75, 'passenger_count': 2, 'rating': 4.8, 'car_model': 'benz'}
# trip.pop("trip_id")  # Removing a key-value pair from the dictionary
# print(trip)

# trip.update({"trip_id":"uber-636989"})
# print(trip)  # Output: {'trip_id': 'uber-636989', 'driver_name': 'John Doe', 'vehicle_type': 'Sedan', 'status': 'Completed', 'pickup_location': 'chennai', 'dropoff_location': 'bangalore', 'passenger_count': 2, 'rating': 4.8, 'car_model': 'benz'}
# trip.clear()  # Clearing the dictionary
# print(trip)  # Output: {} 

# for key, value in trip.items():
    # print(f"{key}: {value}")  # This will print each key-value pair in the dictionary   

# print( trip["dropoff_location"][0])  # Accessing the first element of the dropoff_location list

# print( trip["dropoff_location"][1])  # Accessing the second element of the dropoff_location list

# for location in trip["dropoff_location"]:
    # print(location)  # This will print each dropoff location in the list
 

# trips=[
#     {"trip_id":"ub0001","pick_up":"chennai","drop":"airport","fare":430},
#     {"trip_id":"ub0002","pick_up":"chennai","drop":"mall","fare":500},
#     {"trip_id":"ub0003","pick_up":"chennai","drop":"office","fare":600},
#     {"trip_id":"ub0004","pick_up":"chennai","drop":"home","fare":700},
#     {"trip_id":"ub0005","pick_up":"chennai","drop":"school","fare":800}
# ]

# for trip in trips:
#     print(trip["trip_id"])

trips= {
    "ub0001": {"pick_up":"chennai","drop":"airport","fare":430},
    "ub0002": {"pick_up":"chennai","drop":"mall","fare":500},
    "ub0003": {"pick_up":"chennai","drop":"office","fare":600},
    "ub0004": {"pick_up":"chennai","drop":"home","fare":700},
    "ub0005": {"pick_up":"chennai","drop":"school","fare":800}
}

# print(trips["ub0001"]["fare"])


for trip_id,details in trips.items():
    print(trip_id)
    print(details["pick_up"],"->",details["drop"])
