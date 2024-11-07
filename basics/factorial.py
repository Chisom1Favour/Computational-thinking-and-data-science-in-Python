def fact1(n):
    """Assumes n an int > 0
        Returns n!"""
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

def main():
    num = 5
    res = fact1(num)
    print(res)


if __name__ == "__main__":
    main()
