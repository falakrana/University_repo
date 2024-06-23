# Find if a character k is presesnt in a string


def find(string, k):
    for i in string:
        if i == k:
            return True
        else:
            return False


string = "Hello Falak"
print(find(string, "H"))
