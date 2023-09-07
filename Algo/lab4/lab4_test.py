from lab4 import numWays, minCoin
import os

def read_file(path:str) -> tuple:
    with open(path, "r") as openfile:
        amount = int(openfile.readline().strip())
        coins = [int(c) for c in openfile.readline().strip().split(" ")]
    return (amount, coins)

BASE_PATH = "Algo/lab4/lab 4 test case/"

# test_case = os.listdir(BASE_PATH)
# test_case.remove("4.14(Extra).txt")
# test_case.sort(key=lambda x : int(x.strip(".txt").replace(".", "")))
# for case in test_case:
#     amount, coins = read_file(BASE_PATH + case)
#     print(case)
#     numWays(amount, coins)

case = "4.13.txt"
inp = read_file(BASE_PATH + case)
print(case)
numWays(inp[0], inp[1])