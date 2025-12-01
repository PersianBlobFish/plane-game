
def is_even(n):
    try:
        value = int(n)
    except (TypeError, ValueError):
        raise TypeError("is_even() argument must be an integer or convertible to int")
    return value % 2 == 0

def main():
    number = (input("Enter a number: "))
    if is_even(number):
        print("Even")
    else:
        print("Odd")
main()
