def fib(a, b, n):
    if(n <= 1):
        return b
    return fib(b, a + b, n  - 1)

print(fib(0, 1, int(input())))
