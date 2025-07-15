'''
#one file write file_handling:

file = open("notes.txt", "w")
file.write("Welcome to python\n")
file.write("This is new file\n")
file.close()

'''

'''

file=open("notes.txt","r")
content=file.read()
print("file content:", content)
file.close()    

'''

# Appending to the file
'''
file=open("notes.txt", "a")
file.write("Adding more content \n")
file.close()
'''

with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

        