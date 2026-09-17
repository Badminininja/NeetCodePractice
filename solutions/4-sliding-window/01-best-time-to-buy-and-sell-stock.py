"""
LeetCode 121. Best Time to Buy and Sell Stock

Given an array prices where prices[i] is the price of a given stock on day
i, find the maximum profit achievable by buying on one day and selling on
a later day. If no profit is possible, return 0.

Approach: single pass tracking the lowest price seen so far (low) and the
running high reached since that low (high). Whenever a new price undercuts
low, it becomes the new low and high resets to match it - there's no
profit left to find against the old low once a cheaper buy point exists.
Whenever a price reaches or exceeds the current high, it becomes the new
high and max profit is re-checked against high - low. Prices strictly
between low and high never beat the already-recorded high - low, so they
don't need their own check.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        low = prices[0]
        high = prices[0]

        for price in prices:
            if price < low:
                low = price
                high = low
            elif price >= high:
                high = price
                maxProfit = max(maxProfit, high - low)

        return maxProfit


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([3, 3, 3, 3], 0),
        ([1, 2, 3, 4, 5], 4),
        ([2, 4, 1, 7], 6),
    ]
    for prices, expected in tests:
        result = sol.maxProfit(prices)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: maxProfit({prices}) = {result} (expected {expected})")
