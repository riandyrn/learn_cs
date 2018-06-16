def reverse(str):
    if len(str) == 0:
        return ""
    tokens = str.split(" ")
    return (tokens[-1] + " " + reverse(" ".join(tokens[:-1]))).strip("")

def reverse_iter(str):
    result = ""
    tokens = str.split(" ")
    for i in range(len(tokens)-1, -1, -1):
        result += " " + tokens[i]
    return result.strip()

print(reverse("Hello World! Riandy!"))
print(reverse_iter("Hello World! Riandy!"))