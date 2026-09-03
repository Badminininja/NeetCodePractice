"""
LC 242 - Valid Anagram

Given two strings s and t, return True if t is an anagram of s (uses the
exact same characters, same counts, just rearranged), and False otherwise.

Note: NOT the same as checking if a string equals its own reverse - that
tests for a palindrome, a different property entirely.

Approach:
    Build a frequency dict from s, then "spend down" counts while walking
    t. Any character in t that's missing from the dict, or whose count has
    already hit 0, means it's not a valid anagram. O(n) time, O(n) space.
"""


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True


# Alternate one-liner - correct but O(n log n) due to sorting, vs O(n) above:
def isAnagram_oneliner(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    assert isAnagram("anagram", "nagaram") is True
    assert isAnagram("rat", "car") is False
    assert isAnagram("", "") is True
    assert isAnagram("a", "ab") is False
    assert isAnagram("listen", "silent") is True

    assert isAnagram_oneliner("anagram", "nagaram") is True
    assert isAnagram_oneliner("rat", "car") is False

    print("All tests passed.")
