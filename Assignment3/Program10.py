# Reverse a string uing recursion


def recursive_reverse(ptr):
    # Base case
    if ptr == "":
        return ptr
    else:
        return recursive_reverse(ptr[1:]) + ptr[0]


string = "hello"
print(recursive_reverse(string))
