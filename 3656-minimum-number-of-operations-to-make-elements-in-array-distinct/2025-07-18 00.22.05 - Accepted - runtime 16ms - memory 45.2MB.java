class Solution {
    public int minimumOperations(int[] nums) {
        int count = 0;
        while (nums.length > new HashSet<Integer>(Arrays.asList(Arrays.stream(nums).boxed().toArray(Integer[]::new))).size()) {
            if (nums.length <= 3) {
                nums = new int[0];
            } else {
                nums = Arrays.copyOfRange(nums, 3, nums.length);
            }
            count++;
        }
        return count;
    }
}