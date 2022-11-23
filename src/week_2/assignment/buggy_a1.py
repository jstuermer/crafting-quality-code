def num_buses(n):
    buses = n // 50 + 1
    return buses

def stock_price_summary(price_changes):
    gains = price_changes[0]
    losses = price_changes[0]
    for p in price_changes:
        if p > 0:
            gains = gains + p
        elif p < 0:
            losses = losses + p
    return gains, losses

def swap_k(L, k):
    front_items = []
    back_items = []
    for i in range(k):
        back_items.append(L[-(k-i)])
        front_items.append(L[i])
    L[:] = back_items + L[k:-k] + front_items