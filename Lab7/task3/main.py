from models import Person, Student, Teacher, DataManager
import sys

def create_sample_data():
    """Create sample objects for testing"""
    objects = []
    
    try:
        # Create some students
        objects.append(Student("Alice Johnson", 20, "alice@email.com", "S001", "Computer Science", 3.8))
        objects.append(Student("Bob Smith", 22, "bob@email.com", "S002", "Mathematics", 3.5))
        objects.append(Student("Carol White", 21, "carol@email.com", "S003", "Physics", 3.9))
        
        # Create some teachers
        objects.append(Teacher("Dr. David Brown", 45, "dbrown@email.com", "T001", "Computer Science", 85000))
        objects.append(Teacher("Prof. Emily Davis", 52, "edavis@email.com", "T002", "Mathematics", 92000))
        
        # Create a regular person
        objects.append(Person("Frank Miller", 35, "frank@email.com"))
        
    except (ValueError, TypeError) as e:
        print(f"Error creating sample data: {e}")
        return []
    
    return objects

def demonstrate_list_comprehensions(data_manager, objects):
    """Demonstrate various list comprehension use cases"""
    print("\n" + "="*50)
    print("LIST COMPREHENSION DEMONSTRATIONS")
    print("="*50)
    
    # Filter by type
    students = data_manager.filter_by_type(objects, 'Student')
    teachers = data_manager.filter_by_type(objects, 'Teacher')
    
    print(f"\nStudents ({len(students)}):")
    [print(f"  - {s.name} ({s.major})") for s in students]
    
    print(f"\nTeachers ({len(teachers)}):")
    [print(f"  - {t.name} ({t.subject})") for t in teachers]
    
    # Extract specific attributes
    names = [obj.name for obj in objects]
    print(f"\nAll names: {', '.join(names)}")
    
    # Filter by condition
    young_people = [obj for obj in objects if obj.age < 30]
    print(f"Young people (under 30): {len(young_people)}")
    
    # Transform data
    email_domains = [obj.email.split('@')[1] for obj in objects]
    print(f"Email domains: {set(email_domains)}")
    
    # Dictionary comprehension for summary
    type_summary = {obj.__class__.__name__: len([o for o in objects if o.__class__.__name__ == obj.__class__.__name__]) 
                   for obj in set(objects)}
    print(f"Type summary: {type_summary}")

def main():
    """Main program entry point"""
    print("DATA PERSISTENCE AND ERROR HANDLING DEMO")
    print("="*50)
    
    # Initialize data manager
    data_manager = DataManager("school_data.json")
    objects = []
    
    while True:
        print("\n" + "="*50)
        print("MAIN MENU")
        print("="*50)
        print("1. Create sample data")
        print("2. Save data to file")
        print("3. Load data from file")
        print("4. Display all objects")
        print("5. Demonstrate list comprehensions")
        print("6. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            objects = create_sample_data()
            if objects:
                print(f"\n✓ Created {len(objects)} sample objects")
                data_manager.display_all_objects(objects)
        
        elif choice == '2':
            if objects:
                success = data_manager.save_data(objects)
                if success:
                    print("Data saved successfully!")
            else:
                print("No data to save. Please create or load data first.")
        
        elif choice == '3':
            objects = data_manager.load_data()
            if objects:
                print("Data loaded successfully!")
        
        elif choice == '4':
            if objects:
                data_manager.display_all_objects(objects)
            else:
                print("No objects to display. Please create or load data first.")
        
        elif choice == '5':
            if objects:
                demonstrate_list_comprehensions(data_manager, objects)
            else:
                print("No objects to analyze. Please create or load data first.")
        
        elif choice == '6':
            # Ask if user wants to save before exiting
            if objects:
                save_before_exit = input("Save data before exiting? (y/n): ").lower()
                if save_before_exit == 'y':
                    data_manager.save_data(objects)
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error in main program: {e}")
        sys.exit(1)