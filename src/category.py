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
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else []

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    @property
    def get_product(self):
        """Геттер для получения списка продуктов"""
        return self.__products

    def add_product(self, new_product):
        """Метод добавления продукта в приватный список продуктов"""
        if isinstance(new_product, Product):
            self.get_product.append(new_product)
            Category.product_count += 1


    @property
    def product_list(self):
        """Метод реализации вывода списка продуктов из приватного списка"""
        product_str = ""
        for product in self.get_product:
            product_str += (
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            )
        return product_str

# result = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций"
#                                "для удобства жизни", ["product1", "product2", "product3"])
# print(str(result))
