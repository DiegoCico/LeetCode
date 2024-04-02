package Java;

public class IsomorphicString {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] mapSToT = new int[256];
        int[] mapTToS = new int[256];

        for (int i = 0; i < s.length(); i++) {
            char charS = s.charAt(i);
            char charT = t.charAt(i);

            if (mapSToT[charS] == 0) {
                mapSToT[charS] = charT;
            } else if (mapSToT[charS] != charT) {
                return false;
            }

            if (mapTToS[charT] == 0) {
                mapTToS[charT] = charS;
            } else if (mapTToS[charT] != charS) {
                return false;
            }
        }

        return true;
    }
}
