# Ratiorg got statues of different sizes as a present from CodeMaster for his 
# birthday, each statue having an non-negative integer size. Since he likes to 
# make things perfect, he wants to arrange them from smallest to largest so 
# that each statue will be bigger than the previous one exactly by 1. He may 
# need some additional statues to be able to accomplish that. Help him figure 
# out the minimum number of additional statues needed.

def solution(statues):
    stat = statues
    count = 0
    for num in stat:
        if num < max(stat) and (num + 1) not in stat:
            stat.append(num + 1)
            count += 1
    return count
        
# passed all tests