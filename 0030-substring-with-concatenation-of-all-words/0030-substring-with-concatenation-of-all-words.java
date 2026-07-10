class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> ans=new ArrayList<Integer>();
        if(s==null||s.length()==0||words.length==0) return ans;
        int wordLen=words[0].length();
        int wordCount=words.length;
        int totalLen=wordLen*wordCount;
        Map<String,Integer> need=new HashMap<>();
        for(String sb:words){
            need.put(sb,need.getOrDefault(sb,0)+1);
        }
        for (int offset=0;offset<wordLen;offset++){
            int left=offset;
            int count=0;
            HashMap <String,Integer> map=new HashMap<>();
            for(int right=offset;right+wordLen<=s.length();right+=wordLen){
                String t=s.substring(right,right+wordLen);
                if(!need.containsKey(t)){
                    map.clear();
                    count=0;
                    left=right+wordLen;
                    continue;
                }
                map.put(t,map.getOrDefault(t,0)+1);
                count++;
                while(map.get(t)>need.get(t)){
                    String leftWord=s.substring(left,left+wordLen);
                    map.put(leftWord,map.get(leftWord)-1);
                    if(map.get(leftWord)==0) map.remove(leftWord);
                    left+=wordLen;
                    count--;
                }
                if(count==wordCount){
                    ans.add(left);
                    String leftWord=s.substring(left,left+wordLen);
                    map.put(leftWord,map.get(leftWord)-1);
                    if(map.get(leftWord)==0) map.remove(leftWord);
                    left+=wordLen;
                    count--;
                }
            }
        }
        return ans;
    }
}