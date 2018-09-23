def factorial(n):
    i = 0
    total = 1
    while i != n:
        i += 1
        total = total * i
    return total


print factorial(4)

