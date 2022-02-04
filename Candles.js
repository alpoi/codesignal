/*
    When a candle finishes burning it leaves a leftover. makeNew leftovers can 
    be combined to make a new candle, which, when burning down, will in turn 
    leave another leftover.

    You have candlesNumber candles in your possession. What's the total number 
    of candles you can burn, assuming that you create a new candle as soon as 
    you have enough leftovers?
*/

function solution(candlesNumber, makeNew) {

    let candles = candlesNumber;
    let leftovers = 0;
    let total = 0;
    
    function burnCandle() {
        candles -= 1;
        leftovers += 1;
        total += 1;
    }
    
    function makeCandle() {
        candles += 1;
        leftovers -= makeNew;
    }
    
    while (candles > 0 || leftovers >= makeNew) {
        if (candles > 0) { burnCandle(); }
        if (leftovers >= makeNew) { makeCandle(); }
    }
    
    return total;
    
}
