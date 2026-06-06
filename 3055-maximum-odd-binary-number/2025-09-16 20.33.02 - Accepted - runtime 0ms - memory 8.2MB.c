char* maximumOddBinaryNumber(char* s) {
    int ones = 0;
        for (int i=0; i<strlen(s);i++) {
            if (s[i]=='1') {
                s[i]='0';
                ones++;
            }
        }
        if (ones>1) {
            for (int i=0;i<ones-1;i++) {
                s[i]='1';
            }
        }
        s[strlen(s)-1]='1';
        return s;
}