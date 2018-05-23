'''
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
'''
class MaxProduct:
    def maxProductRec(self, num):
        """
        :type n: int
        :rtype: int
        """
        if num == 0 or num == 1:
            return 0

        max_product = 0
        # Recursion:
        for n in range(1, num-1):
            max_product = max(max_product, max(n * num - n, self.maxProductRec(num - n) * n))

        return max_product

    def maxProductDP(self, num):
        """
                :type n: int
                :rtype: int
                """
        # building the table bottom-up (1 D)
        # using memoisation
        values = [0] * (num+1)

        for i in range(2, num+1):
            for j in range(1, i):
                values[i] = max(values[i], max(i - j, values[i - j]) * j)

        return values[num]

def main():
    int_max_product = MaxProduct()
    print(int_max_product.maxProductDP(10))

if __name__ == "__main__":
    main()