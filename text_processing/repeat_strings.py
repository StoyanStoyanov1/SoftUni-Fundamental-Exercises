text = input().split()
result = [word * len(word) for word in text ]
print(*result, sep="")