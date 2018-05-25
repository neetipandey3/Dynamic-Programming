'''
Dynamic Programming
Longest Common Substring)
Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.

Examples :

Input : X = "abcdxyz", y = "xyzabcd"
Output : 4
The longest common substring is "abcd" and is of
length 4.

Input : X = "zxabcdezy", y = "yzabcdezx"
Output : 6
The longest common substring is "abcdez" and is of
length 6.
'''

class LCS:

    def lcsDP(self, string1, string2, m, n):
        value_table = [[0 for val in range(m + 1)] for val in range(n + 1)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    value_table[i][j] = 0
                if string1[i] == string2[j]:
                    value_table[i][j] = value_table[i - 1][j - 1] + 1
                else:
                    value_table[i][j] = max(value_table[i - 1][j], value_table[i][j - 1])

        return value_table[i][j]


def main():
    lcs = LCS()
    string1= "abcdxyz"
    string2 = "xyzabcd"
    print("Longest Common Substring = {}".format(lcs.lcsDP(string1, string2, len(string1), len(string2))))

if __name__ == "__main__":
    main()