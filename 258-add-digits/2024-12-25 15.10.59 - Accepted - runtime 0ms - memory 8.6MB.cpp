class Solution {
public:
    int addDigits(int num) {
        int num1=0;
        while(num>9){
        while(num>0){
            num1+=num%10;
            num/=10;
        }
        num=num1;
        num1=0;
        }
        return num;
    }
};