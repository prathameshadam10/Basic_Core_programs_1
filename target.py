# Given an array of integers, find all unique triplets in the array that sum up to a target value.
def find_unique_triplets(nums, target):
    """
    Finds the list of unique triplets with the given target
    :param nums: list
    :param target: int
    :return: all_triplets
    """
    nums.sort()
    all_triplets = []

    for i in range(len(nums) - 2):
        sum = target - nums[i]

        start = i + 1
        end = len(nums) - 1
        while start < end:
            t = nums[start] + nums[end]
            if t == sum:
                all_triplets.append([nums[start], nums[end], nums[i]])
                start += 1
                end -= 1
            elif t < sum:
                start += 1
            else:
                end -= 1
    return all_triplets


if __name__ == '__main__':
    my_array = [-1, 0, 1, 2, -1, -4]
    target_sum = 0
    all_triplets = find_unique_triplets(my_array, target_sum)
    print("Triplets with the sum of", target_sum, "are:")
    print(all_triplets)
