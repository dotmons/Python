def twoSum(nums: list, target: int) -> list:

    temp: int = 0
    hashdict = {};

    for counter, elem in enumerate(nums):
        temp = abs(elem - target)
        if temp in hashdict:
            return [counter, hashdict[temp]]
        hashdict[elem] = counter

    return []


list = [2,7,11,15]
print(twoSum(list, 9))

