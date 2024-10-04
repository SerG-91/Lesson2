import pytest


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Sumsung"
    assert smartphone1.description == "Description"
    assert smartphone1.price == 5000
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == "Efficiency"
    assert smartphone1.model == "Model"
    assert smartphone1.memory == 36
    assert smartphone1.color == "red"


def test_smartphone_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 45000


def test_smartphone_add_error(smartphone1):
    with pytest.raises(TypeError):
        result = smartphone1 + 11
