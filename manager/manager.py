import os

from sqlalchemy.orm import joinedload, load_only

from core.models.db_helper import db_helper
from core.models.products import Products


class Manager:
    def __init__(self):
        self.db_helper = db_helper
        self.running: bool = True

    def get_all_products(self):
        while self.running:
            os.system('clear')
            with self.db_helper.get_db() as db:
                all_products = db.query(Products).options(joinedload(Products.category)).all()
                for _ in all_products:
                    print(
                        f"Id: {_.id} | Назва: {_.name} | Ціна: {_.sale} | Опис: {_.description} | Кількість: {_.count} | Категорія: {_.category.category_name}")
                input(("Нажміть будь-яку клавішу для продовження:"))
                self.running = False

    def get_all_product_by_name(self):
        while self.running:

            os.system('clear')
            with self.db_helper.get_db() as db:
                all_product = db.query(Products).options(load_only(Products.name)).all()

                for _ in all_product:
                    print(
                        f"Назва продукту: {_.name}"
                    )
                input(("Нажміть будь-яку клавішу для продовження:"))
                self.running = False
