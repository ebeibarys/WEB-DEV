class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        self.energy = 100
    
    def eat(self, food_amount):
        self.energy += food_amount
        print(f"{self.name} eats and gains {food_amount} energy. Energy: {self.energy}")
    
    def sleep(self, hours):
        energy_gain = hours * 10
        self.energy += energy_gain
        print(f"{self.name} sleeps for {hours} hours and gains {energy_gain} energy. Energy: {self.energy}")
    
    def speak(self):
        return "Some generic animal sound"
    
    def __str__(self):
        return f"{self.name} ({self.species}), {self.age} years old, Energy: {self.energy}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Canis familiaris")
        self.breed = breed
        self.is_trained = False
    
    def speak(self):
        return f"Woof! Woof! (I'm a {self.breed})"
    
    def fetch(self, item):
        if self.energy >= 20:
            self.energy -= 20
            print(f"{self.name} fetches the {item}! Energy remaining: {self.energy}")
        else:
            print(f"{self.name} is too tired to fetch. Energy: {self.energy}")
    
    def train(self):
        self.is_trained = True
        print(f"{self.name} has been trained!")
    
    def __str__(self):
        training_status = "trained" if self.is_trained else "not trained"
        return f"{super().__str__()}, Breed: {self.breed}, {training_status}"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Felis catus")
        self.color = color
        self.mice_caught = 0
    
    def speak(self):
        return "Meow! Meow!"
    
    def hunt(self):
        if self.energy >= 30:
            self.energy -= 30
            self.mice_caught += 1
            print(f"{self.name} caught a mouse! Total mice: {self.mice_caught}. Energy: {self.energy}")
        else:
            print(f"{self.name} is too tired to hunt. Energy: {self.energy}")
    
    def climb_tree(self):
        if self.energy >= 15:
            self.energy -= 15
            print(f"{self.name} climbs the tree! Energy remaining: {self.energy}")
        else:
            print(f"{self.name} is too tired to climb. Energy: {self.energy}")
    
    def __str__(self):
        return f"{super().__str__()}, Color: {self.color}, Mice caught: {self.mice_caught}"


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age, "Aves")
        self.wing_span = wing_span
        self.can_fly = True
    
    def speak(self):
        return "Chirp! Chirp!"
    
    def fly(self):
        if self.can_fly and self.energy >= 25:
            self.energy -= 25
            print(f"{self.name} is flying with its {self.wing_span}cm wings! Energy: {self.energy}")
        elif not self.can_fly:
            print(f"{self.name} cannot fly!")
        else:
            print(f"{self.name} is too tired to fly. Energy: {self.energy}")
    
    def __str__(self):
        return f"{super().__str__()}, Wing span: {self.wing_span}cm"