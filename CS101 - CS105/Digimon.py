class Digimon:
    # To create a Digimon, give it a name, type, and level. Its max health is determined by its level. Its starting health is its max health and it is not knocked out when it starts.
    def __init__(self, name, type, level = 5):
        self.name = name
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.type = type
        self.is_knocked_out = False


    def __repr__(self):
        # Printing a Digimon will tell you its name, its type, its level and how much health it has remaining
        return "This level {level} {name} has {health} hit points remaining. They are a {type} type Digimon".format(level = self.level, name = self.name, health=self.health, type = self.type)

    def revive(self):
        # Reviving a Digimon will flip it's status to False
        self.is_knocked_out = False
        # A revived Digimon can't have 0 health. This is a safety precaution. revive() should only be called if the Digimon was given some health, but if it somehow has no health, its health gets set to 1.
        if self.health == 0:
            self.health = 1
        print("{name} was revived!".format(name = self.name))

    def knock_out(self):
        # Knocking out a Digimon will flip its status to True.
        self.is_knocked_out = True
        # A knocked out Digimon can't have any health. This is a safety precaution. knock_out() should only be called if heath was set to 0, but if somehow the Digimon had health left, it gets set to 0.
        if self.health != 0:
            self.health = 0
        print("{name} was knocked out!".format(name = self.name))

    def lose_health(self, amount):
        # Deducts heath from a Digimon and prints the current health reamining
        self.health -= amount
        if self.health <= 0:
            #Makes sure the health doesn't become negative. Knocks out the Digimon.
            self.health = 0
            self.knock_out()
        else:
            print("{name} now has {health} health.".format(name = self.name, health = self.health))

    def gain_health(self, amount):
        # Adds to a Digimon's heath
        # If a Digimon goes from 0 heath, then revive it
        if self.health == 0:
            self.revive()
        self.health += amount
        # Makes sure the heath does not go over the max health
        if self.health >= self.max_health:
            self.health = self.max_health
        print("{name} now has {health} health.".format(name = self.name, health = self.health))

    def attack(self, other_Digimon):
        # Checks to make sure the Digimon isn't knocked out
        if self.is_knocked_out:
            print("{name} can't attack because it is knocked out!".format(name = self.name))
            return
        # If the Digimon attacking has a disadvantage, then it deals damage equal to half its level to the other Digimon
        if (self.type == "Fire" and other_Digimon.type == "Water") or (self.type == "Water" and other_Digimon.type == "Grass") or (self.type == "Grass" and other_Digimon.type == "Fire"):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_Digimon.name, damage = round(self.level * 0.5)))
            print("It's not very effective")
            other_Digimon.lose_health(round(self.level * 0.5))
        # If the Digimon attacking has neither advantage or disadvantage, then it deals damage equal to its level to the other Digimon
        if (self.type == other_Digimon.type):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_Digimon.name, damage = self.level))
            other_Digimon.lose_health(self.level)
        # If the Digimon attacking has advantage, then it deals damage equal to double its level to the other Digimon
        if (self.type == "Fire" and other_Digimon.type == "Grass") or (self.type == "Water" and other_Digimon.type == "Fire") or (self.type == "Grass" and other_Digimon.type == "Water"):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_Digimon.name, damage = self.level * 2))
            print("It's super effective")
            other_Digimon.lose_health(self.level * 2)

class Trainer:
    # A trainer has a list of Digimon, a number of potions and a name. When the trainer gets created, the first Digimon in their list of Digimons is the active Digimon (number 0)
    def __init__(self, Digimon_list, num_potions, name):
        self.Digimons = Digimon_list
        self.potions = num_potions
        self.current_Digimon = 0
        self.name = name

    def __repr__(self):
        # Prints the name of the trainer, the Digimon they currently have, and the current active Digimon.
        print("The trainer {name} has the following Digimon".format(name = self.name))
        for Digimon in self.Digimons:
            print(Digimon)
        return "The current active Digimon is {name}".format(name = self.Digimons[self.current_Digimon].name)

    def switch_active_Digimon(self, new_active):
        # Switches the active Digimon to the number given as a parameter
        # First checks to see the number is valid (between 0 and the length of the list)
        if new_active < len(self.Digimons) and new_active >= 0:
            # You can't switch to a Digimon that is knocked out
            if self.Digimons[new_active].is_knocked_out:
                print("{name} is knocked out. You can't make it your active Digimon".format(name = self.Digimons[new_active].name))
            # You can't switch to your current Digimon
            elif new_active == self.current_Digimon:
                print("{name} is already your active Digimon".format(name = self.Digimons[new_active].name))
            # Switches the Digimon
            else:
                self.current_Digimon = new_active
                print("Go {name}, it's your turn!".format(name = self.Digimons[self.current_Digimon].name))

    def use_potion(self):
        # Uses a potion on the active Digimon, assuming you have at least one potion.
        if self.potions > 0:
            print("You used a potion on {name}.".format(name = self.Digimons[self.current_Digimon].name))
            # A potion restores 20 health
            self.Digimons[self.current_Digimon].gain_health(20)
            self.potions -= 1
        else:
            print("You don't have any more potions")

    def attack_other_trainer(self, other_trainer):
        # Your current Digimon attacks the other trainer's current Digimon
        my_Digimon = self.Digimons[self.current_Digimon]
        their_Digimon = other_trainer.Digimons[other_trainer.current_Digimon]
        my_Digimon.attack(their_Digimon)

