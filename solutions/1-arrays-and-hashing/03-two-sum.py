"""
LC 1 - Two Sum

Given an array of integers nums and an integer target, return the indices
of the two numbers that add up to target. Exactly one valid answer exists,
and the same element can't be used twice.

Approach:
    Instead of asking "what do these two numbers sum to", flip it: for each
    number, ask "what's the complement (target - num) I still need?" Track
    value -> index in a dict as we go. If the complement is already a key,
    we've found our pair. Single pass, O(n) time, O(n) space.
"""


def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []  # no solution found (shouldn't happen per problem guarantees)


if __name__ == "__main__":
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3, 3], 6) == [0, 1]
    assert twoSum([1, 5, 3, 8], 9) == [0, 3]   # 1 + 8 = 9
    assert twoSum([1, 5, 3, 8], 11) == [2, 3]  # 3 + 8 = 11

    print("All tests passed.")
