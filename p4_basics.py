# Declaring Variables
name = "Kaushik"
age = 38
year = int("2020") # Convert string to integer

#Printing Variables
print(name)
print(age)
print(year)
print(type(name)) # <class 'str'>
print(type(age))
print(type(year))
print(type(name) == str) # type() is a function that returns the type of the variable
print(type(age) == int)
print(type(year) == int)
print(isinstance(name, str)) # isinstance() is a function that returns True or False
print(isinstance(age, int))
print (name + " is " + str(age) + " years old in " + str(year)) # Convert integer to string

print ("ud" in name) # True