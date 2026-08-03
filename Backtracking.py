class Solution(object):
    def subsets(self,nums=[1,2,3]):
        result = []
        def back(index ,path):
            if index == len(nums):
                result.append(path[:])
                return
            path.append(nums[index])
            back(index+1,path)
            path.pop()

            back(index+1,path)

        back(0,[])
        return result