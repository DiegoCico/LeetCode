import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

public class MeetingScheduler {
    class Solution {
    public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
	var minHeap1 = toMinHeap(slots1);
	var minHeap2 = toMinHeap(slots2);

	for (int[] slot1 = minHeap1.poll(), slot2 = minHeap2.poll(); slot1 != null && slot2 != null;) {
		var start = Math.max(slot1[0], slot2[0]);
		var end = Math.min(slot1[1], slot2[1]);

		if (end - start >= duration)
			return List.of(start, start + duration);
		if (slot1[1] > slot2[1])
			slot2 = minHeap2.poll();
		else
			slot1 = minHeap1.poll();
	}
	return List.of();
}

private Queue<int[]> toMinHeap(int[][] slots) {
	var minHeap = new PriorityQueue<int[]>(Comparator.comparingInt(slot -> slot[0]));
	Collections.addAll(minHeap, slots);
	return minHeap;
}
}
}
