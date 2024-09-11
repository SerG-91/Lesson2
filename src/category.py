from src.product import Product


class Category:
    """Класс описания продуктов"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0


    def __init__(self, name, description, products):
        """Конструктор класса с аргументами: имя/описание/цена/список_товаров"""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else []
