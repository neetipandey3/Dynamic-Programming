'''
Dynamic Programming:

Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"


Solution:

A[i][j] = {true, if the substring Si...Sj is a palindrome; false, otherwise}

A(i,j)=(A(i+1,j−1) and Si == Sj)

Base case: A(i, i) = true
            A(i, i+1) = (Si == Si+1)

'''

class LPS:
    def longest_palin_substring(self, s):
        str_len = len(s)
        table = [[False for _ in range(str_len)] for _ in range(str_len)]

        start = 0
        subs_len = 0
        # initialization for all the substrings with one char
        for i in range(str_len):
            table[i][i], subs_len = True, 1

        # intialization for all the substrings with length 2
        for i in range(str_len - 1):
            if s[i] == s[i + 1]:
                table[i][i+1], start, subs_len = True, i, 2


        # fill the table for all the substrings with length > 2
        n = 3 #start filling up with length 3
        for n in range(3, str_len+1):
            for i in range(str_len - n + 1):
                j =  i + n - 1
                if (table[i + 1][j - 1] and s[i] == s[j]):
                    table[i][j] = True
                    if n > subs_len:
                        start = i
                        subs_len = n
        return subs_len , s[start: start + subs_len]




def main():
    palindrome = LPS()
    print(palindrome.longest_palin_substring("a"))
    print(palindrome.longest_palin_substring("aaaa"))
    print(palindrome.longest_palin_substring("babad"))
    print(palindrome.longest_palin_substring("ccc"))
    print(palindrome.longest_palin_substring("abcba"))
    print(palindrome.longest_palin_substring("bbbab"))

if __name__ == "__main__":
    main()