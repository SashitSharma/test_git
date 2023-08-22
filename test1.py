def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero is not allowed")

# Example usage
num1 = 10
num2 = 5

print("Addition:", addition(num1, num2))
print("Subtraction:", subtraction(num1, num2))
print("Multiplication:", multiplication(num1, num2))
print("Division:", division(num1, num2))
