/**
 * @param {string[]} patterns
 * @param {string} word
 * @return {number}
 */
var numOfStrings = function(patterns, word) {
  let cnt=0;
  for(let w of patterns) 
    if(word.includes(w)) cnt+=1;
    return cnt;
};