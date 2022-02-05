/*
    Given array of integers, find the maximal possible sum of some of its k 
    consecutive elements.
*/

function solution(inputArray, k) {
    let sums        = [];
    let initialSum  = getInitialSum(inputArray, k);
    sums.push( initialSum );
    let nextSum     = initialSum;
        
    for (let i = k; i < inputArray.length; i++) {
        nextSum = nextSum + inputArray[i] - inputArray[i - k];
        sums.push( nextSum );
    }
    
    return Math.max(...sums);
}

function getInitialSum(inputArray, k) {
    let initialSum = 0;
    for (let i = 0; i < k; i++) {
        initialSum += inputArray[i];
    }
    return initialSum;
}