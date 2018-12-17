def user_numbers():
    a = input("Number?: ")
    while a.isspace() or a.isalpha() or a == "":
        print("there is something wrong with your input, please try again")
        a = input("Number?: ")
    b = input("What is second number?: ")
    while b.isspace() or b.isalpha() or b == "":
        print("there is something wrong with your input, please try again")
        b = input("What is second number?: ")
    user_number = float(a), float(b)
    return user_number