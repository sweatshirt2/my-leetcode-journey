def containsDuplicate(nums: list[int]) -> bool:
    tracker = set()
    for num in nums:
        if num in tracker:
            return True
        tracker.add(num)
    return False


def containsDuplicateCheckLength(nums: list[int]):
    num_set = set(nums)
    return len(nums) == len(num_set)