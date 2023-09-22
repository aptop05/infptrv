def razb(n, s):
    if(n == 1):
        return s
    for i in range(2, n + 1):
        if(n % i == 0):
            return razb(n // i, s + " " + str(i))


print(razb(int(input()), ""))
