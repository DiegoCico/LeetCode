class Solution {
    public String reverseVowels(String s) {
        List<String> charList = Arrays.asList(s.split(""));
        return reverse(0, s.length()-1, charList);
    }

    public String reverse(int start, int end, List<String> s) {
    List<String> vowels = List.of("a", "e", "i", "o", "u", "A", "E", "I", "O", "U");


    if (start >= end) {
        return String.join("", s);
    }

    if (vowels.contains(s.get(start)) && vowels.contains(s.get(end))) {
        String temp = s.get(start);
        s.set(start, s.get(end));
        s.set(end, temp);
        return reverse(++start, --end, s);
    }
    
    if (!vowels.contains(s.get(start))) {
        return reverse(++start, end, s);
    }

    if (!vowels.contains(s.get(end))) {
        return reverse(start, --end, s);
    }

    return String.join("", s);
}
}