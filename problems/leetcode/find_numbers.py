from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = filter(bool, map(lambda x: len(str(x)) % 2 == 0 and x, nums))
        return len(list(result))

    def find_numbers(self, nums: List[int]) -> int:
        return sum(len(str(n)) % 2 == 0 for n in nums)


if __name__ == '__main__':
    assert Solution().findNumbers([12, 345, 2, 6, 7896]) == 2, "Invalid case 1"
    assert Solution().findNumbers([555, 901, 482, 1771]) == 1, "Invalid case 2"
    print("Test completed")
