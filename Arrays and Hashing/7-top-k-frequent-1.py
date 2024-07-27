def kFrequent(nums: list[int], k: int) -> list[int]:
    if len(nums) == 0:
        return []
    tracker = {}
    for num in nums:
        tracker[num] = tracker.get(num, 0) + 1
    counter = [[] for i in range(len(nums) - 1)]
    largest = 1
    for key, val in tracker.items():
        counter[val].append(key)
        largest = max(largest, val)
    top_k = []
    for i in range(largest, -1, -1):
        for num in counter[i]:
            top_k.append(num)
            if len(top_k) == k:
                return top_k