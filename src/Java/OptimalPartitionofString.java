class Solution {
    public int partitionString(String s) {
        ArrayList<String> list = new ArrayList<>();
        String word = "";
        for (int i = 0; i < s.length(); i++) {
            String character = "" + s.charAt(i);
            System.out.println(character);
            if (!word.contains(character)) {
                word += character;
            } else {
                list.add(word);
                word = character;
            }
        }
        if (!word.isEmpty()) {
            list.add(word);
        }
        System.out.println(list);
        return list.size();
    }
}
