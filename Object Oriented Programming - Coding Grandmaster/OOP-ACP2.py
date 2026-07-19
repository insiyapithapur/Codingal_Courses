class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


radius = float(input("Enter the radius of the circle: "))

circle = Circle(radius)

print("Area of the circle:", circle.calculate_area())
print("Perimeter of the circle:", circle.calculate_perimeter())