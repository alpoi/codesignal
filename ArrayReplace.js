/*
    Given an array of integers, replace all the occurrences of elemToReplace 
    with substitutionElem.
*/

function solution(inputArray, elemToReplace, substitutionElem) {
    return inputArray.map( x => x == elemToReplace ? substitutionElem : x );
}
