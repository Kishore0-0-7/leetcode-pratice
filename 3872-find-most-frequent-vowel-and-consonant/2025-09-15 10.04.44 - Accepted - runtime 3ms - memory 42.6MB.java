class Solution {
    public int maxFreqSum(String s) {
        HashMap<Character,Integer> vo=new HashMap<>();
        HashMap<Character,Integer> co=new HashMap<>();
        int voc=0,coc=0;
        String vowles="aeiou";
        for(char c:s.toCharArray()){
            if(vowles.indexOf(c)!=-1) vo.put(c,vo.getOrDefault(c,0)+1);
            
            else co.put(c,co.getOrDefault(c,0)+1);
        }
        for(int i:vo.values())
        voc=Math.max(voc,i);
        
        for(int i:co.values())
        coc=Math.max(coc,i);

        return voc+coc;
    }
}