camelCase = input("Enter a camelCase string: ")
def camel_to_snake(camel_str):
    snake_str = ""
    for char in camel_str:
        if char.isupper():
            snake_str += "_" + char.lower()
        else:
            snake_str += char
    return snake_str.lstrip("_")

snake_case = camel_to_snake(camelCase)
print("Snake_case string:", snake_case)