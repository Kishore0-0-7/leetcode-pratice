 class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
    StringBuilder t=new StringBuilder();
        for(String word:words){
            int result=0;
            for(char c:word.toCharArray()){
                result+=weights[c-'a'];
            }
            int mod=result%26;
            char map=(char)('z'-mod);
            t.append(map);
            }
                return t.toString();
            
        }
    }
