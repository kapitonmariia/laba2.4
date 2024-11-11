from core.models.category import Category
from core.models.db_helper import db_helper
from core.models.products import Products


class ManagerSearch:
    def __init__(self):
        self.db_helper = db_helper
        self.running: bool = True

    def search_product(self):
        with self.db_helper.get_db() as db:
            product: str = str(input("Введіть назву продукта"))
            product = db.query(Products).filter(Products.name == product).first()
            category_name = db.query(Category).filter(Category.id == product.id).first().category_name
            print(
                f"Id: {product.id} | Назва: {product.name} | Ціна: {product.sale} | Опис: {product.description} | Кількість: {product.count} | Категорія: {category_name}");
            input(("Нажміть будь-яку клавішу для продовження:"))

    def search_category(self):
        with self.db_helper.get_db() as db:
            category_id = (db.query(Category).filter(
                Category.category_name == str(input("Введіть назву категорії:"))).first()).id

            products = db.query(Products).filter(Products.category_id == category_id).all()
            for product in products:
                print(
                    f"Id: {product.id} | Назва: {product.name} | Ціна: {product.sale} | Опис: {product.description} | Кількість: {product.count} | Категорія: {product.category_id}");
            input(("Нажміть будь-яку клавішу для продовження:"))
