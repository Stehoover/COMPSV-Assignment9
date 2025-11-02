class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    def __init__(self, name: str):
        self.name = name
        self.friends = []  # List of Person objects

    def add_friend(self, friend: 'Person') -> None:
        if friend not in self.friends:
            self.friends.append(friend)

class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    def __init__(self):
        # Dictionary where keys are names (str) and values are Person objects
        self.people = {}

    def add_person(self, name: str) -> None:
        if name in self.people:
            print(f"Error: A person named '{name}' already exists in the network.")
        else:
            new_person = Person(name)
            self.people[name] = new_person
            print(f"'{name}' was added to the network.")

    def add_friendship(self, person1_name: str, person2_name: str) -> None:
        # Checks if both people exist in the network
        if person1_name not in self.people:
            print(f"Error: '{person1_name}' does not exist in the network.")
            return
        if person2_name not in self.people:
            print(f"Error: '{person2_name}' does not exist in the network.")
            return
        
        # Gets the Person objects
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        
        # Creates the bidirectional friendship
        person1.add_friend(person2)
        person2.add_friend(person1)
        print(f"Established friendship between '{person1_name}' and '{person2_name}'.")

    def print_network(self) -> None:
        print("\n--- Social Network ---")
        if not self.people:
            print("The network is empty.")
            return
            
        for person_name, person_obj in self.people.items():
            # Creates a list of friend names
            friend_names = [friend.name for friend in person_obj.friends]
            
            if not friend_names:
                print(f"{person_name}: (No friends)")
            else:
                friends_str = ", ".join(friend_names)
                print(f"{person_name}: {friends_str}")
        print("----------------------")

# Test your code here

print("--- Person Class Example ---")
alex_p = Person("Alex")
jordan_p = Person("Jordan")
print(f"{alex_p.name}'s friends: {[f.name for f in alex_p.friends]}") # []
alex_p.add_friend(jordan_p)
print(f"{alex_p.name}'s friends: {[f.name for f in alex_p.friends]}") # ['Jordan']
print("----------------------------\n")


print("--- SocialNetwork Class Example ---")
network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan") 
network.add_person("Morgan")
network.add_person("Alex") # Error: Duplicate

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")  # Error: Taylor doesn't exist

# Print the final network
network.print_network()