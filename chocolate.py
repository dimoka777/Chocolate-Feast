"""  Hackerrank Chocolate Feast Easy Max Score 25
Function Description
Complete the chocolateFeast function in the editor below. It must return the number of chocolates Bobby can eat after taking full advantage of the promotion.
chocolateFeast has the following parameter(s):
n: an integer representing Bobby's initial amount of money
c: an integer representing the cost of a chocolate bar
m: an integer representing the number of wrappers he can turn in for a free bar
Note: Little Bobby will always turn in his wrappers if he has enough to get a free chocolate.
Input Format
The first line contains an integer, , denoting the number of test cases to analyze.
Each of the next  lines contains three space-separated integers: , , and . They represent money to spend, cost of
a chocolate, and the number of wrappers he can turn in for a free chocolate.
Constraints
"""
import os
# Complete the chocolateFeast function below.


def chocolateFeast(n, c, m):

    result = n // c

    def wrapp(wrappers):
        if wrappers < m:
            return 0
        elif wrappers >= m:
            res_wrap = wrappers // m
            return res_wrap + wrapp((wrappers % m) + res_wrap)

    total_wrapps = wrapp(result)
    result += total_wrapps
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)
        print(result)
    #     fptr.write(str(result) + '\n')
    #
    # fptr.close()
