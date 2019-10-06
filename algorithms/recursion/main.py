# Required recursion conditions:
# 1) recurrence case
# 2) extreme case


# simple recursion
def counddown(i):
    print(i)
    if i <= 0:
        return
    else:
        counddown(i-1)


counddown(10)

# matryoshka
def matryoshka(n):
    if n == 1:
        print("The smallest matryoshka")
    else:
        print("Top matryoshka n=", n)
        matryoshka(n-1)
        print("Down matryoshka n=", n)


matryoshka(5)
