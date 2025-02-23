def main():
    x = int(input("what is x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()

a = int(input("what is a? "))
b = int(input("what is b? "))

if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater tha {a}")
else:
    print(f"{b} is equal to {a}")


a = int(input("what is a? "))
b = int(input("what is b? "))

if a > b or b > a:
    print(f"{a} is not equal to {b}")
else:
    print(f"{b} is equal to {a}")

a = int(input("what is a? "))
b = int(input("what is b? "))

if a != b:
    print(f"{a} is not equal to {b}")
else:
    print(f"{a} is equal to {b}")


score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

name = input("what's your name: ")

match name:
    case "Harry" | "Timmy" | "Tolu":
        print("Naija")
    case "Olanrewaju" | "Pheezo" | "Ebun":
        print("Ijebu")
    case _:
        print("who?")

i = 0

while i < 3:
    print("meow")
    i += 1

for _ in range(5):
    print("meow")

while True:
    n = int(input("what's n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")

def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")

main()



def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("what is n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()