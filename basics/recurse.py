def factR(n):
    """Assumes n an int > 0
        Returns n!"""
    if n == 1:
        return n
    else:
        return n * factR(n-1)

