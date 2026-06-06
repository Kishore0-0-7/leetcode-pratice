class Solution {
public:
    int countPrimes(int n) {
        int cnt = 0,sum=0;
        vector<bool> prime(n + 1, true);
        prime[0]=prime[1]=false;
        for (int i=2;i<n/2+1;i++) {
            if (prime[i]) {
                cnt++;
                for (int j=i*i;j<n;j=j+i) {
                    prime[j] = 0;
                }
            }
        }
        for(int i=2;i<n;i++)
        if(prime[i]) sum+=1;

        return sum;
    }   
};