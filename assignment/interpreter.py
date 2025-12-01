expression = input("Expression: ")
x, y, z = expression.split(" ")
print(x, y, z)
match y:
    case "+":
        print(float(x) + float(z))
    case "-":
        print(float(x) - float(z))
    case "*":
        print(float(x) * float(z))
    case "/":
        print(float(x) / float(z))
    case _:
        print("Unknown operator")
