"""Testing sys module"""

import sys


def main():
    """Simple function"""
    print("Ejecucion exitosa")
    print(f"{sys.path}")


def get_platform():
    """Simple get platform string"""
    match sys.platform:
        case "windows":
            print(f"Running on {sys.platform}")
        case _:
            raise NotImplementedError(f"{sys.platform} not supported!")


def print_menu():
    """Simple print menu"""
    menu = {1: "Print program name", 2: "Age calculation"}

    for option, desc in menu.items():
        print(f"{option} -> {desc}")


if __name__ == "__main__":
    main()
