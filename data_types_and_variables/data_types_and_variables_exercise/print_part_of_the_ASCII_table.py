start = int(input())
end = int(input())

symbols = []

for symbol in range(start, end + 1):

    symbols.append(chr(symbol))

print(*symbols, sep = ' ')