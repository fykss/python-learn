from typing import List


def distribute_candies(candies: List[int]) -> int:
    n = len(candies) // 2

    return min(len(set(candies)), n)


print(distribute_candies([1, 1, 2, 3]))
