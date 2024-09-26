# Question 1: OSKI STOLE YOUR POWER
x = 2
y = 2
def power(x, y):
    # Start with a base result of 1
    result = 1
    
    # Multiply `x` by itself `y` times
    for _ in range(abs(y)):
        result *= x

    # If `y` is negative, return the reciprocal of the result
    if y < 0:
        return 1 / result

    return result