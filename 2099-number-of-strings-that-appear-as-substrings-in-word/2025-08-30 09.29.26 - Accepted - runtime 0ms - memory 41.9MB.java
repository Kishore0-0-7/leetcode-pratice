class Solution {
    public int numOfStrings(String[] patterns, String word) {
        int cnt=0;
        for(String w:patterns){
            if (word.contains(w)) cnt+=1;
        }
        return cnt;
    }
}