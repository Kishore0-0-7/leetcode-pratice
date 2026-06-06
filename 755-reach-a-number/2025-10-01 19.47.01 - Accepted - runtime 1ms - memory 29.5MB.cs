public class Solution {
    public int ReachNumber(int target) {
        target=Math.Abs(target);
        int steps=0,moves=0;
        while (steps<target || (steps-target)%2!=0) {
            moves++;
            steps+=moves;
        }
        return moves;
    }
}