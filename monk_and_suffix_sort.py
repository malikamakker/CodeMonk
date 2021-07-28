'''
Monk loves to play games. On his birthday, his friend gifted him a string S.
Monk and his friend started playing a new game called as Suffix Game.
In Suffix Game, Monk's friend will ask him lexicographically kth smallest
suffix of the string S. Monk wants to eat the cake first so he asked you to play the game.

Sample Input
aacb 3

Sample Output
b

All the suffices of the string are:
aacb
acb
cb
b

After sorting the order of the suffices will be:
aacb
acb
b
cb

3rd smallest suffix will be b.
'''


string, k = input().split(' ')
k = int(k)
n = len(string)

strings = []
for i in range(len(string)):
    strings.append(string[i:])
strings = sorted(strings)
print(strings[k-1])
