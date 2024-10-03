import pytest

from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawnGrass import LawnGrass


@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 31000.0, 14)


@pytest.fixture
def product5():
    return Product("Iphone", "512GB, Gray space", 31000.0, 14)


@pytest.fixture
def product3():
    product3 = {
            "name": "Samsung Galaxy Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }

    return product3


@pytest.fixture
def category1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения"
                    " дополнительных функций для удобства жизни",
        products=[
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        ]
    )


@pytest.fixture
def smartphone1():
    return Smartphone("Sumsung", "Description", 5000, 5, "Efficiency", "Model", 36, "red")


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone", "Description", 4000, 5, "Efficiency", "Model", 36, "red")


@pytest.fixture
def lawn_grass1():
    return LawnGrass("Газон-1", "Description", 3000, 2, "Country", "GerminationPeriod", "Red")


@pytest.fixture
def lawn_grass2():
    return LawnGrass("Газон-22", "Description", 6000, 3, "Country", "GerminationPeriod", "Red")
