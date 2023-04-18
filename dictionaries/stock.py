elements = input().split()
products = {}

for index in range(0, len(elements), 2):
    key = elements[index]
    value = elements[index + 1]
    products[key] = value

elements_to_search = input().split()

for the_product in elements_to_search:
    if the_product in products:
        print(f"We have {products[the_product]} of {the_product} left")
    else:
        print(f"Sorry, we don't have {the_product}")
