int minLengthAfterRemovals(char* s) {
 int a=0,b=0,n=strlen(s);
    for(int i=0;i<n;i++){
        if(s[i]=='a') a+=1;
        else b+=1;
    }
    return a>b?a-b:b-a;
}