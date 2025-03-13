import argparse

from constants import (
    MAX_DIMENSION,
    MAX_MASS,
    MAX_VOLUME,
    STANDARD,
    SPECIAL,
    REJECTED,
    INVALID,
)


def sort(width, height, length, mass):
    """Sorts packages according to their properties"""

    if any(property <= 0 for property in [width, height, length, mass]):
        return INVALID

    volume = width * height * length
    bulky = volume >= MAX_VOLUME or max(width, height, length) >= MAX_DIMENSION
    heavy = mass >= MAX_MASS

    return REJECTED if bulky and heavy else SPECIAL if bulky or heavy else STANDARD


if __name__ == "__main__":
    parser = argparse.ArgumentParser("main.py")
    parser.add_argument("width", help="The package's width in cm", type=float)
    parser.add_argument("height", help="The package's height in cm", type=float)
    parser.add_argument("length", help="The package's length in cm", type=float)
    parser.add_argument("mass", help="The package's mass in kg", type=float)
    args = parser.parse_args()

    stack = sort(**args.__dict__)

    (
        print("All properties need to be greater than 0")
        if stack == INVALID
        else print(stack)
    )
