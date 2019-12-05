def path(m,n):
    """find num of ways go through m by n grids, given each time can only go up or go right"""
    if m==1 or n==1:
        return 1
    return path(m,n-1) + path(m-1, n)

def remove(x, s):
    index_x = s.index(x)
    return s[:index_x] + s[index_x+1:]

def merge(s1, s2):
    if s1==[]:
        return s2
    elif s2 == []:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    return [s2[0]] + merge(s1, s2[1:])

def mario_number(level):
    def ways(n):
        if n == len(level) - 1:
            return 1
        if n >= len(level) or level[n] == 'p':
            return 0
        return ways(n + 1) + ways(n + 2)
    return ways(0)
