def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

n = int(input("Enter N: "))

if is_prime(n):
    print(n, "is prime")
else:
    print(n, "is not prime")

for num in range(2, n + 1):
    if is_prime(num):
        print(num, end=" ")
