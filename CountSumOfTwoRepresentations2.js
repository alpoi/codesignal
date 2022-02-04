/*
    Given integers n, l and r, find the number of ways to represent n as a sum 
    of two integers A and B such that l ≤ A ≤ B ≤ r.
*/

function solution(n, l, r) {

    if (n < 2*l) { return 0 };
    if (n > 2*r) { return 0 };
    
    let A = l;
    let B = r;
    
    if (A + B < n) {
        while (A + B != n) {
            A += 1;
        }
    } else if (A + B > n) {
        while (A + B != n) {
            B -= 1;
        }
    }
    
    let total = Math.ceil( Math.abs( (A - B) / 2 ) );
    
    if ( (n % 2) == 0 && (n / 2) >= l && (n / 2) <= r ) {
        total += 1;
    }
    
    return total;
    
}

