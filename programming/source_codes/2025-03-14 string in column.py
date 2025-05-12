#using loop: reads a string and print it a char per line
s = input("please insert s sting: ")
print("your string character by character is:")
index = 0
while index < len(s):
    print(s[index])
    index += 1
print("that is all")
