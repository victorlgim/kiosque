
from management.product_handler import get_product_by_id


def calculate_tab(consumptions):
    total_price = sum(consumption['amount'] * get_product_by_id(
        consumption['_id'])['price'] for consumption in consumptions)
    subtotal = round(total_price, 2)
    return {"subtotal": f"${subtotal}"}
