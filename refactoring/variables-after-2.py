import unittest


TAX_RATE = 0.15
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1


def calculate_subtotal():
    print('Calculate subtotal')
    return 400.0


def calculate_taxable_subtotal():
    print('Calculate taxable subtotal')
    return 300.0


def calculate_total():
    print('Calculate total')
    subtotal = calculate_subtotal()
    taxable_subtotal = calculate_taxable_subtotal()
    tax = taxable_subtotal * TAX_RATE
    eligible_for_discount = subtotal > DISCOUNT_THRESHOLD
    discount = subtotal * DISCOUNT_RATE if eligible_for_discount else 0
    total = subtotal + tax - discount
    return total


if __name__ == "__main__":
    total = calculate_total()
    print('Total: {}'.format(total))
    