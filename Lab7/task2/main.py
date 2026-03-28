from Lab7.task2.models import Animal, Dog, Cat, Bird

def demonstrate_polymorphism(animals):
    print("\n" + "="*50)
    print("POLYMORPHISM DEMONSTRATION")
    print("="*50)
    
    for animal in animals:
        print(f"{animal.name} says: {animal.speak()}")


def main():
    print("="*50)
    print("OBJECT-ORIENTED PROGRAMMING DEMONSTRATION")
    print("="*50)
    
    print("\n1. CREATING ANIMAL INSTANCES")
    print("-"*30)
    
    generic_animal = Animal("Generic", 5, "Unknown")
    buddy = Dog("Buddy", 3, "Golden Retriever")
    whiskers = Cat("Whiskers", 2, "Orange")
    tweety = Bird("Tweety", 1, 25.5)
    
    animals = [generic_animal, buddy, whiskers, tweety]
    
    for animal in animals:
        print(animal)
    
    print("\n2. DEMONSTRATING OBJECT-SPECIFIC METHODS")
    print("-"*30)
    
    print(f"\n{buddy.name}'s actions:")
    buddy.fetch("ball")
    buddy.train()
    buddy.eat(30)
    
    print(f"\n{whiskers.name}'s actions:")
    whiskers.hunt()
    whiskers.climb_tree()
    whiskers.sleep(2)
    
    print(f"\n{tweety.name}'s actions:")
    tweety.fly()
    tweety.sleep(1)
    tweety.fly()
    
    demonstrate_polymorphism(animals)
    
    print("\n3. ITERATING THROUGH ANIMALS LIST")
    print("-"*30)
    
    for i, animal in enumerate(animals, 1):
        print(f"\nAnimal {i}:")
        print(animal)
        animal.eat(20)
        print(f"After eating: {animal}")
    
    print("\n4. INHERITANCE AND METHOD OVERRIDING SUMMARY")
    print("-"*30)
    
    print(f"Generic animal sound: {generic_animal.speak()}")
    print(f"Dog sound (overridden): {buddy.speak()}")
    print(f"Cat sound (overridden): {whiskers.speak()}")
    print(f"Bird sound (overridden): {tweety.speak()}")
    
    print("\n5. FINAL STATE OF ALL ANIMALS")
    print("-"*30)
    for animal in animals:
        print(animal)


if __name__ == "__main__":
    main()