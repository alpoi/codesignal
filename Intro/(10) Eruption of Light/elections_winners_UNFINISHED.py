# Elections are in progress!
#
# Given an array of the numbers of votes given to each of the candidates so 
# far, and an integer k equal to the number of voters who haven't cast their 
# vote yet, find the number of candidates who still have a chance to win the 
# election.
#
# The winner of the election must secure strictly more votes than any other 
# candidate. If two or more candidates receive the same (maximum) number of 
# votes, assume there is no winner at all.

def solution(votes, k):
    if k == 0 and votes.count(max(votes)) == 1:
        # handles corner case where there are no votes remaining
        # and there is a single winner already
        return 1
    return len([el for el in votes if el + k > max(votes)])

# passed 11/12 tests
# exceeded 4 second execution time limit for final test