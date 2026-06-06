/**
 * @param {string} sentence
 * @param {string} searchWord
 * @return {number}
 */
var isPrefixOfWord = function(sentence, searchWord) {
        st=sentence.split(" ");
        for (let i=0;i<st.length;i++){
            if (st[i].startsWith(searchWord))
                return i+1;
                }
        return -1;
};