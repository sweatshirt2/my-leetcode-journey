def threeSum(nums: list[int]) -> list[list[int]]:
    sums = []
    nums.sort()
    if nums[0] > 0:
        return []
    if nums[0] == 0:
        if nums[1] != 0 or nums[2] != 0:
            return []
    k = len(nums) - 1
    while k > 1:
        i = 0
        j = k - 1
        while i < j:
            sum = nums[i] + nums[j]
            if sum == -nums[k]:
                sums.append([nums[i], nums[j], nums[k]])
            if sum < -nums[k]:
                i += 1
                continue
            j -= 1
        k -= 1
    return sums