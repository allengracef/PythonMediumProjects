def binary_search(num,target):
    l = 0
    r = len(num) -1

    while l <= r:

        mid = l + (r - l)//2

        if num[mid] == target:
            print(f"Target found at: {mid}")
            return mid

        if num[mid] > target:
            r = mid -1
        elif num[mid] < target:
            l = mid + 1
        else:
            return mid
num = [4,23,34,39,44,49,59,78,88]
binary_search(num,39)