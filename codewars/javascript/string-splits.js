/*
 * Solution to "String Splits" problem on Codewars (Kata 6).
 * https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
*/

function solution(str){
    if (str.length === 0) {
        return [];
    }

    let pairs = [];
  
    let pair = str[0]; 
    for (var i = 1; i < str.length; i++) {
        pair = pair + str[i];
        if (i % 2 !== 0) {
            pairs.push(pair);
            pair = "";
        }
    }

    if (pair.length > 0) {
        pairs.push(pair + "_");
    }

    return pairs;
}