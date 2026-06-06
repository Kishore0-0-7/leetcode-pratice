class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        unordered_map<int,int> mp;
        int count=0;
        for (auto& d:dominoes) {
            int a=d[0],b=d[1];
            int k=min(a,b)*10+max(a,b);
            count+=mp[k];
            mp[k]++;
        }
        return count;
    }
};