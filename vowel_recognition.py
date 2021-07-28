'''
Problem
{a,e,i,o,u,A,E,I,O,U}

Natural Language Understanding is the subdomain of Natural Language Processing where people used to design AI based
applications have ability to understand the human languages. HashInclude Speech Processing team has a project
named Virtual Assistant.
For this project they appointed you as a data engineer (who has good knowledge of creating clean datasets by
writing efficient code).
As a data engineer your first task is to make vowel recognition dataset. In this task you have to find the presence of
vowels in all possible substrings of the given string. For each given string you have to print the total number of
vowels.

Sample Input
1
baceb

Sample Output
16


First line is number of input string, In given example, string is "baceb" so the substrings will be like
-"b, ba, bac, bace, a, ac, ace, aceb, c, ce, ceb, e, eb, baceb" now the number of vowels in each substring will be
0, 1, 1, 2, 1, 1, 2, 2, 0, 1, 1, 1, 1, 2  and the total number will be sum of all presence which is 16.

'''



n = int(input())

for i in range(n):
    str = input()
    sum = 0
    substr_count_end = []
    substr_count_start = []
    substr_count_start.append(0)
    substr_count_end.append(0)
    vowel_pos = []
    for j in range(1, len(str)+1):
        substr_count_end.append(substr_count_end[j-1] + len(str) - j + 1)
        substr_count_start.append(substr_count_start[j-1] + j)
        if str[j-1] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vowel_pos.append(j)
    sum = 0
    for j in vowel_pos:
        sum = sum + len(str) - j + 1 + substr_count_end[j-1] - substr_count_start[j-1]
    print(sum)
