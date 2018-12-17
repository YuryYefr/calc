def user_oper():
    user_operations = input("you choose what?:")
    while user_operations.isspace() or user_operations.isalpha():
        print("there is something wrong with your input, please try again")
        user_operations = input("you choose what?: ")
    return user_operations