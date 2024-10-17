x = 12
y = 7
z = 10

largest_odd = None

for num in (x, y, z):
    if num % 2 != 0:
        if largest_odd is None or num > largest_odd:
            largest_odd = num

if largest_odd is not None:
    print("The largest odd number is:", largest_odd)
else:
    print("There are no odd numbers among x, y, and z")
