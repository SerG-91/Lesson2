def test_category_init(category1):
    assert category1.name == "Смартфоны"
    assert category1.description == ("Смартфоны, как средство не только коммуникации, но и получения"
                                     " дополнительных функций для удобства жизни")
    assert category1.category_count == 1
    assert category1.product_count == 2


def test_add_product(category1, product5):
    category1.add_product(product5)
    assert category1.get_product[-1].name == "Iphone"


def test_str_print(category1):
    assert str(category1) == "Смартфоны, количество продуктов: 2 шт."
