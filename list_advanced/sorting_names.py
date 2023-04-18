def sorting_name(names):
    sorted_names = sorted(names, key=lambda name: (-len(name), name))
    return sorted_names

the_names = input().split(", ")
print(sorting_name(the_names))