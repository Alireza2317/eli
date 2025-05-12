#reads the radius of the base and the height of a cone and returns its volume
print("reads the radius of the base and the height of a cone and returns its volume") 
r = int(input("please, insert the radius of the base of the cone: ")) #radius of the base
h = int(input("please, insert the height of the cone: "))             #height of the cone
pi = 3.14159
v = (pi * h * r**2)/3
print("the volume of the cone is", v)
