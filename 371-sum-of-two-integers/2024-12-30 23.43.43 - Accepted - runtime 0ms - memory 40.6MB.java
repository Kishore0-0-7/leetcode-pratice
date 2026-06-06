class Solution {
    public int getSum(int a, int b) {
    int carry=0;
    int mask=0xffffffff;
    while (b!=0){
            carry=a&b;
            a=a^b;
            b=carry<<1;
    }
        return (a&mask) ==mask? a|~mask :a;
    }
}