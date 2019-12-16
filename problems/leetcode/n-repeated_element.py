def repeatedNTimes(self, A: List[int]) -> int:
    test_dict = {key: 0 for key in A}

    for i in A:
        if i in test_dict:
            test_dict[i] += 1

    for key, value in test_dict.items():
        if value == len(A) / 2:
            return key
