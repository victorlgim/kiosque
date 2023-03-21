from menu import products
from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type
from management.product_handler import add_product
from management.tab_handler import calculate_tab

if __name__ == "__main__":

    print(get_product_by_id(8))
    print(get_products_by_type('vegetable'))
    print(add_product(products, description="Teste",
          price=34.91, rating=7, title="Test", type="drink"))
    print(calculate_tab([{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]))
