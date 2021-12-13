# Some people are standing in a row in a park. There are trees between them 
# which cannot be moved. Your task is to rearrange the people by their heights 
# in a non-descending order without moving the trees. People can be very tall!

def solution(a):
    
    heights = sorted([num for num in a if num != -1])
    trees = [False if x == -1 else True for x in a]

    for i in range(len(trees)):
        if trees[i]:
            trees[i] = heights[0]
            del heights[0]
        else:
            trees[i] = -1
        
    return trees
    

# passed all tests