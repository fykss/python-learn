class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int: 
        return sum(True if c_j == c_s else False for c_j in J for c_s in S)

    def num_jewels_in_stones_1(self, J: str, S: str) -> int:
        return sum(s in J for s in S)

    def num_jewels_in_stones_2(self, J: str, S: str) -> int:
        return sum(map(S.count, J))  # Equal sum(map(lambda c: S.count(c), J))


if __name__ == '__main__':
    assert Solution().numJewelsInStones(J = "aA", S = "aAAbbbb") == 3, "Invalid case 1 def numJewelsInStones"
    assert Solution().numJewelsInStones(J = "z", S = "ZZ") == 0, "Invalid case 2 def numJewelsInStones"

    assert Solution().num_jewels_in_stones_1(J = "aA", S = "aAAbbbb") == 3, "Invalid case 1 def num_jewels_in_stones_1"
    assert Solution().num_jewels_in_stones_1(J = "z", S = "ZZ") == 0, "Invalid case 2 def num_jewels_in_stones_1"

    assert Solution().num_jewels_in_stones_2(J = "aA", S = "aAAbbbb") == 3, "Invalid case 1 def num_jewels_in_stones_2"
    assert Solution().num_jewels_in_stones_2(J = "z", S = "ZZ") == 0, "Invalid case 2 def num_jewels_in_stones_2"

    print("Test completed") 