# Given an array of integers, find the pair of adjacent elements that has the 
# largest product and return that product.

def solution(inputArray):
    products = []
    for i in range(len(inputArray) - 1):
        products.append(inputArray[i]*inputArray[i+1])
    return sorted(products)[-1]

# passed all tests