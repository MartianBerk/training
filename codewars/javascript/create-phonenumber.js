/*
 * Solution to "Create Phone Number" problem on Codewars (Kata 6).
 * https://www.codewars.com/kata/525f50e3b73515a6db000b83
*/

function createPhoneNumber(numbers){
  const a = numbers.splice(0,3)
  const b = numbers.splice(0,3)
  const c = numbers.splice(0,4)
  return `(${a.join('')}) ${b.join('')}-${c.join('')}`;
}