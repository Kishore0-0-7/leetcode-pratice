class Solution {
    public int findDuplicate(int[] nums) {
        HashMap<Integer, Integer> d = new HashMap<>();
        for (int i : nums) {
            if (d.containsKey(i)) {
                return i;
            } else {
                d.put(i, 1);
            }
        }
        return -1;
    }
}