class Solution {
    public int countTestedDevices(int[] batteryPercentages) {
     int tested=0;
        for (int percentage:batteryPercentages) {
            if (percentage-tested>0) {
                tested++;
            }
        }
        return tested;   
    }
}