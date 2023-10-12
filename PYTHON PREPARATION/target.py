# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
def target(nums,target):
    dic={}
    for i in range(len(nums)):
        val = target - nums[i]
        if val in dic:
            return [dic[val], i]
        else:
             dic[nums[i]] = i
    return [] 
print(target([2,7,11,8],9))       