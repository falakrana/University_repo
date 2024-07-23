# K Items with the maximum sum


def kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k):
    ones = [1] * numOnes
    zeros = [0] * numZeros
    neg_ones = [-1] * numNegOnes
    items = ones + zeros + neg_ones
    items.sort(reverse=True)
    return sum(items[:k])
