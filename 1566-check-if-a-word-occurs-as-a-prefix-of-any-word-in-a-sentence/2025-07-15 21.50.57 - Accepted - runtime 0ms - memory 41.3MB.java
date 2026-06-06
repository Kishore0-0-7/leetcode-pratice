class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        String []st=sentence.split(" ");
        for (int i=0;i<st.length;i++){
            if (st[i].startsWith(searchWord))
                return i+1;
                }
        return -1;
    }
}