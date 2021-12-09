# You have deposited a specific amount of money into your bank account. Each year your balance 
# increases at the same growth rate. With the assumption that you don't make any additional 
# deposits, find out how long it would take for your balance to pass a specific threshold.

def solution(deposit, rate, threshold):
    years = 0
    while deposit < threshold:
        deposit *= 1 + (rate/100)
        years += 1
    return years

# passed all tests