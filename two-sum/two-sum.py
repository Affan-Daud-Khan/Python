def twoSum( nums, target):
        store={}
        for index,num in enumerate(nums):
            n = target - num
            if n not in store:
                store[num] = index
            else:
                print ([store[n], index])
                return [store[n], index]

twoSum([2,7,11,15], 9)
