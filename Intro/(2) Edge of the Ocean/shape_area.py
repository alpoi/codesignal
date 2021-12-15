# Below we will define an n-interesting polygon. Your task is to find the area 
# of a polygon for a given n.
#
# A 1-interesting polygon is just a square with a side of length 1. An 
# n-interesting polygon is obtained by taking the n - 1-interesting polygon 
# and appending 1-interesting polygons to its rim, side by side. You can see 
# the 1-, 2-, 3- and 4-interesting polygons in the picture below.
#
# https://codesignal.s3.amazonaws.com/tasks/shapeArea/img/area.png?_tm=1624642306583

def solution(n):
    area = 1
    for i in range(2,n+1):
        area += 2*i + 2*(i-2)
    return area

# passed all tests