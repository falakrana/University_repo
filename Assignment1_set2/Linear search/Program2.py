# Find the minimum number in a list

def minimum_element(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min


l = [1, 32, 8, 4, 13, 42, 24]

print(minimum_element(l))



