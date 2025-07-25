/*
 * Solution to "Is My Friend Cheating" problem on Codewars (Kata 5).
 * https://www.codewars.com/kata/5547cc7dcad755e480000004/
 * 
 * The maths eluded me on this a bit, was only able to solve by brute force.
 * i.e. Looping through all pairs of numbers from 1 to n == O(n^2).
 * Copilot was used to find the optimal mathematical formula of b = (total - a) / (a + 1).
 * The result of b is then checked for greater than 0, less than or equal to n, and an integer.
 * This is == O(n).
 * 
 * The trick to find the improved algorithm was to rearrange the equation (where S == sum1ToN(n)):
 * - a * b = S - a - b
 * - a * b + b = S - a
 * - b * (a + 1) = S - a
 * For each of these we need to know a & b, so the brute force loop is required.
 * - b = (S - a) / (a + 1)
 * But here we calculate b based on a, so we only need to loop through a.
*/

function sum1ToN(n) {
    return n * (n + 1) / 2;
}

function removeNb(n) {
    const total = sum1ToN(n);
    const results = [];

    for (let a = 1; a <= n; a++) {
        const b = (total - a) / (a + 1);
        if (b > 0 && b <= n && Number.isInteger(b)) {
            results.push([a, b]);
        }
    }

    return results;
}


console.log(removeNb(26));
console.log(removeNb(100));
console.log(removeNb(1000003));