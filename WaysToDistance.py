'''
Dynamic Programming:
Count number of ways to cover a distance
Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps.

Examples :

Input:  n = 3
Output: 4
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step

Input:  n = 4
Output: 7

**** Method #1: Recursion. Method #2: Memoization

'''

class WaysToDistance:
    #Recursion
    def getWaysToDistanceRec(self, dist: int):
        if dist < 0:
            return 0

        if dist == 0:
            return 1

        for i in range(1, dist + 1):
            return self.getWaysToDistanceRec(dist - 1) + self.getWaysToDistanceRec(
                dist - 2) + self.getWaysToDistanceRec(dist - 3)

    #Memoization (Dynamic Programming)
    def getWayToDistanceDP(self, dist: int):
        value_table = [0 for val in range(dist+1)]

        # 1, 1, and 2 ways respectively as base case
        value_table[0] = 1
        value_table[1] = 1
        value_table[2] = 2

        for i in range(3, dist + 1):
            value_table[i] = value_table[i - 1] + value_table[i - 2] + value_table[i - 3]

        return value_table[dist]

def main():
    ways_to_distance = WaysToDistance()
    print(ways_to_distance.getWaysToDistanceRec(4))
    print(ways_to_distance.getWayToDistanceDP(4))

if __name__ == "__main__":
    main()


