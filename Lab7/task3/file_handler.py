import json
from models import create_animal_from_dict

class FileHandler:
    @staticmethod
    def save_to_file(animals, filename="data.json"):
        try:
            animal_dicts = [animal.to_dict() for animal in animals]
            
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(animal_dicts, file, indent=4, ensure_ascii=False)
            
            print(f"Successfully saved {len(animals)} animals to {filename}")
            return True
            
        except TypeError as e:
            print(f"Error: Invalid data type while saving to file - {e}")
            return False
        except PermissionError as e:
            print(f"Error: Permission denied when trying to write to {filename}")
            return False
        except Exception as e:
            print(f"Unexpected error while saving file: {e}")
            return False
        finally:
            print("Save operation completed")
    
    @staticmethod
    def load_from_file(filename="data.json"):
        animals = []
        
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                animal_dicts = json.load(file)
            
            animal_objects = [create_animal_from_dict(data) for data in animal_dicts]
            
            print(f"Successfully loaded {len(animal_objects)} animals from {filename}")
            return animal_objects
            
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Starting with empty list.")
            return []
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format in {filename} - {e}")
            return []
        except KeyError as e:
            print(f"Error: Missing required key in data - {e}")
            return []
        except Exception as e:
            print(f"Unexpected error while loading file: {e}")
            return []
        finally:
            print("Load operation completed")