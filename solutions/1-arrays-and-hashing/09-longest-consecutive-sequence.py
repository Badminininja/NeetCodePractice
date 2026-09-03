"""
LC 128 - Longest Consecutive Sequence

Given an unsorted array of integers, return the length of the longest run
of consecutive integers (e.g. [100, 4, 200, 1, 3, 2] -> 4, for the run
1, 2, 3, 4). Must run in O(n) time.

Approach:
    Put everything in a set for O(1) lookups. The trap: walking forward
    from EVERY number (checking num+1, num+2, ...) looks O(1) per lookup
    but is actually O(n^2) overall, because a long run gets redundantly
    re-walked starting from every number inside it.

    Fix: only start a forward walk from a number that is the TRUE START of
    its sequence - detected by checking that (num - 1) is NOT in the set.
    Every other number in that run gets skipped in O(1) before any walk
    begins. Since only sequence-starts ever trigger a walk, and every
    number belongs to exactly one sequence, the total work summed across
    every walk in the whole run is bounded by n - true O(n).
"""


def longestConsecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # only start if this is a sequence's beginning
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest


if __name__ == "__main__":
    assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longestConsecutive([]) == 0
    assert longestConsecutive([1, 2, 0, 1]) == 3
    assert longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]) == 7

    print("All tests passed.")
