'''
The idea to find gcd is by using euclid algorithm:
gcd(a, b) = gcd(b, a mod b), where (a > b) 
          = gcd(a, b mod a), where (b > a) 
          = a, where (a == b)

The idea behind euclid algorithm is tile breaking, for details
check following video:
https://www.youtube.com/watch?v=NdqwT9kfquY&t=322s
'''

def gcd(a, b):
    if a == b or b == 0:
        return a
    if a > b:
        return gcd(b, a % b)
    if a < b:
        return gcd(a, b % a)

def gcd_iter(a, b):
    if a < b:
        b, a = a, b
    while a % b != 0:
        a, b = b, a % b
    return b

if __name__ == "__main__":
    tests = [
        {"a": 48, "b": 18, "ans": 6},
        {"a": 18, "b": 48, "ans": 6},
        {"a": 6, "b": 6, "ans": 6},
    ]
    for test in tests:
        a, b, ans = test["a"], test["b"], test["ans"]
        got = gcd(a, b)
        if got != ans:
            print(f"unexpected answer for gcd({a}, {b}), got: {got}, expected: {ans}")
            exit()
        got = gcd_iter(a, b)
        if got != ans:
            print(f"unexpected answer for gcd({a}, {b}), got: {got}, expected: {ans}")
            exit()
    print("test succeed")