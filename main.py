from menu import products
from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type
from management.product_handler import add_product


if __name__ == "__main__":

    print(get_product_by_id(8))
    print(get_products_by_type('vegetable'))
    print(add_product(products, description="Teste",
          price=34.91, rating=7, title="Test", type="drink"))
