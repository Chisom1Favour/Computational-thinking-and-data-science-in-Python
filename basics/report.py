def IsIn(str1, str2):
    if str1 in str2 or str2 in str1:
        print('String found')
        return True
    else:
        print('String not found')
        return False

def main():
    string1 = "This is gold"
    string2 = "If This is true"
    IsIn(string1, string2)

if __name__ == "__main__":
    main()
