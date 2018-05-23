'''
Coin Change Problem

Dynamic Programming: Overlapping sub-problems

Problem Summary:
You are working at the cash counter at a fun-fair, and you have different types of coins available to you in infinite quantities. The value of each coin is already given. Can you determine the number of ways of making change for a particular number of units using the given types of coins?
For example, if you have  types of coins, and the value of each type is given as  respectively, you can make change for  units in three ways:  , , and .
'''
class CoinChange:
    def countDP(self, change_of: int, type_of_coins: list, no_of_coin_types: int):

        #Initialize overlapping sub-problems table with bottom-up calculation
        #The final value would be at position (change_of + 1) beginning at change_of = 0
        value_table = [[0 for val in range(no_of_coin_types)] for val in range(change_of + 1)]

        #   Base case: change of nothing
        #   change_of = 0
        for idx in range(no_of_coin_types):
            value_table[0][idx] = 1

        #   Base case: change of something but with nothing
        #   no_of_coin_types == 0 and change_of >= 1:
        for idx in range(change_of + 1):
            value_table[idx][0] = 0

        for i in range (1, change_of+1):
            for j in range(no_of_coin_types):
                # Case when a coin type is used
                # check for case when the index of table goes < 0
                coin_used_count = value_table[i - type_of_coins[j]][j] if i - type_of_coins[j] >= 0 else 0

                # Case when a coin type is not used
                # check for case when the index of table goes < 0
                coin_not_used_count = value_table[i][j-1] if j-1 >= 0 else 0

                # count of all the possible combinations
                value_table[i][j] = coin_used_count + coin_not_used_count


        return value_table[change_of][no_of_coin_types-1]


def main():
    coin_change = CoinChange()
    print(coin_change.countDP(3, [8, 3, 1, 2], 4))

if __name__ == "__main__":
    main()