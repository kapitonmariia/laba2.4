import os

from core.models.base import Base
from core.models.category import Category
from core.models.db_helper import db_helper
from core.models.products import Products
from manager.manager import Manager

from manager.managerCategory import ManagerCategory
from manager.managerProducts import ManageProducts
from manager.managerSearch import ManagerSearch

running: bool = True

if __name__ == '__main__':
    Base.metadata.create_all(bind=db_helper.engine)
    while running:
        os.system('clear')
        print("------Виберіть опцію------")
        print("-----------------------------------------------------------")
        print("1 - Пошук товару (Lazy Loading)")
        print("-----------------------------------------------------------")
        print("2 - Пошук по категорії (Lazy Loading)")
        print("-----------------------------------------------------------")
        print("3 - Завантаження вcіх позицій товару (Eager Loading)")
        print("-----------------------------------------------------------")
        print("4 - Завантаженя всіх позицій по вибіркових даних (Explicit Loading)")
        print("-----------------------------------------------------------")
        print("5 - Керування товаром")
        print("-----------------------------------------------------------")
        print("6 - Керування категоріями")
        print("-----------------------------------------------------------")
        print("0 - Вихід")
        print("-----------------------------------------------------------")
        action: int = int(input())
        match action:
            case 1:
                ManagerSearch().search_product()
            case 2:
                ManagerSearch().search_category()

            case 3:
                Manager().get_all_products()
            case 4:
                Manager().get_all_product_by_name()
            case 5:
                ManageProducts().manage_products()
            case 6:
                ManagerCategory().manage_category()
            case 0:
                running = False
