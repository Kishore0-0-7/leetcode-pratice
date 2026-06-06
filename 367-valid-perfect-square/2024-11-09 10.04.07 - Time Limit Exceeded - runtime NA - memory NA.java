class Solution {
    public boolean isPerfectSquare(int num) {
      int a=0;
      while (a*a<=num){
        a=a+1;
      }  
       return (a-1)*(a-1)==num; 
    }
}