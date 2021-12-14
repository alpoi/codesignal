# Check if the given string is a correct time representation of the 24-hour 
# clock.

def solution(time):
    time = time.split(':')
    if len(time[0]) != 2 or len(time[1]) != 2: # leading zero required
        return False
    if not 0 <= int(time[0]) < 24:
        return False
    if not 0 <= int(time[1]) < 60:
        return False

    return True

# passed all tests