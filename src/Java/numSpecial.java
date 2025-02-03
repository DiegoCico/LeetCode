class Solution {
    public int numSpecial(int[][] mat) {
       int m = mat.length, n = mat[0].length;
       int[] row_count = new int[m]; 
       int[] col_count = new int[n]; 

       for (int row = 0; row < m; row++) {
           for (int col = 0; col < n; col++) {
               if (mat[row][col] == 1) {
                   row_count[row]++;
                   col_count[col]++;
               }
           }
       }

       int count = 0;
       for (int row = 0; row < m; row++) {
           for (int col = 0; col < n; col++) {
               if (mat[row][col] == 1 && row_count[row] == 1 && col_count[col] == 1) {
                   count++; 
               }
           }
       }

       return count;
   }
}