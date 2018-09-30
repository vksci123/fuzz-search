sum = 0
def substring(s, n):
    w = 1
    sum = 0
    while w <= n:
        i=0
        while i <= n-w:
            print (s[i:(i+w)])
            sum += int(s[i:(i+w)])
            i += 1
        w += 1
    return sum

# Solving using dynamic programming
# Let total number of substrings for a string is
# S = s1, s2, s3, s4, s5, ..., S

def main(s):
    print ('Output: ')
    print(substring(s, len(s)))
