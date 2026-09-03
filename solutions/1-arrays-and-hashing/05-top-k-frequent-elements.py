"""
LC 347 - Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent
elements. Answer can be returned in any order.

Approach (optimal - bucket sort):
    Frequency is bounded: a number can appear at most len(nums) times. So
    instead of sorting numbers by frequency (O(n log n)), use frequency
    itself as an array index - "bucket sort". buckets[f] holds every number
    that occurred exactly f times. Walk buckets from highest index down,
    collecting numbers until we have k. Every number is counted once and
    placed in exactly one bucket, so total work across both the counting
    pass and the bucket walk is O(n).
"""

from collections import Counter


def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # buckets[i] = list of numbers that appear exactly i times
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result

    return result


# Simpler (but O(n log n)) alternative using Python's Counter built-in -
# good to know exists, but the bucket-sort version above is the O(n) answer.
def topKFrequent_counter(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]


def _normalize(result: list[int]) -> set:
    return set(result)


if __name__ == "__main__":
    assert _normalize(topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert _normalize(topKFrequent([1], 1)) == {1}
    assert _normalize(topKFrequent([1, 2], 2)) == {1, 2}

    assert _normalize(topKFrequent_counter([1, 1, 1, 2, 2, 3], 2)) == {1, 2}

    print("All tests passed.")
