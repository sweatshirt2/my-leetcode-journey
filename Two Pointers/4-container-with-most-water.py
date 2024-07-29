def maxContainer(heights: list[int]) -> list[int]:
    i, j = 0, len(heights) - 1
    capacity = 0
    while i < j:
        capacity = max(capacity, min(heights[i], heights[j]) * (j - i))
        if heights[i] < heights[j]:
            i += 1
            continue
        j -= 1
    return capacity