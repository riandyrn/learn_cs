'''
The basic idea to solve this problem is by realizing that we need
to find scenarios for each player when they always try their best not
all possibility of scenario.

Trying the best means every moves done by player will always resulted
in winning the playes, unless the condition is impossible for player to win.
It is much easier to understand this problem by writing it on paper.
'''

def pickcoin(n, first, second):
    if n == 1:
        return (first, 1)
    if n == 2:
        return (first, 1)
    if n == 3:
        return (second, 2)
    if n == 4:
        return (first, 3)
    # first player try to take coins, sum the resulted possibilities
    tmp = {first: 0, second: 0}
    for x in [1, 2, 4]:
        if n > x:
            res = pickcoin(n-x, second, first)
            tmp[res[0]] += res[1]
    # each player will always try the best, which means first 
    # player will also always try to win
    if tmp[first] > 0:
        return (first, tmp[first])
    else:
        return (second, tmp[second])

def pickcoin_iter(n, first, second):
    # define first player result memo
    memo = {1: (first, 1), 
            2: (first, 1), 
            3: (second, 2), 
            4: (first, 3)}
    # start the process
    for i in range(5, n+1):
        tmp = {first: 0, second: 0}
        # first player try to take coins
        for x in [1, 2, 4]:
            # fetch second player result
            res = memo[i - x]
            # invert result from memo: first -> second, second -> first
            if res[0] == first:
                res = (second, res[1])
            else:
                res = (first, res[1])
            # sum resulted possibilities
            tmp[res[0]] += res[1]
        # each player will always try the best, which means first 
        # player will also always try to win
        if tmp[first] > 0:
            memo[i] = (first, tmp[first])
        else:
            memo[i] = (second, tmp[second])
    # return main result
    return memo[n]

#start the game
for i in range(1, 31):
    first, second = "alice", "bob"
    res = pickcoin(i, first, second)
    res_iter = pickcoin_iter(i, first, second)
    if res != res_iter:
        exit()
    print(f"i: {i}, first: {first}, second: {second}, result: {res[0]} {res[1]}")