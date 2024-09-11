# """
# Создай класс Album у которого есть поля
#
# - Исполнитель (artist) - строка
# - Название (title) - строка
# - Треки (tracks) - это **список**
#
# **Создай два экземпляра album_1 и album_2**
#
# Исполнитель: Queen
#
# Название: Killer Queen
#
# Треки: Brighton rock, Killer Queen, Tenement Funster
#
# Исполнитель: Metallica
#
# Название: Black Album
#
# Треки: Enter Sandman, Sad But True, Holier Than Thou
# """
#
# # class Album:
# #     artist: str
# #     title: str
# #     tracks: list
# #
# #     def __init__(self, artist=None, title=None, tracks=None):
# #         self.artist = artist
# #         self.title = title
# #         self.tracks = tracks
# #
# #
# # album_1 = Album("Quinn", "Killer Queen", ["Brighton rock", "Killer Queen", "Tenement Funster"])
# #
# # album_2 = Album("Metallica", "Black Album", ["Enter Sandman", "Sad But True", "Holier Than Thou"])
#
#
# # код для проверки
# # print(album_1.artist, album_1.title, len(album_1.tracks), "треков")  # Queen Killer Queen 3 треков
# # print(album_2.artist, album_2.title, len(album_2.tracks), "треков")  # Metallica Black Album 3 треков
#
#
# """
# Создай класс Bottle (бутылка) c полями
#
# - Цвет (color) - строка
# - Объем (volume) - число с плавающей точкой
#
# Создай три экземпляра
#
# - Красную 0.7
# - Белую 0.3
# - Черную 1.0
# """
#
#
# # class Bottle:
# #     color: str
# #     volume: float
# #
# #     def __init__(self, color, volume):
# #         self.color = color
# #         self.volume = volume
# #
# #
# # bottle_1 = Bottle("Красная", 0.7)
# # bottle_2 = Bottle("Белую", 0.3)
# # bottle_3 = Bottle("Черную", 1.0)
# #
# #
# # # код для проверки
# # print(bottle_1.color, bottle_1.volume)  # Красная 0.7
# # print(bottle_2.color, bottle_2.volume)  # Белая 0.3
# # print(bottle_3.color, bottle_3.volume)  # Черная 1.0
#
#
# """
# Создай класс `Number` c полем `value` (указывается при инициализации)
#
# Создай экземпляр, например `x = Number(7)`
#
# Добавь методы:
#
# `.get()` возвращает текущее value
#
# `.add(<значение>)` добавляет указанное число к value
#
# `.substract(<значение>)` вычитает указанное число из value
# """
#
# # class Number:
# #     value: str
# #
# #     def __init__(self, value):
# #         self.value = value
# #
# #     def get(self):
# #         return self.value
# #
# #     def add(self, char):
# #         self.value += char
# #         return self.value
# #
# #     def substract(self, char):
# #         self.value -= char
# #         return self.value
# #
# #
# #
# # # код для проверки
# # n = Number(7)
# # print(n.get())  # 7
# # n.add(3)
# # print(n.get())  # 10
# # n.substract(5)
# # print(n.get())  # 5
#
# """
# Создай класс Student (студент) с полями
#
# - Имя (name) - строка
# - Курс (course) - целое число
#
# Создай два экземпляра
#
# - Алиса , 3 [курс]
# - Маргарита , 2 [курс]
# """
#
#
# # class Student:
# #     name: str
# #     course: int
# #
# #     def __init__(self, name, course):
# #         self.name = name
# #         self.course = course
# #
# #
# # student_1 = Student("Алиса", 3)
# # student_2 = Student("Маргарита", 2)
# #
# #
# # # код для проверки
# # print(student_1.name, student_1.course)  # Алиса 3
# # print(student_2.name, student_2.course)  # Маргарита 2
from src.category import Category
from src.product import Product

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)