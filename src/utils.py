import json
import os.path
from typing import Any

from config import DATA_PATH
from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """" Функция чтение файла json """

    with open(path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_object_from_json(data: dict) -> Any:
    """ Функция преобразования json файла в экземпляры класса """

    categorys = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categorys.append(Category(**category))
    return categorys


if __name__ == "__main__":

    path_json = os.path.join(DATA_PATH, "products.json")
    product_list = read_json(path_json)
    category_data = create_object_from_json(product_list)
    print(category_data[0].name)
    print(category_data[0].products[0].name)
