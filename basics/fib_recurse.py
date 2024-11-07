def fib(n):
    """Assumes n int >= 0
        Returns fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('fib of', i, '= ', fib(i))

def main():
    num = 10
    testFib(num)

if __name__ == "__main__":
    main()
