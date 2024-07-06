# Count Number of Zeros in a Number using recursion

def Count_zero(n, count=0):
    if n == 0:
        if count == 0:
            return 1
        else:
            return count
    else:
        if n % 10 == 0:
            count += 1
        return Count_zero(n // 10, count)


print(Count_zero(20044020))