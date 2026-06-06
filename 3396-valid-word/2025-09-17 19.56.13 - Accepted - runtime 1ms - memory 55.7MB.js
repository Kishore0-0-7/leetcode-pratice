/**
 * @param {string} word
 * @return {boolean}
 */
var isValid = function(word) {
    let n=word.length;
        if (n<3) {
            return false;
        }
        let vowels=0;
        let consonants=0;

        for (let c of word) {
            if (/[a-zA-Z]/.test(c)) {
                if ("aeiouAEIOU".includes(c)) {
                    vowels++;
                } else {
                    consonants++;
                }
            } else if (!/[0-9]/.test(c)) {
                return false;
            }
        }
        return vowels>=1 && consonants>=1;
};