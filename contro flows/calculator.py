def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y

def divide(x, y):
    if y !=0:
        return x / y
    else:
        return "cannot divide zero"
    
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /):")
num2 = float(input("Enter the second number:"))
    
    # performs calculation based on user input
    
if operator == "+":
        result = add(num1, num2)
elif operator =="-":
        results = subtract(num1, num2)
elif operator == "*":
        results = multiply(num1, num2)
elif operator == "/":
        results = divide(num1, num2)
else:
        results = "Invalid operator"
        
        print(f"Results:{results}")
