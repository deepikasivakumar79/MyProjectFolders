# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

def containsDuplicate(nums):
       
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            else:
                dic[nums[i]] = i
        return False
print(containsDuplicate([1,3]))