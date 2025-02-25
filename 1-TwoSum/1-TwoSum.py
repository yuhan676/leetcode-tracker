class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # HashMap to store the number and its index
        num_map = {}
        
        for i, num in enumerate(nums):
            # Find the complement
            complement = target - num
            
            # If complement exists in the map, return the indices
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, add the number and its index to the map
            num_map[num] = i
        
        # If no solution is found, raise an exception (though we are guaranteed there will be a solution)
        raise ValueError("No two sum solution")
