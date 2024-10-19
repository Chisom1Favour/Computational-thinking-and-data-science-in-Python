def greedy(items, maxCost, keyFunction):
    """Assumes items a lis, maxCost >= 0,
        keyFunction maps element of items to numbers"""
    itemsCopy = sorted(items, key = keyFunctio, reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)
