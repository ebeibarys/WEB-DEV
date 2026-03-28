# Object-Oriented Programming in Python - Animal Hierarchy

This project demonstrates core OOP concepts in Python using an animal hierarchy.

## Features

- **Base Class (Animal)**: Contains common attributes and methods
- **Child Classes**: Dog, Cat, Bird with specialized behaviors
- **Inheritance**: Child classes inherit from Animal
- **Polymorphism**: Same method (speak()) behaves differently for each class
- **Method Overriding**: Child classes override parent methods
- **Encapsulation**: Attributes are managed through methods
- **Modular Design**: Code organized in separate modules

## Class Structure

### Animal (Base Class)
- Attributes: name, age, species, energy
- Methods: eat(), sleep(), speak(), __str__()

### Dog (Child Class)
- Additional Attributes: breed, is_trained
- Additional Methods: fetch(), train()
- Overridden Methods: speak(), __str__()

### Cat (Child Class)
- Additional Attributes: color, mice_caught
- Additional Methods: hunt(), climb_tree()
- Overridden Methods: speak(), __str__()

### Bird (Child Class)
- Additional Attributes: wing_span, can_fly
- Additional Methods: fly()
- Overridden Methods: speak(), __str__()

## How to Run

1. Ensure you have Python 3.8+ installed
2. Clone this repository
3. Navigate to the project directory
4. Run: `python main.py`

## Expected Output

The program will demonstrate:
- Creating objects of different classes
- Calling class-specific methods
- Polymorphism through the speak() method
- Iterating through collections of objects
- Method overriding and inheritance