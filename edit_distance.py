def calculate_lcs_length(a,b):
    a_len = len(a)
    b_len = len(b)
    dp = []
    for i in range(a_len + 1):
        dp.append([0 for j in range(b_len + 1)])
    for i in range(1, a_len + 1):
        for j in range(1, b_len + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j - 1])
    max_length = dp[a_len][b_len]
    return max_length

def EditDistance(s, t):
    """
        Computes levenshtein distance between two strings
    """
    sourceLen = len(s)
    targetLen = len(t)
    if sourceLen == 0:
        return targetLen
    elif targetLen == 0:
        return sourceLen

    s = ' ' +s
    t = ' ' +t
    sourceLen += 1
    targetLen += 1
    d = [[0 for j in range(targetLen)] for i in range(sourceLen)]

    # Source prefix can be transformed to empty string as follows
    for i in range(1, sourceLen):
        d[i][0]= i

    for j in range(1, targetLen):
        d[0][j] = j

    for i in range(1, sourceLen):
        for j in range(1, targetLen):
            if s[i] == t[j]:
                subCost = 0
            else:
                subCost = 1

            d[i][j] = min(
                d[i-1][j] +1,
                d[i][j-1] +1,
                d[i-1][j-1] + subCost,
            )

            # Add transposition
            if i>1 and j>1 and s[i] == t[j-1] and s[i-1] == t[j]:
                d[i][j] = min(
                        d[i][j],
                        d[i-2][j-2] + 1)

    return d[sourceLen-1][targetLen-1]

# def search(ind, term, threshold):
#     """
#         Takes an index and searches through it
#     """
#     a = AVLTree()
# 
#     if len(term) == 0:
#         return []
#     
#     for elem in list(term):
#         # print('Processing %s' % elem)
#         ind[elem].search(term, threshold, a)
#     return a.inorder_traverse()
