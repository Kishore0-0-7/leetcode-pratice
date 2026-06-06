static inline void push(char st[],int *top,char ch){
    st[++(*top)]=ch;
}
static inline int pop(char st[],int *top){
    return st[(*top)--];
}
int minLength(char * s){
    char st[100];
    int top=-1;
    int k=strlen(s);
    for(int i=0;i<k;i++){
        if(top==-1){
            push(st,&top,s[i]);
        }
        else if((s[i]=='B' && st[top]== 'A') || (s[i] == 'D' && st[top]=='C')){
            pop(st,&top);
        }
        else{
            push(st,&top,s[i]);
        }
    }
    return top+1;
}