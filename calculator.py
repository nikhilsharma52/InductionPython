def calculator(operation, *args):
    if operation == "+":
        result = args[0]
        for num in args[1:]:
            result += num

    elif operation == "-":
        result = args[0]
        for num in args[1:]:
            result -= num

    elif operation == "*":
        result = args[0]
        for num in args[1:]:
            result *= num

    elif operation == "/":
        result = args[0]
        for num in args[1:]:
            result /= num

    return result


print(calculator("+", 10, 20, 30))
print(calculator("-", 50, 10, 5))
print(calculator("*", 2, 3, 4))
print(calculator("/", 100, 5, 2))
