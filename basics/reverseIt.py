def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ' ,' + firstName)
    else:
        print(firstName, lastName)

def main():
    printName('Olga', 'Nwanne', False)
    printName('Olga', 'Nwanne', reverse = False)
    printName('Olga', lastName='Nwanne', reverse=False)
    printName(lastName='Nwanne', firstName='Oluchi', reverse=True)

if __name__ == "__main__":
    main()
