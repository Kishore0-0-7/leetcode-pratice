class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        vector<int> lst;
        for(int i=0;i<matrix.size();i++){
            for(int j=0;j<matrix[i].size();j++){
                lst.push_back(matrix[i][j]);
            }
        }
        sort(lst.begin(),lst.end());
        return (lst[k-1]);
    }
};