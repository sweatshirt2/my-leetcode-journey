def twoSum2(nums: list[int], target: int) -> list[int]:
    j = len(nums) - 1
    while j > -1:
        if nums[j] < target:
            break
        j -= 1
    i = 0
    while i < j:
        if (nums[i] + nums[j]) == target:
            return [i, j]
        if (nums[i] + nums[j]) < target:
            i += 1
            continue
        j -= 1
    return []