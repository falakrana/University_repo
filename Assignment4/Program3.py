def playGame(nums):
    nums.sort()
    arr = []
    alice_turn = True

    while nums:
        if alice_turn:
            min_elem = nums.pop(0)
            arr.append(min_elem)
        else:
            min_elem = nums.pop(0)
            arr.append(min_elem)

        # Alternate the turn
        alice_turn = not alice_turn

    return arr


# Example usage:
nums = [5, 4, 2, 3]
result = playGame(nums)
print(result)
