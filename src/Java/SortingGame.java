package Java;

import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class SortingGame {
    public int[] deckRevealedIncreasing(int[] deck) {
        Arrays.sort(deck);
        Deque<Integer> deque = new LinkedList<>();

        for (int i = deck.length - 1; i >= 0; --i) {
            if (!deque.isEmpty()) {
                deque.addFirst(deque.removeLast());
            }
            deque.addFirst(deck[i]);
        }

        for (int i = 0; i < deck.length; ++i) {
            deck[i] = deque.removeFirst();
        }

        return deck;
    }
}
