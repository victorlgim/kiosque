from menu import products
from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type
from management.product_handler import add_product
from management.tab_handler import calculate_tab
from management.product_handler import menu_report
from management.product_handler import add_product_extra

if __name__ == "__main__":

    print(get_product_by_id(8))
    print(get_products_by_type('vegetable'))
    print(add_product(products, description="Teste",
          price=34.91, rating=7, title="Test", type="drink"))
    print(calculate_tab([{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]))
    print(menu_report())

    required_keys = ("description", "price", "rating", "title", "type")
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
    print(add_product_extra(products, *required_keys, **new_product))
