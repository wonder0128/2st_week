shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):

    # O(N) + O(M) * O(1) = O(N + M)
    menus_set = set(menus) # O(N)
    for order in orders: # O(M)
        if order not in menus_set: # O(1)
            return False
    return True

result = is_available_to_order(shop_menus, shop_orders)
print(result)