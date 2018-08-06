'''

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".


Solution:
table A[][] to store max length of subsequences

A[i][j] = {2+ A[i+1][j-1] if s[i]==s[j], or max(A[i+1][j], A[i][j-1])}

Base Case:
A[i][i] = 1 # for all one character subsequence

'''

class LongestPalindromicSubSequence:

    def LPS_dp(self, s: str):
        str_len = len(s)
        table = [[0 for _ in range(str_len)] for _ in range(str_len)]

        #Base Case initialization - could already be taken care of during table
        # initialization for all table[i][i] = 1
        for i in range(str_len):
            table[i][i] = 1

        #for n in range(2, str_len+1): #loop for length of subsequence
            #for i in range(str_len-n+1):
                #j = i+n-1
        for j in range(1, len(s)):
                for i in reversed(range(j)):
                    table[i][j] = 2 + table[i + 1][j - 1] if s[i] == s[j] else max(table[i + 1][j], table[i][j - 1])
        return table[0][str_len-1]

def main():
    lps = LongestPalindromicSubSequence()
    print("Length of Longest Palindromic Subsequence is {}".format(lps.LPS_dp("bbbab")))



if __name__ == "__main__":
    main()


