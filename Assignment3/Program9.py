# Find length of string recursion


def length_string(ptr):
    if ptr == "":
        return 0
    else:
        return 1 + length_string(ptr[1:])
