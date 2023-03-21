from menu import products


def get_product_by_id(id: int):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")

    for product in products:
        if product['_id'] == id:
            return product

    return {}


def get_products_by_type(type: str):
    if not isinstance(type, str):
        raise TypeError("product type must be a str")

    list_products = []
    for product in products:
        if product["type"] == type:
            list_products.append(product)

    if len(list_products) > 0:
        return list_products

    return []
