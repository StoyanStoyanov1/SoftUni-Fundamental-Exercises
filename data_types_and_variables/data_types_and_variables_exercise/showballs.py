number_snowballs = int(input())
max_snowball_value = 0

c_snowball_snow = 0
c_snowball_time = 0
c_snowball_quality = 0

for i in range(1, number_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow / snowball_time) ** snowball_quality

    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        c_snowball_snow = snowball_snow
        c_snowball_time = snowball_time
        c_snowball_quality = snowball_quality

print(f'{c_snowball_snow} : {c_snowball_time} = {max_snowball_value:.0f} ({c_snowball_quality})')