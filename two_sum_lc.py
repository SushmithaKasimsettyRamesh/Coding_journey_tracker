'''Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.'''


def two_sum(nums, target):
    # Iterate through the array
    for i in range(len(nums)):
        # Iterate through the rest of the array
        for j in range(i + 1, len(nums)):
            # If the sum of the current pair equals the target, return their indices
            if nums[i] + nums[j] == target:
                return [i, j]

    # If no solution is found, return an empty list
    return []


# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
