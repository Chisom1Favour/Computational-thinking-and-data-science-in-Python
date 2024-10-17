
x = 0

for i in range(10):
    y = int(input("Enter an integer"))
    if (y % 2 != 0):
        if (x < y):
            x = y
            print("X is greater than y", x);
        else:
            print("X is less than y")
    else:
        print("y is not divisible by 2")
        
            
