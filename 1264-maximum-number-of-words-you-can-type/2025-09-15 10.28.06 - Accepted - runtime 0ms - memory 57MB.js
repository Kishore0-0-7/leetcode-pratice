/**
 * @param {string} text
 * @param {string} brokenLetters
 * @return {number}
 */
var canBeTypedWords = function(text, brokenLetters) {
    let words=text.split(" ");
    // let brokenSet=new Set(brokenLetters.split(""));
    let count=words.length;

    for (let word of words) {
        for (let ch of brokenLetters) {
            if (word.includes(ch)) {
                count--;
                break;
            }
        }
    }
    return count;
};