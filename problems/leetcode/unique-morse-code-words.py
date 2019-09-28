# https://leetcode.com/problems/unique-morse-code-words/


def uniqueMorseRepresentations(words: list) -> int:
    pattern = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
               "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # zip !!!!!!!!!!!!!
    dic = dict(zip(letters, pattern))

    words_m = []

    for word in words:
        word_m = ""
        for letter in word:
            word_m += dic.get(letter)
        words_m.append(word_m)

    reuslt = len(dict.fromkeys(words_m))

    return reuslt


words = ["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(words))
