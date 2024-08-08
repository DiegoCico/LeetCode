class Solution {
    public boolean isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        int x = Math.abs(sx - fx);
        int y = Math.abs(sy - fy);

        if(x == 0 && y == 0 && t == 0) return true;
        else if(x == 0 && y == 0 && t < 2) return false;
        else if(t >= y && t>=x) return true;
        else return false;
    }
}