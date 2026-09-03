"""
LeetCode 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Approach: stack. Push openers. On a closer, the top of the stack must be its
matching opener or the string is invalid. At the end, the stack must be empty.

Time:  O(n)
Space: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in pairs:
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("(])", False),
        ("(", False),
        (")", False),
        ("", True),
    ]
    for s, expected in tests:
        result = sol.isValid(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: isValid({s!r}) = {result} (expected {expected})")
