# For any positive value of N, print 1 to N without using for or while loops via recursion (Reverse Countdown)


def reverse_number_using_recursion(n, reverse=0):

    if n == 0:
        return reverse
    else:
        reverse = reverse * 10 + n % 10
        return reverse_number_using_recursion(n // 10, reverse)


print(reverse_number_using_recursion(5))