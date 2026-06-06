class Solution {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Integer> numToIndexMap = new HashMap<>();
        int sizeOfArray = numbers.length;
        for(int i = 0; i < sizeOfArray; i++) {
            int diff = target - numbers[i];
            if(numToIndexMap.containsKey(diff)) {
                return new int[]{numToIndexMap.get(diff)+1,i+1};
            }
            numToIndexMap.put(numbers[i], i);
        }
        return null;
    }
}