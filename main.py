# Lucas Brinks
# 1/14/25
# Returning Multiple Values from a Python Function
from random import randint as r
# def math(num1,num2):
#     prod = num1 * num2
#     sum = num1 + num2
#     return prod, sum

# maths = math(2,4)
# prod, sum = maths

# print(f'The product = {prod}')
# print(f'The sum = {sum}')

def ball(num1,num2):
    big = max(num1,num2)
    
    small = min(num1,num2)
    return big,small

big,small = ball(num1= r(1,100), num2= r(1,100))


print(f'The larger number is {big} and the smaller number is {small}')