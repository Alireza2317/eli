#reading from a file

name_of_file = input("what is the name of the file? ")

#opening file in read mode and refer to it as filereference
filereference = open(name_of_file, 'r') 

#read the file line by line
counter = 0
for readline in filereference:
    counter += 1
    print(f"line {counter} of file contains \"{readline[:-1]}\" ")

filereference.close()