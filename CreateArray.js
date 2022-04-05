/* 
    Given an integer size, return array of length size filled with 1s.
*/

function solution(size) {
    let array = new Array(size);
    for (let i = 0; i < array.length; i++) { array[i] = 1; }
    return array;
}
