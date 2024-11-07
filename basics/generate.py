# Generate all combinations of N items
def powerSet(items):
    """
    Generates all combinations of N items into 2 bags, whereby each
    item is in one or more bags

    Yields a tuple, (bag1, bag2), where each bag is represented as a list
    of which item(s) are in each bag
    """
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            state = (i // (3**j)) % 3
            if state == 1:
                bag1.append(items[j])
            elif state == 2:
                bag2.append(items[j])
        yield(bag1, bag2)


