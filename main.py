BASKET = [{'Produkt': 'T-Shirt', 'Preis': 20}, {'Produkt': 'Hose', 'Preis': 50}]
DISCOUNT = 0.1


# Unpure function
def calculate_total_unpure():
    global BASKET, DISCOUNT
    total = sum(item['Preis'] for item in BASKET)
    discount = total * DISCOUNT
    total = total - discount
    print(f'Gesamtpreis: {total}')
    return total


# Pure function
def calculate_total_pure(basket, discount):
    """Berechnet den Gesamtpreis eines Warenkorbs mit einem Rabatt."""
    total = sum(item['Preis'] for item in basket)
    discount_amount = total * discount
    total = total - discount_amount
    return total


if __name__ == '__main__':
    print('Unpure function:')
    calculate_total_unpure()

    print('Pure function:')
    total = calculate_total_pure(BASKET, DISCOUNT)
    print(f'Gesamtpreis: {total}')
