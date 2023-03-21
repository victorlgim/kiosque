from menu import products


def get_product_by_id(id: int):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")

    for product in products:
        if product['_id'] == id:
            return product

    return {}



