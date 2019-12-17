from typing import List
from collections import Counter


#  My solution
def uncommonFromSentences(A: str, B: str) -> List[str]:
    A = A.split(" ")
    B = B.split(" ")

    counter = Counter(A + B).most_common()
    result = []

    for i in range(len(counter)):
        if counter[i][1] == 1:
            result.append(counter[i][0])

    return result


#  Another
def uncommonFromSentences_1(self, A: str, B: str) -> List[str]:
    both = A.split(' ') + B.split(' ')
    return [x for x in both if both.count(x) == 1]


res = uncommonFromSentences("Hello world", "Hello da")
print(res)
