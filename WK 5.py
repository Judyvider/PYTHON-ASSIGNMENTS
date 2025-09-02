class Superhero:
    def __init__(self, name, secret_identity, superpower):
        self.name = name
        self.secret_identity = secret_identity
        self.superpower = superpower
        print(f"A new hero has been created: {self.name}!")

    def display_info(self):
        print(f"Hero Name: {self.name}")
        print(f"Secret Identity: {self.secret_identity}")
        print(f"Superpower: {self.superpower}")

    def use_power(self):
        print(f"{self.name} is using their {self.superpower}!")

class FlyingSuperhero(Superhero):
    def __init__(self, name, secret_identity, superpower, max_flight_speed):
        super().__init__(name, secret_identity, superpower)
        self.max_flight_speed = max_flight_speed
        print(f"{self.name} also has the ability to fly!")

    def fly(self):
        print(f"{self.name} is flying at a maximum speed of {self.max_flight_speed} km/h!")

print("--- Creating a standard superhero ---")
captain_america = Superhero("Captain America", "Steve Rogers", "Enhanced Strength and Durability")
captain_america.display_info()
captain_america.use_power()
print("-" * 30)

print("--- Creating a flying superhero ---")
superman = FlyingSuperhero("Superman", "Clark Kent", "Heat Vision", 28000)
superman.display_info()
superman.use_power()
superman.fly()
print("-" * 30)
