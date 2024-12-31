# Factorial(n) = n * Factorial(n - 1)
# Factorial(n - 1) = (n - 1) * Factorial(n - 2)
# ....
# Factorial(1) = 1
def factorial(n):
    if n == 1 :
        return 1
    return n * factorial(n - 1)


print(factorial(5))