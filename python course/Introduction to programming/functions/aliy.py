def add (x,y):
    return x+y

def subtract (x,y):
    return x-y

def multiply (x,y):
    return x*y

def divide (x,y):
    return x/y

num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))

print("try operations")
print("sum:", add(num1, num2))
print("Difference:", subtract(num1,num2))
print("product:", multiply(num1,num2))
print("Quotent:", divide(num1,num2))