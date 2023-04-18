tail, body, head = input(), input(), input()

result = [tail, body, head]
result[0], result[2] = result[2], result[0]

print(result)
