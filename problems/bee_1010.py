def get_item_data():
    """Prompts for item data and returns the code, quantity and value."""
    code, quantity, value = input().split()
    return code, int(quantity), float(value)


def calculate_total_value(item1, item2):
    """Calculates the total amount to be paid for two items."""
    _, quantity1, value1 = item1
    _, quantity2, value2 = item2

    total = quantity1 * value1 + quantity2 * value2
    return total


def main():
    """Main function of the program."""
    # Get item data
    item1 = get_item_data()
    item2 = get_item_data()

    # Calculate the total amount to be paid
    total_to_pay = calculate_total_value(item1, item2)

    # Display the formatted total amount
    print('TOTAL AMOUNT TO PAY: $ {:.2f}'. format(total_to_pay))


if __name__ == "__main__":
    main()
