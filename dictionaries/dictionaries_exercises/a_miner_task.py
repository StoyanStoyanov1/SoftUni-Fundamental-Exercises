current_resource = input()
all_resource = {}

while current_resource != "stop":
    value = int(input())
    if current_resource not in all_resource:
        all_resource[current_resource] = 0
    all_resource[current_resource] += value

    current_resource = input()

for resource, quantity in all_resource.items():
    print(f"{resource} -> {quantity}")