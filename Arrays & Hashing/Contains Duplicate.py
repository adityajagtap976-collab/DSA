# Brute force way to check if the array contains duplicates
def contains_duplicate_brute(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


print(contains_duplicate_brute([1, 2, 3, 4, 5]))  # Output: False
print(contains_duplicate_brute([1, 2, 3, 4, 5, 1]))  # Output: True

# Complexity:

# Time: O(n^2) — two nested loops, each going through the array.

# Space: O(1) — only a constant amount of extra space is used.


# Hash based way to check if the array contains duplicates
def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


print(contains_duplicate([1, 2, 3, 4, 5]))  # Output: False
print(contains_duplicate([1, 2, 3, 4, 5, 1]))  # Output: True

# Complexity:

# Time: O(n) — one pass through the array, and each in check / add is O(1) average case.

# Space: O(n) — in the worst case (no duplicates), the set grows to hold every element.
