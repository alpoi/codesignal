/*
    Given a sequence of integers as an array, determine whether it is possible 
    to obtain a strictly increasing sequence by removing no more than one 
    element from the array.

    Note: sequence a0, a1, ..., an is considered to be a strictly increasing 
    if a0 < a1 < ... < an. Sequences containing only one element are also 
    considered to be strictly increasing.
*/

function solution(sequence) {
    let temp = [...sequence];
    let count = 0;
    
    for (let i = 0; i < sequence.length - 1 ; i++) {
        if (sequence[i] >= sequence[i + 1]) {
            if (count > 0) { 
                break;
            } else { 
                count += 1;
                sequence[i + 1] = sequence[i];
            }
        }
        if (i + 1 == sequence.length - 1) { return true; }
    }
    
    count = 0;
    sequence = [...temp];
    
    for (let i = 0; i < sequence.length - 1 ; i++) {
        if (sequence[i] >= sequence[i + 1]) {
            if (count > 0) { 
                return false; 
            } else { 
                count += 1; 
                sequence[i] = sequence[i - 1];
                i--;
            }
        }
        if (i + 1 == sequence.length - 1) { return true; } 
    }
    
}
