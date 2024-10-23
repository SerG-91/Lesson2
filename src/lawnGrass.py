from src.product import Product, Mixin


class LawnGrass(Product, Mixin):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError


if __name__ == "__main__":
    low = LawnGrass("444444rdfs", "Description", 5000, 5, "Efficiency", "ST4", "red")
