"""
LC 217 - Contains Duplicate

Given an integer array nums, return True if any value appears at least
twice in the array, and False if every element is distinct.

Approach:
    Track "have I seen this number before" using a set (existence only,
    no need to count occurrences). Single pass, O(n) time, O(n) space.
"""


def containsDuplicate(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


# Alternate one-liner (mentioned as a follow-up, not the primary answer):
def containsDuplicate_oneliner(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


if __name__ == "__main__":
    assert containsDuplicate([1, 2, 3, 1]) is True
    assert containsDuplicate([1, 2, 3, 4]) is False
    assert containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert containsDuplicate([]) is False
    assert containsDuplicate([7]) is False

    assert containsDuplicate_oneliner([1, 2, 3, 1]) is True
    assert containsDuplicate_oneliner([1, 2, 3, 4]) is False

    print("All tests passed.")
