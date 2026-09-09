"""
LeetCode 125. Valid Palindrome

Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is
also case-insensitive and ignores all non-alphanumeric characters.

Approach: two pointers, left and right, starting at opposite ends and
walking toward each other. Skip past any non-alphanumeric character on
either side before comparing. Lowercase each character only at the point
of comparison, since by then both have already survived the alnum check
(cheaper than lowercasing the whole string up front).

Time:  O(n)
Space: O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        left = 0
        right = len(s) - 1

        while True:
            if left > right:
                return True
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        (" ", True),
        (".,", True),
        ("0P", False),
        ("a", True),
        ("ab", False),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon", True),
    ]
    for s, expected in tests:
        result = sol.isPalindrome(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: isPalindrome({s!r}) = {result} (expected {expected})")
