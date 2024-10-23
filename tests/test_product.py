from src.lawnGrass import LawnGrass
from src.product import Product, Mixin, BaseProduct
from src.smartphone import Smartphone


def test_product_init(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_product_init_2(product2):
    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 31000.0
    assert product2.quantity == 14


def test_new_product(product3):
    product = Product.new_product(product3)
    assert product.name == "Samsung Galaxy Ultra"


def test_add_product(product1, product2):
    assert product1 + product2 == 1334000.0


def test_str_product(product1):
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт"


def test_classes():
    assert Smartphone.__mro__[1:] == LawnGrass.__mro__[1:]
    assert issubclass(Product, Mixin) is True
    assert issubclass(Mixin, object) is True
    assert issubclass(BaseProduct, object) is True
