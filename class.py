class car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def display_info(self):
        print(f"My car is a {self.color} {self.model}")

    def change_color(self, color):
        self.color = color

my_car = car(model = "Toyota", color = "Blue")
my_car.display_info()
my_car.change_color("white")
##print(f"The color is {my_car.color}")
my_car.display_info()