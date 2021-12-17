# A little child is studying arithmetic. They have just learned how to add two 
# integers, written one below another, column by column. But the child always 
# forgets about the important part - carrying.

# Given two integers, your task is to find the result that the child will get.

def solution(param1, param2):

    if param2 > param1:
        param1, param2 = str(param2), str(param1)
    else:
        param1, param2 = str(param1), str(param2)

    while len(param1) > len(param2):
        param2 = '0' + param2

    return int(''.join([str( (int(param1[i]) + int(param2[i])) % 10) for i in range(len(param1))]))
    
# passed all tests