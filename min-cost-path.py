'''
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of minimum cost
 path to reach (m, n) from (0, 0). Each cell of the matrix represents a cost to traverse through that cell.
 Total cost of a path to reach (m, n) is sum of all the costs on that path (including both source and destination).
 You can only traverse down, right and diagonally lower cells from a given cell, i.e., from a given cell (i, j),
 cells (i+1, j), (i, j+1) and (i+1, j+1) can be traversed. You may assume that all costs are positive integers.

For example, in the following figure, what is the minimum cost path to (2, 2)?

1   2   3
4   8   2
1   5   3

The path with minimum cost is highlighted in the following figure.
 The path is (0, 0) –> (0, 1) –> (1, 2) –> (2, 2).
 The cost of the path is 8 (1 + 2 + 2 + 3).

'''

class MinCostPath:

    def getMinCostPath(self, costs: list, r, c):

        cost_table = [[0 for val in range(c+1)] for val in range(r+1)]

        cost_table[0][0] = costs[0][0]
        for j in range(1, (c+1)):
            cost_table[0][j] = cost_table[0][j-1] + costs[0][j]
        for i in range(1, (r+1)):
            cost_table[i][0] = cost_table[i-1][0] + costs[i][0]


        for i in range(1, r+1):
            for j in range(1, c+1):
                cost_table[i][j] = min(cost_table[i-1][j-1], cost_table[i-1][j], cost_table[i][j-1]) + costs[i][j]


        i = r
        j = c

        path = [(i, j)]

        while i>0 and j>0:

            if cost_table[i-1][j] > cost_table[i][j-1]:
                if cost_table[i-1][j-1] > cost_table[i][j-1]:
                    j -= 1
                else:
                    i -= 1
                    j -= 1
            elif cost_table[i-1][j-1] > cost_table[i-1][j]:
                i -= 1
            else:
                i -= 1
                j -= 1
            path.append((i, j))

        #add (0, 0) to the path - the beginning point for traversal
        return cost_table[r][c], path[::-1]





def main():
    minCostPath = MinCostPath()
    min_cost, min_cost_path = minCostPath.getMinCostPath([[1, 2, 3], [4, 8, 2], [1, 5, 3]], 2, 2)
    print(min_cost)
    print(min_cost_path)

    #return minCostPath.getMinCostPath()

if __name__ == "__main__":
    main()