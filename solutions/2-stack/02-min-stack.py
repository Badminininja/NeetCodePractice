"""
LC 155 - Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum
element, all in O(1) time.

Approach:
    Two parallel stacks. minStack holds the actual values. ActualMin holds
    two entries per push: (the min *before* this push, this push's value)
    if val is a new minimum, or (this push's value, the min *before* this
    push) otherwise - either way, ActualMin[-1] always ends up holding the
    correct running minimum as of this push. Popping removes one logical
    entry (two list entries) from each stack together, so they always stay
    in sync - no separately cached "current min" variable to go stale.

    Caught mid-build: self.getMin() reads live from ActualMin[-1], so
    calling it *after* already appending val in the same branch returns the
    value just appended, not the true previous minimum. Fix: capture
    self.getMin() into a local variable before mutating ActualMin, not
    after.

Time:  O(1) for every operation.
Space: O(n) - two entries in ActualMin per element in minStack.
"""


class MinStack:

    def __init__(self):
        self.minStack = []
        self.ActualMin = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if not self.ActualMin:
            self.ActualMin.append(val)
            self.ActualMin.append(val)
        else:
            if val < self.getMin():
                self.ActualMin.append(self.getMin())
                self.ActualMin.append(val)
            else:
                oldMin = self.getMin()
                self.ActualMin.append(val)
                self.ActualMin.append(oldMin)

    def pop(self) -> None:
        self.minStack.pop()
        self.ActualMin.pop()
        self.ActualMin.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.ActualMin[-1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2); ms.push(0); ms.push(-3)
    assert ms.getMin() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2
    print("Official example: PASS")

    ms2 = MinStack()
    ms2.push(5); ms2.push(3); ms2.push(7)
    assert ms2.getMin() == 3
    ms2.pop(); ms2.pop()
    ms2.push(4)
    assert ms2.getMin() == 4
    print("Pop-then-push case: PASS")

    ms3 = MinStack()
    ms3.push(1); ms3.push(1); ms3.push(2)
    assert ms3.getMin() == 1
    ms3.pop(); assert ms3.getMin() == 1
    ms3.pop(); assert ms3.getMin() == 1
    print("Duplicate-min case: PASS")

    print("All tests passed.")
