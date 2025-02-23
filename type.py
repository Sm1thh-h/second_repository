# student = {"rat", "bee"}

# print(type(student))

# age = 12

# print(type(age))

## this is the source code, we will be working to make the code better 
# try:
#     x = int(input("what is x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

##trying to make the code better 

# try:
#     x = int(input("what is x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

##this code is making sure the user give us a value 


def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("what is x? "))
            return x
        except ValueError:
            pass
    return x

main()

# this is  a better code because it is more dynamic and main is the one prompting
# what x should be.the caller is main and we are letting main handle what must be 
# asked 


def main():
    x = get_int("what's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass
    return x

main()
