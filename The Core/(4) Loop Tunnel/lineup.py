# To prepare his students for an upcoming game, the sports coach decides to try 
# some new training drills. To begin with, he lines them up and starts with the 
# following warm-up exercise: when the coach says 'L', he instructs the 
# students to turn to the left. Alternatively, when he says 'R', they should 
# turn to the right. Finally, when the coach says 'A', the students should turn 
# around.

# Unfortunately some students (not all of them, but at least one) can't tell 
# left from right, meaning they always turn right when they hear 'L' and left 
# when they hear 'R'. The coach wants to know how many times the students end 
# up facing the same direction.

# Given the list of commands the coach has given, count the number of such 
# commands after which the students will be facing the same direction.

def solution(commands):
    facing = 'same'
    count = 0
    for char in commands:
        if char == 'L' or char == 'R':
            if facing == 'same':
                facing = 'diff'
            elif facing == 'diff':
                facing = 'same'
                count += 1
        if char == 'A':
            if facing == 'same':
                count += 1
    return count

# passed all tests