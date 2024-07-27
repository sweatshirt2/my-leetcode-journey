def mostFrequent(nums: list[int], k:int) -> list[int]:
    tracker = {}
    for num in nums:
        tracker[num] = tracker.get(num, 0) + 1
    counter = [[] for i in range(len(nums))]
    largest = 1
    for key, val in tracker.items():
        counter[val].append(key)
        largest = max(largest, key)
    top_k = []
    for i in range(largest, -1, -1):
        top_k.extend(counter[i])
        if len(top_k) >= k:
            return top_k