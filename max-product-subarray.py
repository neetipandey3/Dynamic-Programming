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

class MaxProductSubArray:
    def getMaxProdSubarray(self, nums: list):
        len_nums = len(nums)
        max_products = [0 for i in range(len_nums)]
        min_products = [0 for i in range(len_nums)]

        max_products[0] = min_products[0] = max_product = nums[0]


        #product_tbl[1] = max(nums[0] * nums[1], nums[1])
        '''
        Need to handle two cases:
        1. max positive product thus far
        2. max negative product thus far, expecting a negative number in the subsequent index
        '''
        for i in range(1, (len_nums)):
            if nums[i] > 0:
                max_products[i] = max(max_products[i-1]*nums[i], nums[i])
                min_products[i] = min(max_products[i - 1] * nums[i], nums[i])
            else:
                max_products[i] = min(max_products[i - 1] * nums[i], nums[i])
                min_products[i] = max(max_products[i - 1] * nums[i], nums[i])
            max_product = max(max_product, max_products[i])

        return max_product

def main():
    max_prod_subarray = MaxProductSubArray()
    print(max_prod_subarray.getMaxProdSubarray([2, 3, -2, 4]))
    print(max_prod_subarray.getMaxProdSubarray([-1, 0, -1]))
    print(max_prod_subarray.getMaxProdSubarray([-2, 3, -4]))  #Negative product scenario

if __name__ == "__main__":
    main()



