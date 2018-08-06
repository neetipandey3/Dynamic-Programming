'''Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
    '''


class Subsequences:
    def num_distinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int

        Solution:
        Base case, "" as subsequence in S but not in T => DP[i][0] = 1
        if the last_char(S) != last_char(T),
            drop the last_char in S and continue counting
            A[i][j] = A[i-1][j] -(1)
        else,
            count = (1) + substrings afters dropping last char in both, S & T
            A[i][j] = A[i-1][j-1]

        """


        table = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

        #Base Case
        for i in range(len(s)+1):
            table[i][0] = 1

        #DP /Memoization
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i - 1] != t[j - 1]:
                    table[i][j] = table[i - 1][j]
                else:
                    table[i][j] = table[i - 1][j] + table[i - 1][j - 1]

        return table[len(s)][len(t)]

def main():
    subs = Subsequences()
    s= "rabbbit"
    t = "rabbit"
    print(subs.num_distinct(s, t))

if __name__ == "__main__":
    main()



