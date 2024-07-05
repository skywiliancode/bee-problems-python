
def get_item_value():
    """Function for return radius"""
    radius = float(input())
    return radius


def calculate_circle_area(radius):
    PI = 3.14159
    area = 4/3 * PI * (radius * radius * radius)
    return area


def main():

    radius = get_item_value()
    area = calculate_circle_area(radius)

    print('VOLUME = {:.3f}'.format(area))


if __name__ == "__main__":
    main()
