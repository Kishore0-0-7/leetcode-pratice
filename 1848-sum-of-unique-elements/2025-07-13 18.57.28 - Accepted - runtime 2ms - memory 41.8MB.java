class Solution {
    public int sumOfUnique(int[] nums) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        
        int sum = 0;
        for (int key : freq.keySet()) {
            if (freq.get(key) == 1) {
                sum += key;
            }
        }
        
        return sum;
    }
}