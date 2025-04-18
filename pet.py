class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} is eating...")

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} is sleeping...")

    def play(self):
        if self.energy > 0:
            self.energy = max(self.energy - 3, 0)
            self.happiness = min(self.happiness + 2, 10)
            print(f"{self.name} is playing...")
        else:
            print(f"{self.name} is too tired to play")

    def train(self, trick):
        if self.energy > 0:
            self.energy = max(self.energy - 2, 0)
            self.happiness = min(self.happiness + 1, 10)
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}")
        else:
            print(f"{self.name} is too tired to train")

    def show_tricks(self):
        return(f"Tricks: [{', '.join(self.tricks)}]")

    def get_status(self):
        # print(f"{self.name}'s current status:")
        # print(f"Hunger: {self.hunger}")
        # print(f"Energy: {self.energy}")
        # print(f"Happiness: {self.happiness}")
        # print(self.show_tricks())

        print(f"{self.name}'s current status:\n Hunger: {self.hunger}\n Energy: {self.energy}\n Happiness: {self.happiness}\n {self.show_tricks()}")
        