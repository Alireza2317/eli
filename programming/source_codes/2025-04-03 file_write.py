#writing into a file

name_of_file = input("what is the name of the file to write? ")

#opening file in write mode and refer to it as filereference
filereference = open(name_of_file, 'w') 

#write someting into the File
for i in range(1,101):
    filereference.write(f"this is line {i} of file {name_of_file} after modification\n")

filereference.close()