int minLengthAfterRemovals(char* s) {
 int a=0,b=0;
    for(int i=0;i<strlen(s);i++){
        if(s[i]=='a') a+=1;
        else b+=1;
    }
    return a>b?a-b:b-a;
}