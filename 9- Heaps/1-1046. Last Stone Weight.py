"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

"""
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1 # Negate to force Max Heap

        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)

            if largest != next_largest:
                heapq.heappush(stones, largest - next_largest)

        return -heapq.heappop(stones) if stones else 0
