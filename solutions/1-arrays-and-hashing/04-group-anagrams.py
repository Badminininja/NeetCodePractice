"""
LC 49 - Group Anagrams

Given an array of strings, group the anagrams together. Anagrams can be
returned in any order.

Approach:
    Sorting the letters of a word produces a signature that's identical for
    every anagram of that word (e.g. "eat", "tea", "ate" all sort to "aet").
    Use a dict mapping signature -> list of original words, so no pairwise
    comparison between words is ever needed. Single pass, O(n * k log k)
    where k is the max word length (from sorting each word).
"""

from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = {}  # signature -> list of words

    for word in strs:
        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


# Same logic using defaultdict to skip the manual "if key not in groups" check.
def groupAnagrams_defaultdict(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())


def _normalize(result: list[list[str]]) -> set:
    """Helper for order-independent comparison in tests."""
    return {tuple(sorted(group)) for group in result}


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = _normalize([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])

    assert _normalize(groupAnagrams(strs)) == expected
    assert _normalize(groupAnagrams_defaultdict(strs)) == expected
    assert groupAnagrams([""]) == [[""]]
    assert _normalize(groupAnagrams(["a"])) == _normalize([["a"]])

    print("All tests passed.")
