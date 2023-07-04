# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"

def two_sum(nums, target):
    # Create a dictionary to store the complement of each number and its index
    complement_dict = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in complement_dict:
            # Found a pair that sums to the target
            return [complement_dict[complement], i]

        # Add the current number and its index to the complement dictionary
        complement_dict[num] = i

    # No solution found
    return []


# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)
