# a = 4
# print(a)

names = ["JameS", "heNrY", "JOSEph", "TolanI"]
unique = set()
for name in names:
    if name.isupper():
        unique.add(name)
        continue
    unique.add(name.upper())
print(unique)

if 2 > 3:
    print("pass")
else:
    print("dont pass")

num = input("Enter number: ")
number = int(num)
condition = 0
count = 2
iteration = 0

while iteration <= number/2:
    if number % count == 0:
        print(f"condition met at iteration = {iteration}")
        condition = 1
        break
    iteration += 1
if condition == 0:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


num = input("enter number: ")
number = int(num)
condition = 0
count = 2

while count <= number/2:
    if number % count == 0:
        print(f"number is divisible by {count}")
        condition = 1
        break
    count += 1

if condition == 0:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


a = ["tIMMy", "YakUB"]
unique = set()
for item in a:
    if item.islower():
        unique.add(item)
        continue
    unique.add(item.lower())
print(unique)

new_set = set()
test_integer = [2, 3, 4, 5, 6, 7]
for item in test_integer:
    print(item ** 2)
        


number = input(f"enter the number: ")
number_int = int(number)
condition = 0
count = 2 

while count <= number_int/2:
    if number_int % 2 == 0:
        print(f"this number is divisible by: {count}")
        condition = 1
        break
    count += 1

if condition == 0:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

fruits = ["apple", "banana", "cherry"]
new_fruit = {x for x in fruits}
print(new_fruit)

b = "banana"
for x in b:
    print(b)


fruits = ["banana", "guava", "orange", "apple"]
for x in fruits:
    if x == "orange":
        break 
    print(x)

fruits = ["banana", "guava", "orange", "apple"]
new_fruits = []
for x in fruits:
    if x == "orange":
        break
    new_fruits.append(x)
print(new_fruits)
    

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(1, 10):
    if x == 3:
        continue
    print(x)
else:
    print("finished")

def myfunction():
    print("Hello from my function")
myfunction()


def my_new_function():
    fruits = ["banana", "guava", "orange", "apple"]
    new_fruits = []
    for x in fruits:
        if x == "orange":
            break
        new_fruits.append(x)
    print(new_fruits)
my_new_function()

def my_func(fname):
    print(fname + " & Tolu")
my_func("Timi")
my_func("Lanre")
my_func("Ebun")

def my_func(fname, lname ):
    print(fname + " " + lname)
my_func("Tolu", "Layi")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(food):
    for x in fruits:
        print(x)
fruits = [2, 3, 5, 7, 8, 10]

my_function(fruits)

def sample_funtion(y):
    return 5 * y
print(sample_funtion(10))

def my_function(x):
  print(x)

my_function(3)

def my_function(x):
  print(x)

my_function(x = 3)

a = ["toLu", "TIMMy", "Lanre"]
new_a = []
for name in a:
    new_a.append(name.lower())
print(new_a)

def my_function(x):
  return 5 * x

print(my_function(3))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)


class dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def __str__(self):
        return f"{self.name} barks like a goat even though she is an {self.breed}"

my_dog = dog("Chloe", "Alstatian")

print(my_dog)

class dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def sound(self):
        print(f"{self.name} barks like a goat even though she is an {self.breed}")

my_dog = dog("Chloe", "Alstatian")

my_dog.sound()


name = input("Enter your name: ")
print(f"Hello, {name}")

print("my name is",name, sep="")

name = input("Enter your name: ")

name = name.strip()

name = name.capitalize()

print(f"Hello, {name}")

x = float(input("what's x? "))
y = float(input("what's y? "))

round(2.66)


print(f"addition of {x} and {y} is {x + y:,}")

x = float(input("what's x? "))
y = float(input("what's y? "))


print(f"addition of {x} and {y} is {x + y:.2f}")

def hello(to = "world"):
    print("hello," , to)
hello()
name = input("what's your name? ")
hello(name)

def main():
    name =input("what's your name: ")
    hello(name)

def hello(to = "world"):
    print("hello,", to)

main()

