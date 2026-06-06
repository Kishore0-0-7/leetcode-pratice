class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        String[] words=text.split(" ");
        Set<Character> brokenSet=new HashSet<>();

        for (char ch:brokenLetters.toCharArray()) {
            brokenSet.add(ch);
        }

        int count=words.length;

        for (String word:words) {
            for (char ch:brokenSet) {
                if (word.indexOf(ch)!=-1) {
                    count--;
                    break;
                }
            }
        }
        return count;
    }
}