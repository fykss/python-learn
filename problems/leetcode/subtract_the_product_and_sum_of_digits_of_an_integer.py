from functools import reduce
import operator


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """First solution"""
        product = 1
        sum = 0
        for c in str(n):
            product *= int(c)
            sum += int(c)
        return product - sum

    def subtractProductAndSum_1(self, n: int) -> int:
        """Another"""
        A = map(int, str(n))
        return reduce(operator.mul, A) - sum(A)


if __name__ == "__main__":
    assert Solution().subtractProductAndSum(1) == 0, "Invalid answer with value 1"
    assert Solution().subtractProductAndSum(22) == 0, "Invalid answer with value 22"
    print("Test completed")
