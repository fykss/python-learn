# simple recursion
def counddown(i):
    print(i)
    if i <= 0:
        return
    else:
        counddown(i-1)


counddown(10)
