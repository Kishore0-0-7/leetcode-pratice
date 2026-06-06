class Solution {
public:
    int countGoodRectangles(vector<vector<int>>& rectangles) {
        int max = std::min(rectangles[0][0], rectangles[0][1]);
        int count = 0;
        for (int i = 0; i < rectangles.size(); i++) {
            int currentMin = std::min(rectangles[i][0], rectangles[i][1]);
            if (max < currentMin) {
                max = currentMin;
                count = 1;
            } else if (max == currentMin) {
                count++;
            }
        }
        return count; 
    }
};