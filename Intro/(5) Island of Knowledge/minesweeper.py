# In the popular Minesweeper game xou have a board with some mines 
# and those cells that don't contain a mine have a number in it that 
# indicates the total number of mines in the neighboring cells. 
# Starting off with some arrangement of mines we want to create a 
# Minesweeper game setup.

def solution(m):
    
    # bool is a subclass of int so we can do arithmetic with True, False
    # use what we learned in add_border to pad with zeroes
    
    for row in m:
        row.insert(0, 0)
        row.append(0)
    m.insert(0, [0 for i in range(len(m[0]))])
    m.append([0 for i in range(len(m[0]))])
    
    # then use what we learned in box_blur, ommitting m[x][y] (mines do not count themselves)

    return[[m[x - 1][y - 1] + m[x][y - 1] + m[x + 1][y - 1] + \
            m[x - 1][y]     + m[x + 1][y] + \
            m[x - 1][y + 1] + m[x][y + 1] + m[x + 1][y + 1]
            for y in range(1, len(m[0]) - 1)] 
            for x in range(1, len(m) - 1)   ]

# passed all tests