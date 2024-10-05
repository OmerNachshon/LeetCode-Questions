"""
You're given strings jewels representing the types of stones that are jewels,
 and stones representing the stones you have.
 Each character in stones is a type of stone you have.
 You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

class Solution: # time complexity: O(n)
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        jewels = set(jewels)
        for stone in stones:
            if stone in jewels:
                counter+=1
        return counter


if __name__ == '__main__':
    sol = Solution()
    print(sol.numJewelsInStones(jewels="aA",stones="aAAbbbb"))
