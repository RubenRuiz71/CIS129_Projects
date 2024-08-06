
# Define the Pet class
class Pet:
    def __init__(self, name='', pet_type='', age=0):
        """Initialize a Pet object with optional values."""
        self.name = name
        self.pet_type = pet_type
        self.age = age

    # Mutators
    def set_name(self, name):
        """Set the name of the pet."""
        self.name = name

    def set_type(self, pet_type):
        """Set the type of the pet."""
        self.pet_type = pet_type

    def set_age(self, age):
        """Set the age of the pet."""
        self.age = age

    # Accessors
    def get_name(self):
        """Get the name of the pet."""
        return self.name

    def get_type(self):
        """Get the type of the pet."""
        return self.pet_type

    def get_age(self):
        """Get the age of the pet."""
        return self.age

# Main function
def main():
    # Create a Pet object
    animal = Pet()

    # Get values for a pet
    input_name = input("Enter a pet name: ")
    animal.set_name(input_name)

    input_type = input("Enter a pet type: ")
    animal.set_type(input_type)

    input_age = int(input("Enter a pet age: "))
    animal.set_age(input_age)

    # Show values for this pet
    print(f"The pet name is {animal.get_name()}.")
    print(f"The pet type is {animal.get_type()}.")
    print(f"The pet age is {animal.get_age()}.")

# Ensure the main function is called when the script is executed
if __name__ == "__main__":
    main()
