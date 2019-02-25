# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) --> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) --> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) --> False


def spy_game(nums):
    james = []
    bond = [0, 0, 7]
    index = 0

    while index <= len(nums):
        for i in nums:
            if i == 0 or i == 7:
                james.append(i)
                index += 1
                if james == bond:
                    return True
                else:
                    continue
            if i != 0 or i != 7:
                index += 1
                if james == bond:
                    return True
                else:
                    continue
    else:
        return False


# Check
spy_game([1, 2, 4, 0, 0, 7, 5])

# Check
spy_game([1, 0, 2, 4, 0, 5, 7])

# Check
spy_game([1, 7, 2, 0, 4, 5, 0])

