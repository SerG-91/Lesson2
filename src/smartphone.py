from src.product import Product
from src.lawnGrass import LawnGrass


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError


#

if __name__ == "__main__":
    smart1 = Smartphone("Sumsung", "Description", 5000, 5, "Efficiency", "ST4", 36, "red")
    smart2 = Smartphone("Iphon", "Description", 5000, 5, "Efficiency", "ST4", 36, "red")

    low = LawnGrass("444444rdfs", "Description", 5000, 5, "Efficiency", "ST4", "red")
    print(smart1 + low)
