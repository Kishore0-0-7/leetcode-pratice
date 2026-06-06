class Solution {
    public int mostFrequentEven(int[] nums) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int item : nums) {
            if (item % 2 == 0) {
                seen.put(item, seen.getOrDefault(item, 0) + 1);
            }
        }
        
        int maxCount = 0;
        int output = -1;
        
        for (Map.Entry<Integer, Integer> entry : seen.entrySet()) {
            int num = entry.getKey();
            int count = entry.getValue();
            if (count > maxCount) {
                maxCount = count;
                output = num;
            } else if (count == maxCount) {
                output = Math.min(output, num);
            }
        }
        
        return output;
    }
}