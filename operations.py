def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You cannot divide on zero")


def multiply(a, b):
    return a * b