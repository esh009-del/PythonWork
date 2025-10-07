#name is a variable
name ="jill"
age=30
profession="musician"
print("Hello"+ name )
#typical string concatenation
# print(name + "is" + age + "years old and is a " + profession  + "by profession")

#we can simplify using format function 
# print(" {} is {} years old and is a {}  by profession".format(name,age,profession))

#we can further simplify further using formatted string or for shorter fstring
print(f" {name} is {age} years old and is a {profession}  by profession")