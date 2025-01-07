class Solution {
    public String reverseWords(String s) {
        ArrayList<String> list = new ArrayList<>(Arrays.asList(s.split(" ")));
        ArrayList<String> newlist = new ArrayList();
        for (String word : list) {
            if (word.equals(""))
                continue;
            
            newlist.addFirst(word);
        }
        return String.join(" ", newlist);
    }
}