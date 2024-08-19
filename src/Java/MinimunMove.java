class Solution {
    public int minMoves(int[][] rooks) {
        int n = rooks.length;
        
        // Sort rooks by their row positions
        Arrays.sort(rooks, (a, b) -> Integer.compare(a[0], b[0]));
        
        // Target positions after sorting by rows
        int[] targetRows = new int[n];
        for (int i = 0; i < n; i++) {
            targetRows[i] = i;
        }
        
        // Calculate moves needed to place each rook in its target row
        int rowMoves = 0;
        for (int i = 0; i < n; i++) {
            rowMoves += Math.abs(rooks[i][0] - targetRows[i]);
        }
        
        // Sort rooks by their column positions
        Arrays.sort(rooks, (a, b) -> Integer.compare(a[1], b[1]));
        
        // Target positions after sorting by columns
        int[] targetCols = new int[n];
        for (int i = 0; i < n; i++) {
            targetCols[i] = i;
        }
        
        // Calculate moves needed to place each rook in its target column
        int colMoves = 0;
        for (int i = 0; i < n; i++) {
            colMoves += Math.abs(rooks[i][1] - targetCols[i]);
        }
        
        // Total moves is the sum of row moves and column moves
        return rowMoves + colMoves;
    }
}