#String in python.


#String Formatting
name = "anil"
age = 18

# print(f"my name is {name} i am {age} year old.")
# print("my name is {} i am {} year old." .format(name, age))
# print("name: {0}, age: {1}" .format(name, age))
# print("My name is %s and I am %d years old." % (name, age))


#String Methods
rest = 'Hello, jet'
message = "time"

print(rest[0:5])
print(rest[2:])
print(rest[::-2])

print(len(rest)) # length
print(rest.upper()) # uppercase
print(rest.lower()) # lowercase
print(rest.strip()) # remove space
print(rest.replace("H", "i")) # replace
print(rest.split(',')) # split 
print(rest.find("o")) # find


#Strings are immutable—you can't change characters directly.
tank = "kumar"
tank = "12" + tank[1:]
print(tank)