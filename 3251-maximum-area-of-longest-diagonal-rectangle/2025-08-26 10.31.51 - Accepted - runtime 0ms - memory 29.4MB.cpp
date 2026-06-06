class Solution {
public:
    int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
        double maxd=0;
        int maxa=0;
        for (auto &lst:dimensions) {
            double curd=sqrt(lst[0] * lst[0] + lst[1] * lst[1]);
            int cura=lst[0]*lst[1];
            if (curd>maxd||(curd==maxd && cura>maxa)) {
                maxd=curd;
                maxa=cura;
            }
        }
        return maxa;
    }
};