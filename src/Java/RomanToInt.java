package Java;

public class RomanToInt {
    public int romanToInt(String s) {
        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'I') {
                if (i + 1 < s.length() && s.charAt(i + 1) == 'V') {
                    total += 4;
                    i++;
                } else if (i + 1 < s.length() && s.charAt(i + 1) == 'X') {
                    total += 9;
                    i++;
                } else {
                    total += 1;
                }
            } else if (c == 'V') {
                total += 5;
            } else if (c == 'X') {
                if (i + 1 < s.length() && s.charAt(i + 1) == 'L') {
                    total += 40;
                    i++;
                } else if (i + 1 < s.length() && s.charAt(i + 1) == 'C') {
                    total += 90;
                    i++;
                } else {
                    total += 10;
                }
            } else if (c == 'L') {
                total += 50;
            } else if (c == 'C') {
                if (i + 1 < s.length() && s.charAt(i + 1) == 'D') {
                    total += 400;
                    i++;
                } else if (i + 1 < s.length() && s.charAt(i + 1) == 'M') {
                    total += 900;
                    i++;
                } else {
                    total += 100;
                }
            } else if (c == 'D') {
                total += 500;
            } else if (c == 'M') {
                total += 1000;
            }
        }
        return total;
    }
}
