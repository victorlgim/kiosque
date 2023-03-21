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


def menu_report():

    product_count = len(products)

    total_price = sum(product.get("price", 0) for product in products)
    avg_price = round(total_price / product_count, 2)

    type_count = {}
    for product in products:
        product_type = product.get("type")
        if product_type in type_count:
            type_count[product_type] += 1
        else:
            type_count[product_type] = 1

    most_common_type = max(type_count, key=type_count.get)

    report = f"Products Count: {product_count} - Average Price: ${avg_price} - Most Common Type: {most_common_type}"

    return report


def add_product_extra(menu, *args, **kwargs):

    for key in args:
        if key not in kwargs:
            raise KeyError(f"field {key} is required")

    extra_keys = set(kwargs.keys()) - set(args)
    for key in extra_keys:
        kwargs.pop(key)

    if not menu:
        new_id = 1
    else:
        new_id = max(item['_id'] for item in menu) + 1

    new_product = {'_id': new_id}
    new_product.update(kwargs)

    menu.append(new_product)

    return new_product
