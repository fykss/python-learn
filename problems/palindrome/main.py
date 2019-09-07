import math

palindrome = "palindrome string"
string = "ababa"


# short solve
if string[::-1] == string:
    print(string, "palindrome string")
else:
    print(string, "not palindrome string")


# ternary view
print(string, palindrome) if string[::-1] == string else print(string, "not", palindrome)


# separating by char using loop
def isPalindrome(str):
    for i in range(0, math.floor(len(string)/2)):
        if str[i] != str[len(str) - 1 - i]:
            return False
    return True


print(isPalindrome(string))


# using extra variable
reverse_str = ""
for i in string:
    reverse_str = i + reverse_str
    if string == reverse_str:
        print(string, palindrome)
