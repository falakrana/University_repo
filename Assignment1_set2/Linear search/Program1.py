# Find the maximum number in a list
def maximum_element(l):
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return max


l = [1, 32, 8, 4, 13, 42, 24]

print(maximum_element(l))



