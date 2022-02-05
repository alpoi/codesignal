/*
    Construct a square matrix with a size N × N containing integers from 1 to 
    N * N in a spiral order, starting from top-left and in clockwise direction.

    3x3: 3, 2, 2, 1, 1
    4x4: 4, 3, 3, 2, 2, 1, 1
    5x5: 5, 4, 4, 3, 3, 2, 2, 1, 1
    ...
*/

function solution(n) {
    
    let matrix = [];
    
    for (let k = 0; k < n; k++) {
        matrix[k] = new Array(n);
    }
    
    let total = 0;

    let i = 0,
        j = -1;

    function fillRight(steps) {
        for (let k = 1; k < steps + 1; k++) {
            matrix[i][++j] = ++total;
        }
    }
    
    function fillDown(steps) {
        for (let k = 1; k < steps + 1; k++) {
            matrix[++i][j] = ++total;
        }
    }
    
    function fillLeft(steps) {
        for (let k = 1; k < steps + 1; k++) {
            matrix[i][--j] = ++total;
        }
    }
    
    function fillUp(steps) {
        for (let k = 1; k < steps + 1; k++) {
            matrix[--i][j] = ++total;
        }
    }
    
    fillRight(n);
    while (n > 1) {
        fillDown(--n);
        fillLeft(n);
        fillUp(--n);
        fillRight(n);
    }
    
    return matrix;
}
