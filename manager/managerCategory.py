from core.models.category import Category
from core.models.db_helper import db_helper
import os


class ManagerCategory:
    def __init__(self):
        self.db_helper = db_helper
        self.running: bool = True

    def manage_category(
            self,
    ) -> None:
        while self.running:
            os.system('clear')
            print("----КЕРУВАННЯ КАТЕГОРІЯМИ----")
            print("-----------------------------------------------------------")
            print("1 - Вивести список категорій")
            print("-----------------------------------------------------------")
            print("2 - Додати категорію")
            print("-----------------------------------------------------------")
            print("3 - Редагувати категорію")
            print("-----------------------------------------------------------")
            print("4 - Видалити категорію")
            print("-----------------------------------------------------------")
            print("0 - Назад")
            print("-----------------------------------------------------------")
            action: int = int(input())
            match action:
                case 1:
                    with db_helper.get_db() as db:
                        categories = db.query(Category).all()
                        for category in categories:
                            print(f"ID: {category.id}, Назва: {category.category_name}")
                        input(("Нажміть будь-яку клавішу для продовження:"))
                case 2:
                    category_name: str = str(input("Введіть назву нової категорії:"))
                    with db_helper.get_db() as db:
                        new_category = Category(category_name=category_name)
                        db.add(new_category)
                        db.commit()
                        print("Категорія створена")
                        input(("Нажміть будь-яку клавішу для продовження:"))

                case 3:
                    with db_helper.get_db() as db:
                        categories = db.query(Category).all()
                        for category in categories:
                            print(f"ID: {category.id}, Назва: {category.category_name}")
                        _category = db.query(Category).filter(
                            Category.id == int(input("Введіть ID категорії:"))).first()
                        new_category_name = str(input(
                            f'Введіть нову назву категорії або нажміть Enter щоб залишить стару (стара назва {_category.category_name}):'))

                        if new_category_name:
                            _category.category_name = new_category_name

                        db.commit()
                        print("Категорія оновленна")

                case 4:
                    with db_helper.get_db() as db:
                        categories = db.query(Category).all()
                        print("-----------------------------------------------------------")
                        for category in categories:
                            print(f"ID: {category.id}, Назва: {category.category_name}")
                        print("-----------------------------------------------------------")
                        category_id = int(input("Введіть ID категорії для видалення: "))

                        category = db.query(Category).filter(Category.id == category_id).first()

                        if category:
                            print("Пов'язані товари, які будуть видалені:")
                            print("-----------------------------------------------------------")
                            for product in category.products:
                                print(f"ID: {product.id}, Назва: {product.name}")
                            print("-----------------------------------------------------------")
                            db.delete(category)
                            db.commit()
                            print("Категорія та всі пов'язані товари видалені.")
                            input("Нажміть будь-яку клавішу для продовження:")
                        else:
                            print("Категорію з таким ID не знайдено.")
                        os.system('cls')
                        print("Залишилися категорії та їх товари:")
                        remaining_categories = db.query(Category).all()
                        for category in remaining_categories:
                            print(f"Категорія ID: {category.id}, Назва: {category.category_name}")
                            for product in category.products:
                                print(f"   Товар ID: {product.id}, Назва: {product.name}")

                        input("Нажміть будь-яку клавішу для продовження:")

                case 0:
                    self.running = False
