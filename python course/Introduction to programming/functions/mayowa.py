def fact(num):
    if num == 1:
        return 1
    else:
        result = num
        while num > 1:
            num = num-1
            result = result*num
        return result
number = int(input("Enter a number:"))
print("The factorial of", number, "is", fact(number))
         