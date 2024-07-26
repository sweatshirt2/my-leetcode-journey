def twoSum(nums: list[int], target: int) -> list[int]:
    tracker = {}
    for i in range(len(nums) - 1):
        diff = target - nums[i]
        if diff in tracker:
            return [tracker[diff], i]
        tracker[nums[i]] = i