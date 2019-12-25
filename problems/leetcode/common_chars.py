from collections import Counter
from typing import List


def common_chars(A: List[str]) -> List[str]:
    word_first = Counter(A[0])
    for word in A:
        counter_word = Counter(word)
        for key in word_first.keys():
            word_first[key] = min(word_first[key], counter_word[key])
    return list(word_first.elements())


test_1 = ["bella", "label", "roller"]
test_2 = ["cool", "lock", "cook"]

print(common_chars(test_1))
print(common_chars(test_2))
