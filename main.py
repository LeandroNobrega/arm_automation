import argparse
from sort_package.sort_package import sort

def main():
    parser = argparse.ArgumentParser(
        description="Classify a package as STANDARD, SPECIAL, or REJECTED based on its dimensions and mass."
    )

    parser.add_argument("width", type=float, help="Width of the package in cm")
    parser.add_argument("height", type=float, help="Height of the package in cm")
    parser.add_argument("length", type=float, help="Length of the package in cm")
    parser.add_argument("mass", type=float, help="Mass of the package in kg")

    args = parser.parse_args()

    try:
        result = sort(args.width, args.height, args.length, args.mass)
        print(f"Package parameters: Width {args.width}, Height {args.height}, Length {args.length}, Mass {args.mass}")
        print(f"Package classification: {result}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
