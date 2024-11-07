def fib(limit):
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b

x = fib(200)

for i in x:
    print(i)
