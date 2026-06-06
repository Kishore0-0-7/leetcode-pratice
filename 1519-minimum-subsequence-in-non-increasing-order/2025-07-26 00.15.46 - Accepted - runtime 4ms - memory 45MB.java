class Solution {
    public List<Integer> minSubsequence(int[] nums) {
        Arrays.sort(nums);
        // Reverse sort manually
        int n = nums.length;
        for (int i = 0; i < n / 2; i++) {
            int tmp = nums[i];
            nums[i] = nums[n - 1 - i];
            nums[n - 1 - i] = tmp;
        }

        int total = 0;
        for (int num : nums) total += num;

        int rSum = 0;
        List<Integer> res = new ArrayList<>();

        for (int num : nums) {
            rSum += num;
            res.add(num);
            if (rSum > total - rSum) break;
        }

        return res;
    }
}