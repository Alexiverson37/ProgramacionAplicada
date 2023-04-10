def factorial(num):
    print("valor inicial ->",num)
    if num > 1:
        num =num * factorial(num-1)
    print("valor final->",num)
    return num 
print(factorial(5))