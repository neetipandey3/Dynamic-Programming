'''
Dynamic Programming-

Longest Common Substring:
The program finds the max such length and sub-sequence


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


Returns: LCS length, LCS

'''

class LCS:

    def lcsDP(self, string1, string2, m, n):
        value_table = [[0 for val in range(m + 1)] for val in range(n + 1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if string1[i-1] == string2[j-1]:
                    value_table[i][j] = value_table[i - 1][j - 1] + 1
                else:
                    value_table[i][j] = max(value_table[i - 1][j], value_table[i][j - 1])

        #code to trace back (bottom-up) the sub-sequence

        lcs = ""
        i = m
        j = n

        while i > 0 and j > 0:
            #move diagonally up with the letters match
            if string1[i-1] == string2[j-1]:
                lcs += string1[i-1]
                i -= 1
                j -= 1

            #move in the direction of max value it came from (up or down)
            else:
                if value_table[i-1][j] > value_table[i][j-1]:
                    i -= 1
                else:
                    j -= 1

        return value_table[m][n], lcs[::-1]



def main():
    lcs = LCS()
    string1= "abcdxyz"
    string2 = "xyzabcd"
    print("Longest Common Substring (length & sub-sequence) = {}".format(lcs.lcsDP(string1, string2, len(string1), len(string2))))

if __name__ == "__main__":
    main()