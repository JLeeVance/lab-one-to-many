class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("The type must be in the list")
        self.owner = owner

        Pet.all.append(self)

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, new_name):
        if not hasattr(self, "name"):
            self._name = new_name
        else:
            raise Exception("You shouldn't rename your Pet!")
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, new_owner):
        if isinstance(new_owner, Owner):
            self._owner = new_owner
            new_owner._pets.append(self)
            print(f"{self.name} found a home!")
        else:
            print(f"{self.name} is available for adoption.")


class Owner:

    def __init__(self, name):
        self.name = name
        print(f"{name} has been created, welcome.")
        self._pets = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) != str or hasattr(self, "name"):
            raise Exception("Your name can not be reset")
        else:
            self._name = new_name
        
    def pets(self):
        pet_lists = [pet for pet in self._pets]
        return pet_lists

    def add_pet(self, new_pet):
        if isinstance(new_pet, Pet):
            new_pet._owner = self
            self._pets.append(new_pet)
            print(f"{self.name} now owns {self._pets[-1].name}")
        else:
            raise Exception("If you would like to be able to add a pet, you will need an instance of a Pet.")
    
    def get_sorted_pets(self):
        sorted_pets = sorted(self._pets, key=lambda pet: pet.name)
        return sorted_pets





'''PLAY GROUND'''


# frank = Owner("Frank")
# jackie = Owner("Jackie")

# print("\n" * 1)

# jackson = Pet("Jackson", "dog")
# bennet = Pet("Bennet", "cat")

# print("\n" * 1)

# '''testing add_pet'''

# frank.add_pet(jackson)
# frank.add_pet(bennet)

# franks_pets = frank.get_sorted_pets()
# for pet in franks_pets:
#     print(pet.name)


