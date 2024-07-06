# For any positive value of N, print N to 1 without using for or while loops via recursion (Countdown)


def count_down(n):
    if n == 0:
        return
    else:
        print(n)
        count_down(n - 1)


print(count_down(5))