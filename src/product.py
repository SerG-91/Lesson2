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
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, list_product):
        """Класс метод по созданию нового продукта"""
        # if list_product.get('name') == Product.name:
        #     name = list_product.get('name')
        #     description = list_product.get('description')
        #     quantity = list_product.get('quantity') + Product.quantity
        #     if list_product.get('price') > Product.price:
        #         price = list_product.get('price')
        #     price = Product.quantity
        #     return cls(name, description, price, quantity)
        name = list_product.get('name')
        description = list_product.get('description')
        price = list_product.get('price')
        quantity = list_product.get('quantity')
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер получения цены товара"""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для записи новой цены"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if value < self.price:
                choice = input("YES(y) / NO(n)")
                if choice == 'y':
                    self.__price = value
                else:
                    self.__price = self.__price
