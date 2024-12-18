class Solution {
    public boolean validPalindrome(String s) {
    int l = s.length();
    if(l==0|| l==1) return true;
    boolean deleted = false;
    for (int i = 0, j = l - 1; i < j; i++, j--) {
        //System.out.println("\ni=" + i + " ; j=" + j);
        if (s.charAt(i) != s.charAt(j)) {
            if (deleted) return false;
            else {
                deleted = true;
                //System.out.println("i=" + i + " ; j=" + j);
                return isPalindrome(s.substring(i+1, j+1)) 
                                    || isPalindrome(s.substring(i, j));
            }
        }
    }
    return true;
}

boolean isPalindrome(String s) {
    //System.out.println(s);
    if(s == null || s.length()==0|| s.length()==1) return true;
    int l = s.length();
    char[] chars = s.toCharArray();
    for (int i = 0, j = l - 1; i < j; i++, j--) {
        if (s.charAt(i) != s.charAt(j)) return false;
    }
    return true;
}
}   