def longestSequence(nums: list[int]) -> int:
    length = 1
    tracker = set(nums)
    for num in nums:
        if num - 1 not in tracker:
            l = 1
            while num + 1 in tracker:
                l += 1
            length = max(length, l)
    return length