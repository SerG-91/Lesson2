class Product:
    """Класс описания продуктов"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Конструктор класса с аргументами: имя/описание/цена/количество"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
