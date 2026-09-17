"""
LeetCode 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without
duplicate characters.

Approach: sliding window with two pointers, left and right, and a dict
mapping each character to the index it was last seen at. right drives a
single forward pass over the string. Whenever the character at right was
already seen *and* that occurrence is still inside the current window
(library[char] >= left), left jumps to just past it - anything before that
can't be part of a valid window anymore anyway. The dict is never cleared;
a stale entry from before left just gets ignored by the >= left check, so
there's no need to restart the scan.

Time:  O(n)
Space: O(min(n, alphabet size))
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        library = {}
        maxOutput = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] in library and library[s[right]] >= left:
                left = library[s[right]] + 1
            library[s[right]] = right
            maxOutput = max(maxOutput, right - left + 1)
            right += 1

        return maxOutput


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("dvdf", 3),
        ("abba", 2),
        ("tmmzuxt", 5),
    ]
    for s, expected in tests:
        result = sol.lengthOfLongestSubstring(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: lengthOfLongestSubstring({s!r}) = {result} (expected {expected})")
