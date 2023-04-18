country = input().split(", ")
city = input().split(", ")

result = dict(zip(country, city))

for country, city in result.items():
    print(f"{country} -> {city}")