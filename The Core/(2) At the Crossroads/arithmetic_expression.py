# Consider an arithmetic expression of the form a#b=c. Check whether it is 
# possible to replace # with one of the four signs: +, -, * or / to obtain a 
# correct expression.

def solution(a, b, c):
    return (a + b == c) or (a - b == c) \
                        or (a * b == c) \
                        or (a / b == c if b != 0 else False)

# passed all tests
