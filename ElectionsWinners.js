/*
    Given an array of the numbers of votes given to each of the candidates so 
    far, and an integer k equal to the number of voters who haven't cast their 
    vote yet, find the number of candidates who still have a chance to win the 
    election.

    The winner of the election must secure strictly more votes than any other 
    candidate. If two or more candidates receive the same (maximum) number of 
    votes, assume there is no winner at all.
*/

function solution(votes, k) {
    let threshold = Math.max(...votes);
    let count = 0;
    
    if (k == 0) {
        switch ( votes.filter( x => x == threshold ).length ) {
            case 1:
                return 1;
            default:
                return 0;
        }
    }
    
    for (let candidate of votes) {
        if (candidate + k > threshold) { count++; }
    }
    
    return count;
}
