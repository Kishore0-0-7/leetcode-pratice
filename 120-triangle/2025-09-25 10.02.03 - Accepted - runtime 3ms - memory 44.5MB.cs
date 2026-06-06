public class Solution {
    public int MinimumTotal(IList<IList<int>> triangle) {
        for (int i=triangle.Count - 2; i>=0; i--) {
            for (int j=0; j < triangle[i].Count; j++) {
                int down =triangle[i+ 1][j];
                int diag =triangle[i+ 1][j + 1];
                triangle[i][j] =triangle[i][j] + Math.Min(down, diag);
            }
        }
        return triangle[0][0];
    }
}