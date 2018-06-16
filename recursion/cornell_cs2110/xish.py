def xish(first, second):
    if len(first) == 0:
        return True
    return (first[0] in second) and xish(first[1:], second)

def xish_iter(first, second):
    result = True
    for x in first:
        result &= (x in second)
    return result

print(xish("Hello", "Helo"))
print(xish("Hello", "Heo"))

print(xish_iter("Hello", "Helo"))
print(xish_iter("Hello", "Heo"))