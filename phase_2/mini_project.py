class Character:
    
    """
    A base class representing a character in the game.
    """

    def __init__(self, emoji:str, name:str, health:int, strength:int):
        
        """
        Base class for all characters in the game.
        Args:
            emoji (str): The emoji representation of the character.
            name (str): The name of the character.
            health (int): The health points of the character.
            strength (int): The attack strength of the character.
        """
        
        self.emoji = emoji
        self.name = name
        self.health = health
        self.strength = strength
        self.alive_status = True
        
    def stats(self):
        
        """
        Returns a string representation of the character's current stats.
        Returns:
            str: A string containing the character's name, health, and strength.
        """
        
        return f'Name: {self.name} | Health: {self.health} | Strength: {self.strength}'
    
    def died_message(self):
        
        """
        Returns a message indicating that the character has been defeated.
        Returns:
            str: A message indicating the character's defeat.
        """
        
        return f"{self.name} has been defeated!"

class Warrior(Character):
    
    """
    A subclass of Character representing a warrior with armor.
    """
    
    def __init__(self, emoji:str, name:str, health:int, strength:int, armor:int):
        
        """
        Initializes a Warrior character with additional armor attribute.
        Args:
            emoji (str): The emoji representation of the warrior.
            name (str): The name of the warrior.
            health (int): The health points of the warrior.
            strength (int): The attack strength of the warrior.
            armor (int): The armor points of the warrior, which can absorb damage before health is affected.
        """
        
        super().__init__(emoji, name, health, strength)
        self.armor = armor
        print(f'{self.stats()} | Armor: {self.armor}')

    def heal(self, amount:int):
        
        """
        Heals the warrior by a specified amount, but only if they are still alive.
        Args:
            amount (int): The amount of health to restore to the warrior.
        """
        
        if not self.alive_status:
            print(f"{self.name} cannot be healed because he's are defeated.")
            return
        health_before = self.health
        self.health += amount
        print(f"🩹 {self.name} is healing {amount} with bandages! | Health: {health_before} -> {self.health}")
        
    def attack(self, character):
        
        """
        Attacks another character, reducing their health by the warrior's strength. If the target's health drops to 0 or below, they are marked as defeated.
        Args:
            character (Character): The target character to attack.
        """
        
        if not character.alive_status:
            print(f"{character.name} is already defeated! {self.name} cannot attack.")
            return
        
        print(f"⚔️  {self.name} attacks {character.name} with a mighty sword!", end = " | ")
        character.health -= self.strength
        
        if character.health <= 0:
            print(f"{self.name} has defeated {character.name}!")
            character.alive_status = False
            return
        print(f"{character.name}'s health is now {character.health}")
        
class Goblin(Character):

    """
    A subclass of Character representing a goblin.
    """

    def __init__(self, emoji:str, name:str, health:int, strength:int):
        
        """
        Initializes a Goblin character.
        Args:
            emoji (str): The emoji representation of the goblin.
            name (str): The name of the goblin.
            health (int): The health points of the goblin.
            strength (int): The attack strength of the goblin.
        """

        super().__init__(emoji, name, health, strength)
        print(self.stats())
        
    def attack(self, character):
        
        """
        Attacks another character, reducing their health by the goblin's strength. If the target's health drops to 0 or below, they are marked as defeated.
        Args:
            character (Character): The target character to attack.
        """
        
        if not character.alive_status:
            print(f"{character.name} is already defeated! {self.name} cannot attack.")
            return
        
        print(f"{self.emoji} {self.name} attacks {character.name} with a rusty dagger!")
        if character.armor > 0:
            character.armor -= self.strength
            if character.armor > 0:
                print(f"    {self.name} attacks {character.name}! | {character.name}'s armor is now {character.armor}")
            elif character.armor == 0:
                print(f"    {self.name} attacks {character.name}! | {character.name}'s armor is now 0 | {character.name} is vulnerable!")
            else:
                character.health -= abs(character.armor)
                print(f"    {character.name} has lost all armor and takes {abs(character.armor)} damage! | {character.name}'s health is now {character.health}")
                character.armor = 0
                
        else:
            character.health -= self.strength
            
            if character.health <= 0:
                character.alive_status = False
                print(f"    {self.name} has defeated {character.name}!")
                return

            print(f"    {self.name} attacks {character.name}! | {character.name}'s health is now {character.health}")           
        
if __name__ == "__main__":
    warrior = Warrior("🤖", "Aragorn", health=100, strength=20, armor=5)
    goblin = Goblin("👹", "Glim", health=50, strength=10)

    warrior.attack(goblin)
    warrior.attack(goblin)
    warrior.attack(goblin)
    warrior.attack(goblin)  # Testing attacking an already defeated character