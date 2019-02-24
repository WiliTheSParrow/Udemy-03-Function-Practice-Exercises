# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
def has_33(nums):
    index=0
    for x in nums:
        index2 = index + 1
        if x == 3:
            if nums[index]==nums[index2]:
                return True
            else:
                return False
        index = index + 1
        
# Check
has_33([1, 3, 3])

# Check
has_33([1, 3, 1, 3])

# Check
has_33([3, 1, 3])
