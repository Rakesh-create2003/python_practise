
#one file write file_handling:

# file = open("notes.txt", "w")
# file.write("Welcome to python\n")
# file.write("This is new file\n")
# file.close()




# #one file read file_handling:
# # Reading the file content
# file=open("notes.txt","r")
# content=file.read()
# print("file content:", content)
# file.close()    



# Appending to the file

# file=open("notes.txt", "a")
# file.write("Adding more content \n")
# file.close()

# # Reading the file content using a for loop
# with open("notes.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# # Feedback logging example:

# feedback=input("Enter your feedback: ") 

# with open("feedback_log.txt", "a") as log:
#     log.write(feedback + "\n")

# print("Feedback successfully")

# Reading the file content using a readline
# with open("data.txt", "r") as file:
#     print(file.readline().strip())
#     print(file.readline().strip())
#     print(file.readline().strip())
#     print(file.readline().strip())

 # Reading the file content using a while loop
# with open ("file.txt") as file:
#     while True:
#         line=file.readline()
#         if not line:
#             break
#         if "ERROR" in line:
#             print(f'found error: {line.strip()}')  # print(line.strip())

# Reading the file content using a for loop
# with open("file.txt") as file:
    # for _ in range(5):
#         print(file.readline().strip())

# Reading and writing CSV files
# with open ("content.csv", "r") as in_file, open("output.csv", "w") as out_file:
#     for line in in_file:
#         print(line.strip())   # Check if the line is not empty
#         out_file.write(line.strip()+"\n")  # Write the line to the output file
#

# Reading and printing specific column from CSV file
# import csv

# with open("content.csv", "r") as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print(row["age"])
        

with open("content.csv", "r") as file:
    lines = file.readlines()
    for line in lines[1:]:
        column=(line.strip().split(","))
        print(column[1])