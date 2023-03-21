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


def add_product(menu, **kwargs):
    if not menu:
        new_id = 1
    else:
        max_id = max(product["_id"] for product in menu)
        new_id = max_id + 1

    new_product = {"_id": new_id}
    new_product.update(kwargs)

    menu.append(new_product)

    return new_product
