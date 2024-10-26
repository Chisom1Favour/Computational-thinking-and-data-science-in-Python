def find_root_and_power(n): 
    for pwr in range(1, 6):
        root = int(n ** (1 / pwr))
        if root ** pwr == n:
            return root, pwr
        if (root + 1) ** pwr == n:
            return root + 1, pwr
    return None

def main():
    try:
        n = int(input("Enter an integer"))
        result = find_root_and_power(n)

        if result:
            root, pwr = result
            print(f"root = {root}, pwr = {pwr}")
        else:
            print("No such pair of integers (root, pwr) exists.")
    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    main()
