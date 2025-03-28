class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.__battery_life = battery_life  # Private attribute

    def turn_on(self):
        return f"{self.brand} {self.model} is now ON."

    def turn_off(self):
        return f"{self.brand} {self.model} is now OFF."

    def get_battery_status(self):
        return f"Battery life: {self.__battery_life}%"

# Child class demonstrating Inheritance
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_life, strap_color):
        super().__init__(brand, model, battery_life)
        self.strap_color = strap_color

    def show_time(self):
        return "Showing current time on the smartwatch."