# Six Digimon are made with different levels. (If no level is given, it is level 5)
b = Digimon("Squirtle", "Water")
c = Digimon("Lapras", "Water", 9)
d = Digimon("Bulbasaur", "Grass", 10)
e = Digimon("Vulpix", "Fire")
f = Digimon("Staryu", "Water", 4)
a = Digimon("Charmander", "Fire", 7)


#Getting input to get the trainers names and letting them select the Digimon they want.
trainer_one_name = input("Welcome to the world of Digimon. Please enter a name for player one and hit enter. ")
trainer_two_name = input("Hi, " + str(trainer_one_name) + "! Welcome! Let's find you an opponent. Enter a name for the second player. ")

choice = input("Hi, " + trainer_two_name + "! Let's pick our Digimon! " + trainer_one_name + ", would you like a Level 7 Charmander, or a Level 7 Squirtle? " + trainer_two_name + " will get the other one. Type either 'Charmander' or 'Squirtle'. ")

while choice != 'Charmander' and choice != 'Squirtle':
  choice = input("Whoops, it looks like you didn't choose 'Charmander' or 'Squirtle'. Try selecting one again! ")

# Keeping track of which Digimon they chose
trainer_one_Digimon = []
trainer_two_Digimon = []

if choice == 'Charmander':
  trainer_one_Digimon.append(a)
  trainer_two_Digimon.append(b)

else:
  trainer_one_Digimon.append(b)
  trainer_two_Digimon.append(a)

# Selecting the second Digimon
choice = input(trainer_two_name + ", would you like a Level 9 Lapras, or a Level 10 Bulbasaur? " + trainer_one_name + " will get the other one. Type either 'Lapras' or 'Bulbasaur'. ")

while choice != 'Lapras' and choice != 'Bulbasaur':
  choice = input("Whoops, it looks like you didn't choose 'Lapras' or 'Bulbasaur'. Try selecting one again! ")

if choice == 'Lapras':
  trainer_one_Digimon.append(d)
  trainer_two_Digimon.append(c)

else:
  trainer_one_Digimon.append(c)
  trainer_two_Digimon.append(d)

# Selecting the third Digimon
choice = input(trainer_one_name + ", would you like a Level 5 Vulpix, or a Level 4 Staryu? " + trainer_two_name + " will get the other one. Type either 'Vulpix' or 'Staryu'. ")

while choice != 'Vulpix' and choice != 'Staryu':
  choice = input("Whoops, it looks like you didn't choose 'Vulpix' or 'Staryu'. Try selecting one again! ")

if choice == 'Vulpix':
  trainer_one_Digimon.append(e)
  trainer_two_Digimon.append(f)

else:
  trainer_one_Digimon.append(f)
  trainer_two_Digimon.append(e)
  
# Creating the Trainer objects with the given names and Digimon lists
trainer_one = Trainer(trainer_one_Digimon, 3, trainer_one_name)
trainer_two = Trainer(trainer_two_Digimon, 3, trainer_two_name)

print("Let's get ready to fight! Here are our two trainers")

print(trainer_one)
print(trainer_two)

# Testing attacking, giving potions, and switching Digimon. This could be built out more to ask for input
trainer_one.attack_other_trainer(trainer_two)
trainer_two.attack_other_trainer(trainer_one)
trainer_two.use_potion()
trainer_one.attack_other_trainer(trainer_two)
trainer_two.switch_active_Digimon(0)
trainer_two.switch_active_Digimon(1)


# def battle(trainer_one, trainer_two):
#     # Print initial battle information
#     print("Let the battle begin between {one} and {two}!".format(one=trainer_one.name, two=trainer_two.name))
    
#     # Initialize turn counter
#     turn = 1
    
#     # Continue battle until a winning condition is met
#     while True:
#         print("\nTurn", turn)
#         print(trainer_one)
#         print(trainer_two)
        
#         # Trainer one attacks trainer two
#         trainer_one.attack_other_trainer(trainer_two)
#         if check_winner(trainer_two):
#             print("{name} has no more Pokémon left! {winner} wins!".format(name=trainer_two.name, winner=trainer_one.name))
#             break
        
#         # Trainer two attacks trainer one
#         trainer_two.attack_other_trainer(trainer_one)
#         if check_winner(trainer_one):
#             print("{name} has no more Pokémon left! {winner} wins!".format(name=trainer_one.name, winner=trainer_two.name))
#             break
        
#         # Increment turn counter
#         turn += 1

# def check_winner(trainer):
#     # Check if all of the trainer's Pokémon are knocked out
#     return all(Digimon.is_knocked_out for Digimon in trainer.Digimons)

# # Example of how to start the battle
# battle(trainer_one, trainer_two)


# still working
# 
# and working

# new feature add