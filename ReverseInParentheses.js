/*
    Write a function that reverses characters in (possibly nested) 
    parentheses in the input string.

    Input strings will always be well-formed with matching ()s.
*/

function solution(inputString) {
    let openIndexes = [];
    
    for (let i = 0; i < inputString.length; i++) {
        if (inputString[i] == '(') {
            
            openIndexes.push(i);
            
        } else if (inputString[i] == ')') {
            
            let innerStart = openIndexes.pop()
            let tempString = inputString.slice(innerStart, i + 1)
                                        .replace('(',' ')
                                        .replace(')',' ')
                                        .split('')
                                        .reverse()
                                        .join('');
                                        
            inputString = inputString.slice(0, innerStart) + tempString 
                        + inputString.slice(i + 1);
        }
        
    }
    
    inputString = inputString.replace(/\s+/g, '');
    return inputString;

}
