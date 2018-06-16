def elfish(str, search="elf"):
    if len(search) == 0:
        return True
    return (search[0] in str) and elfish(str, search[1:])

def elfish_iter(str, search="elf"):
    result = True
    for x in search:
        result &= (x in str)
    return result

print(f"elfish('Hello!'): {elfish('Hello!')}, elfish_iter('Hello!'): {elfish_iter('Hello!')}")
print(f"elfish('Hellof!'): {elfish('Hellof!')}, elfish_iter('Hellof!'): {elfish_iter('Hellof!')}")
