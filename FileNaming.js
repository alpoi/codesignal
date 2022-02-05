/*
    You are given an array of desired filenames in the order of their creation. 
    Since two files cannot have equal names, the one which comes later will 
    have an addition to its name in a form of (k), where k is the smallest 
    positive integer such that the obtained name is not used yet.

    Return an array of names that will be given to the files.
*/

function solution(names) {
    let newNames = [];
    
    for (let name of names) {
        if (checkExistence(name)) {
            let newName = name + '(' + findLargestIndex(name) + ')';
            newNames.push(newName);
        } else {
            newNames.push(name);
        }
    }
    
    function checkExistence(name) {
        if (newNames.includes(name)) { 
            return true; 
        } else { 
            return false; 
        }
    }
    
    function findLargestIndex(name) {
        let newName = name + '(1)';
        let i = 2;
        while (checkExistence(newName)) {
            newName = name + '(' + i++ + ')';
        }
        return i - 1;
    }
    
    return newNames;
}