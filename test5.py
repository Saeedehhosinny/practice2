a = int(input("Enter a:"))
b = int(input("Enter b:"))
op = input("Enter op(+, -, /, *)")
if op == "+":
    r = a + b
if op == "-":
    r = a - b
if op == "*":
    r = a * b
if op == "/":
    if b == 0:
        r ="Run again"
else:
    r = a / b 
print(r)