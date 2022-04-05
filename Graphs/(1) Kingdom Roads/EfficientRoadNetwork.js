/*
    Once upon a time, in a kingdom far, far away, there lived a King Byteasar 
    III. As a smart and educated ruler, he did everything in his (unlimited) 
    power to make every single system within his kingdom efficient. The king 
    went down in history as a great road builder: during his reign a great 
    number of roads were built, and the road system he created was the most 
    efficient during those dark times.

    When you started learning about Byteasar's III deeds in your history 
    classes, a creeping doubt crawled into the back of your mind: what if the 
    famous king wasn't so great after all? According to the most recent studies, 
    there were n cities in Byteasar's kingdom, connected by two-way roads. You 
    managed to get information about these roads from the university library, 
    so now you can write a function that will determine whether the road system 
    in Byteasar's kingdom was efficient or not.

    A road system is considered efficient if it is possible to travel from any 
    city to any other city by traversing at most 2 roads.
*/

function solution(n, roads) {
    
    function getDirect(A) {
        return roads.filter( x => x.includes(A) )
                    .map( x => x.indexOf(A) ? x[0] : x[1] )
                    .concat([A]);
    }
    
    for ( let i = 0; i < n; i++ ) {
        for ( let j = i + 1; j < n; j++ ) {
            if ( getDirect(i).includes(j) ) { // saves time
                continue;
            } else if ( !getDirect(i).filter( x => getDirect(j).includes(x) ).length ) { 
                return false; 
            }
        }
    }
    
    return true;
}
