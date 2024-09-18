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

    def add_product(self, new_product):
        """Метод добавления продукта в приватный список продуктов"""
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def get_product(self):
        """Геттер для получения продуктов"""
        return self.__products

    @property
    def product_list(self):
        """Метод реализации вывода списка продуктов из приватного списка"""
        product_str = ""
        for product in self.get_product:
            product_str += (
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            )
        return product_str
