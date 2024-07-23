# Assign Cookies
def findContentChildren( g, s):
    g.sort()
    s.sort()
    child = 0
    cookie = 0
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1
    return child