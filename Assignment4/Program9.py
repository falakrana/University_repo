# Relative Ranks


def findRelativeRanks(score):
    sorted_one = sorted(score, reverse=True)

    answer = [""] * len(score)

    rank_ = {
        sorted_one[0]: "Gold Medal",
        sorted_one[1]: "Silver Medal",
        sorted_one[2]: "Bronze Medal",
    }

    for i in range(len(score)):
        s = score[i]
        if s in rank_:
            answer[i] = rank_[s]
        else:
            answer[i] = str(sorted_one.index(s) + 1)

    return answer


score = [10,3, 23]
print(findRelativeRanks(score))
