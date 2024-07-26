def productExceptSelf(nums: list[int]) -> list[int]:
    l = len(nums)
    products = [1] * l
    for i in range(1, l):
        products[i] = products[i - 1] * nums[i - 1]
    cumulative = nums[l]
    for i in range(l - 2, -1, -1):
        products[i] *= cumulative
        cumulative *= nums[i]
    return products