import json
from typing import List, Optional
from datetime import datetime

class Person:
    """Base class representing a person"""
    
    def __init__(self, name: str, age: int, email: str):
        """
        Initialize a Person object
        
        Args:
            name: Person's name
            age: Person's age
            email: Person's email address
            
        Raises:
            ValueError: If age is negative or email is invalid
            TypeError: If name is not a string or age is not an integer
        """
        self._validate_inputs(name, age, email)
        
        self.name = name
        self.age = age
        self.email = email
        self.created_at = datetime.now()
    
    def _validate_inputs(self, name: str, age: int, email: str):
        """Validate person attributes"""
        # Type validation
        if not isinstance(name, str):
            raise TypeError(f"Name must be a string, got {type(name).__name__}")
        
        if not isinstance(age, int):
            raise TypeError(f"Age must be an integer, got {type(age).__name__}")
        
        if not isinstance(email, str):
            raise TypeError(f"Email must be a string, got {type(email).__name__}")
        
        # Value validation
        if age < 0:
            raise ValueError(f"Age cannot be negative, got {age}")
        
        if age > 150:
            raise ValueError(f"Age seems unrealistic, got {age}")
        
        if '@' not in email or '.' not in email:
            raise ValueError(f"Invalid email format: {email}")
    
    def display_info(self) -> str:
        """Return formatted person information"""
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"
    
    def to_dict(self) -> dict:
        """Convert person object to dictionary for JSON serialization"""
        return {
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'type': 'Person'
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create a Person object from dictionary data"""
        return cls(
            name=data['name'],
            age=data['age'],
            email=data['email']
        )


class Student(Person):
    """Student class inheriting from Person"""
    
    def __init__(self, name: str, age: int, email: str, student_id: str, major: str, gpa: float):
        """
        Initialize a Student object
        
        Args:
            student_id: Student's ID
            major: Student's major
            gpa: Student's GPA
            
        Raises:
            ValueError: If GPA is not between 0 and 4.0
        """
        super().__init__(name, age, email)
        
        # Additional validation
        if gpa < 0 or gpa > 4.0:
            raise ValueError(f"GPA must be between 0 and 4.0, got {gpa}")
        
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
        self.courses = []
    
    def display_info(self) -> str:
        """Override parent method to include student-specific information"""
        base_info = super().display_info()
        return f"{base_info}, Student ID: {self.student_id}, Major: {self.major}, GPA: {self.gpa}"
    
    def to_dict(self) -> dict:
        """Override to include student-specific attributes"""
        data = super().to_dict()
        data.update({
            'student_id': self.student_id,
            'major': self.major,
            'gpa': self.gpa,
            'type': 'Student'
        })
        return data
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create a Student object from dictionary data"""
        return cls(
            name=data['name'],
            age=data['age'],
            email=data['email'],
            student_id=data['student_id'],
            major=data['major'],
            gpa=data['gpa']
        )


class Teacher(Person):
    """Teacher class inheriting from Person"""
    
    def __init__(self, name: str, age: int, email: str, teacher_id: str, subject: str, salary: float):
        """
        Initialize a Teacher object
        
        Args:
            teacher_id: Teacher's ID
            subject: Subject taught
            salary: Teacher's salary
            
        Raises:
            ValueError: If salary is negative
        """
        super().__init__(name, age, email)
        
        # Additional validation
        if salary < 0:
            raise ValueError(f"Salary cannot be negative, got {salary}")
        
        self.teacher_id = teacher_id
        self.subject = subject
        self.salary = salary
        self.classes = []
    
    def display_info(self) -> str:
        """Override parent method to include teacher-specific information"""
        base_info = super().display_info()
        return f"{base_info}, Teacher ID: {self.teacher_id}, Subject: {self.subject}, Salary: ${self.salary:,.2f}"
    
    def to_dict(self) -> dict:
        """Override to include teacher-specific attributes"""
        data = super().to_dict()
        data.update({
            'teacher_id': self.teacher_id,
            'subject': self.subject,
            'salary': self.salary,
            'type': 'Teacher'
        })
        return data
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create a Teacher object from dictionary data"""
        return cls(
            name=data['name'],
            age=data['age'],
            email=data['email'],
            teacher_id=data['teacher_id'],
            subject=data['subject'],
            salary=data['salary']
        )


class DataManager:
    """Handles data persistence and file operations"""
    
    def __init__(self, filename: str = "data.json"):
        self.filename = filename
        self.class_map = {
            'Person': Person,
            'Student': Student,
            'Teacher': Teacher
        }
    
    def save_data(self, objects: List[Person]) -> bool:
        """
        Save list of objects to JSON file
        
        Args:
            objects: List of Person objects (including Student and Teacher)
            
        Returns:
            bool: True if save successful, False otherwise
        """
        try:
            # Using list comprehension to convert objects to dictionaries
            data_to_save = [obj.to_dict() for obj in objects]
            
            # Save to file
            with open(self.filename, 'w') as file:
                json.dump(data_to_save, file, indent=4)
            
            print(f"✓ Successfully saved {len(objects)} objects to {self.filename}")
            return True
            
        except TypeError as e:
            print(f"✗ Error: Object not JSON serializable - {e}")
            return False
            
        except PermissionError as e:
            print(f"✗ Error: Permission denied to write file - {e}")
            return False
            
        except Exception as e:
            print(f"✗ Unexpected error while saving: {e}")
            return False
    
    def load_data(self) -> List[Person]:
        """
        Load objects from JSON file
        
        Returns:
            List[Person]: List of recreated objects
        """
        objects = []
        
        try:
            # Read from file
            with open(self.filename, 'r') as file:
                data = json.load(file)
            
            # Validate data structure
            if not isinstance(data, list):
                raise ValueError("Invalid data format: Expected a list of objects")
            
            # Recreate objects from dictionaries using list comprehension
            for item_data in data:
                try:
                    obj_type = item_data.get('type', 'Person')
                    obj_class = self.class_map.get(obj_type, Person)
                    
                    obj = obj_class.from_dict(item_data)
                    objects.append(obj)
                    
                except (KeyError, ValueError, TypeError) as e:
                    print(f"⚠ Warning: Skipping invalid object - {e}")
                    continue
            
            # Using list comprehension to count by type
            type_counts = {obj_type: len([obj for obj in objects if obj.__class__.__name__ == obj_type]) 
                          for obj_type in ['Person', 'Student', 'Teacher']}
            
            print(f"✓ Successfully loaded {len(objects)} objects from {self.filename}")
            print(f"  - Persons: {type_counts['Person']}, Students: {type_counts['Student']}, Teachers: {type_counts['Teacher']}")
            
            return objects
            
        except FileNotFoundError:
            print(f"⚠ Warning: File {self.filename} not found. Starting with empty list.")
            return []
            
        except json.JSONDecodeError as e:
            print(f"✗ Error: Invalid JSON format in {self.filename} - {e}")
            return []
            
        except PermissionError as e:
            print(f"✗ Error: Permission denied to read file - {e}")
            return []
            
        except Exception as e:
            print(f"✗ Unexpected error while loading: {e}")
            return []
    
    def filter_by_type(self, objects: List[Person], obj_type: str) -> List[Person]:
        """
        Filter objects by type using list comprehension
        
        Args:
            objects: List of Person objects
            obj_type: Type to filter by ('Person', 'Student', 'Teacher')
            
        Returns:
            List[Person]: Filtered list of objects
        """
        return [obj for obj in objects if obj.__class__.__name__ == obj_type]
    
    def get_average_age(self, objects: List[Person]) -> float:
        """
        Calculate average age using list comprehension
        
        Args:
            objects: List of Person objects
            
        Returns:
            float: Average age
        """
        if not objects:
            return 0.0
        
        ages = [obj.age for obj in objects]
        return sum(ages) / len(ages)
    
    def display_all_objects(self, objects: List[Person]):
        """Display all objects with their information"""
        if not objects:
            print("No objects to display.")
            return
        
        print("\n" + "="*50)
        print("ALL OBJECTS")
        print("="*50)
        
        # Using enumerate with list comprehension for formatted output
        for i, obj in enumerate(objects, 1):
            print(f"{i}. {obj.display_info()}")
        
        print("="*50)
        print(f"Total: {len(objects)} objects")
        print(f"Average age: {self.get_average_age(objects):.1f} years")