# Richest Customer Wealth

# Note: beat only 9 % in runtime and 92 % in memory.

def richest_wealth(account):
    max_list = []
    for i in range(len(account)):
        total = 0
        for j in range(len(account[i])):
            total += account[i][j]
            max_list.append(total)

    return max(max_list)


accounts = [[1, 5], [7, 3], [3, 5]]
print(richest_wealth(accounts))
