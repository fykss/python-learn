# class Solution:

# My Solution
def maxNumberOfBalloons(self, text: str) -> int:
    ballon = [0] * 5   

    for c in text:
        if c == 'b':
            ballon[0] += 1
        elif c == 'a':
            ballon[1] += 1
        elif c == 'l':
            ballon[2] += 1
        elif c == 'o':
            ballon[3] += 1
        elif c == 'n':
            ballon[4] += 1

    ballon[2] //= 2
    ballon[3] //= 2

    Answer = max(ballon)

    for i in ballon:
        if i < Answer:
            Answer = i

    return Answer
        

# Another solution
def maxNumberOfBalloons_1(self, text: str) -> int:
	   return int(min({text.count(char) / 'balloon'.count(char) 
					   for char in list('balloon')}))


for char in list('balloonnn'):
    print('balloonnn'.count(char))

text = 'balloonnn'

# result = int(min({text.count(char) / 'balloon'.count(char) for char in list('balloon')}))
result = {text.count(char) / 'balloon'.count(char) for char in list('balloon')}
# print(text.count(char))