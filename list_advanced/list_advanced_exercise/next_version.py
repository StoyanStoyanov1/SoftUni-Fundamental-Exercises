digits = input().split(".")
result = int(digits[0] + digits[1] + digits[2]) + 1
print(".".join(str(result)))