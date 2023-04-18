class Zoo:

    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"{species.title() + 's'} in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"{species.title() + 'es'} in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"{species.title() + 's'} in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result

zoo_name = input()
zoo = Zoo(zoo_name)
count_command = int(input())

for count in range(count_command):
    animal, the_name = input().split()
    zoo.add_animals(animal, the_name)

info = input()
print(zoo.get_info(info))
