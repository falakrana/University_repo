# Find Number with Even Number of Digits.


def number_with_even_digit(l):
    count = 0
    for i in l:
        if len(str(i)) % 2 == 0:
            count += 1
    return count

l = [12,345,2,6,7896]

print(number_with_even_digit(l))
