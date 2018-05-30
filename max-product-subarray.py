'''
Dynamic Programming:

Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''
import math
class MaxProductSubArray:
    def getMaxProdSubarray(self, nums: list):
        len_nums = len(nums)

        #product_tbl[1] = max(nums[0] * nums[1], nums[1])
        max_prod = [0 for i in range(len_nums)]
        min_prod = [0 for i in range(len_nums)]
        min_prod = [0 for i in range(len_nums)]
        max_prod[0] = nums[0]
        min_prod[0] = nums[0]
        max_result = nums[0]
        '''
        Need to handle two cases:
        1. max positive product thus far
        2. max negative product thus far, expecting a negative number in the subsequent index
        '''
        for i in range(1, len_nums):
            if nums[i] > 0:
                max_prod[i] = max(max_prod[i-1] * nums[i], nums[i])
                min_prod[i] = min(min_prod[i-1] * nums[i], nums[i])
            elif nums[i] == 0:

                #reset all the values to 1
                max_prod[i] = 0
                min_prod[i] = 0
            else:
                max_prod[i] = max(min_prod[i-1] * nums[i], nums[i])
                min_prod[i] = min(max_prod[i-1] * nums[i], nums[i])


            #min_result = min(min_product, min_result)
            max_result = max(max_prod[i], max_result)

        return max_result

def main():
    max_prod_subarray = MaxProductSubArray()
    print(max_prod_subarray.getMaxProdSubarray([2, 3, -2, 4]))
    print(max_prod_subarray.getMaxProdSubarray([-1, 0, -1]))
    print(max_prod_subarray.getMaxProdSubarray([-2, 3, -4]))  #Negative product scenario
    print(max_prod_subarray.getMaxProdSubarray([-4, -3]))
    print(max_prod_subarray.getMaxProdSubarray([0, 2]))
    print(max_prod_subarray.getMaxProdSubarray([2,-5,-2,-4,3]))

if __name__ == "__main__":
    main()



