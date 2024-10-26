def convert(s):
    numbers = map(float, s.split(','))
    total = sum(numbers)
    return total

def main():
    str1 = '1.23,2.4,3.123,5.12,3.456,9.023'
    result = convert(str1)

if __name__ == "__main__":
    main()
