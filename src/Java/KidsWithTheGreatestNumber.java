import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class kidsWithGreatest {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        ArrayList<Boolean> list = new ArrayList<>();

        int maxNumber = 0;
        for(int i: candies){
            if (maxNumber<i){
                maxNumber = i;
            }
        }

        for(int i : candies){
            if(i + extraCandies >= maxNumber)
                list.add(true);
            else 
                list.add(false);
        }
        return list;
    }
}