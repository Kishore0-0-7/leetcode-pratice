class Solution {
    public int minimumOperations(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        if (set.contains(0)) {
            return set.size() - 1;
        }
        return set.size();
    }
}