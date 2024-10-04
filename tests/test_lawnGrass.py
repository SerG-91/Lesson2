import pytest


def test_smartphone_init(lawn_grass1):
    assert lawn_grass1.name == "Газон-1"
    assert lawn_grass1.description == "Description"
    assert lawn_grass1.price == 3000
    assert lawn_grass1.quantity == 2
    assert lawn_grass1.country == "Country"
    assert lawn_grass1.germination_period == "GerminationPeriod"
    assert lawn_grass1.color == "Red"


def test_smartphone_add(lawn_grass1, lawn_grass2):
    assert lawn_grass1 + lawn_grass2 == 24000


def test_smartphone_add_error(lawn_grass1):
    with pytest.raises(TypeError):
        result = lawn_grass1 + 11
