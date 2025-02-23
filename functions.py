# def add_num(num1, num2, num3):
#     final_num = num1 + num2 + num3
#     return final_num

# print(add_num(1, 2, 3))

# when expecting lots of argument you use *

def add_num(*nums):
    final_num = 0
    print(f"num is type: {type(str(nums))}")

    for num in nums:
        final_num += num
    return final_num

print(add_num(1, 2, 5))
    