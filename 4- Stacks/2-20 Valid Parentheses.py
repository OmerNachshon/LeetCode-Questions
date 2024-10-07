"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

 """

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {'{':'}','(':')','[':']'}
        for parentheses in s:
            if parentheses in hmap:
                stack.append(parentheses)
            else:
                if not stack or parentheses!= hmap[stack.pop()]:
                    return False
        return not len(stack)
