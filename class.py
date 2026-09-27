class character:
    def __init__(self,name,health,attack):
        self.name=name
        self.health=health
        self.attack=attack

    def powers(self):
        print(f"This character {self.name} attack with power {self.attack}")


warrior=character("Thor",100,70)
mage=character("Loki",100,80)

warrior.powers()
mage.powers()