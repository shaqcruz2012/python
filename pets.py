# For this project, you will import the **json** module.

# Write a class named NeighborhoodPets that has methods for adding a pet, deleting a pet, searching for the owner of a pet, saving data to a JSON file, loading data from a JSON file, and getting a set of all pet species. It will only be loading JSON files that it has previously created, so the internal organization of the data is up to you.

# * The init method takes no parameters and initializes all the data members, which must all be **private**.
# * The add_pet method takes as parameters the name of the pet, the species of the pet, and the name of the pet's owner. If a pet has the same name as a pet that has already been added, then the function should raise a **DuplicateNameError** (you'll need to define this exception class).
# * The delete_pet method takes as a parameter the name of the pet and deletes that pet.
# * The get_owner method takes as a parameter the name of the pet and returns the name of its owner.
# * The save_as_json method takes as a parameter the name of the file and saves it in JSON format with that name. You can assume the extension (if any) will be part of the provided name. You can organize your JSON file however you want.
# * The read_json method takes as a parameter the name of the file to read and loads that file. This will replace all of the pets currently in memory.
# * The get_all_species method takes no parameters and returns a Python ***set*** of the species of all pets. Research what a set is, we haven't covered it in class.

# For example, your class could be used like this:

# np = NeighborhoodPets()
# try:
#     np.add_pet("Fluffy", "gila monster", "Oksana")
#     np.add_pet("Tiny", "stegasaurus", "Rachel")
#     np.add_pet("Spot", "zebra", "Farrokh")
# except DuplicateNameError:
#     print('You tried to enter a pet with the same name as another pet.')
# np.save_as_json("pets.json")
# np.delete_pet("Tiny")
# spot_owner = np.get_owner("Spot")
# np.read_json("other_pets.json")  # where other_pets.json is a file it saved in some previous session
# species_set = np.get_all_species()

# If you implement a Pet class (which is a natural option, but not required), then when you save it, you'll need to translate the information into one of the built-in object types the json module recognizes, and translate it back the other way when you read it.

import json

class DuplicateNameError(Exception):
    pass

class NeighborhoodPets:
    def __init__(self):
        self.__pets = {}

    def add_pet(self, name, species, owner):
        if name in self.__pets:
            raise DuplicateNameError("Pet with this name already exists.")
        self.__pets[name] = {"species": species, "owner": owner}

    def delete_pet(self, name):
        if name in self.__pets:
            del self.__pets[name]

    def get_owner(self, name):
        if name in self.__pets:
            return self.__pets[name]["owner"]

    def save_as_json(self, file_name):
        with open(file_name, "w") as f:
            json.dump(self.__pets, f)

    def read_json(self, file_name):
        with open(file_name, "r") as f:
            self.__pets = json.load(f)

    def get_all_species(self):
        return set(pet["species"] for pet in self.__pets.values())

# This class uses a dictionary to store the pets and their information. 
# The keys of the dictionary are the names of the pets, and the values are dictionaries that store the species and owner of the pet. 
# The add_pet method checks if a pet with the same name already exists before adding it to the dictionary. 
# The delete_pet method removes a pet from the dictionary. 
# The get_owner method returns the owner of a pet. 
# The save_as_json method uses the json module to save the dictionary of pets to a file with the given name. 
# The read_json method reads a json file and replaces the pets in memory with the pets from the file. 
# The get_all_species method uses a set comprehension to create a set of all the species of the pets in the dictionary.



