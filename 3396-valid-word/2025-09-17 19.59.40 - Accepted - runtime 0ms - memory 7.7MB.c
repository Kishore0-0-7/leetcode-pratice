bool isValid(char* word) {
    int n=strlen(word);
    if (n < 3) return false;
    int vowels=0, consonants=0;
    for (int i=0;i < n;i++) {
        char c=word[i];
        if (isalpha(c)) {
            char lower=tolower(c);
            if (lower=='a'||lower=='e'||lower=='i'||lower=='o'||lower=='u')
                vowels++;
            else
                consonants++;
        } else if (!isdigit(c)) {
            return false;
        }
    }

    return vowels >= 1 && consonants >= 1;
}