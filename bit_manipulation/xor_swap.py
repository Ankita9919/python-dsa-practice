def xor_swap(a: int, b: int) -> tuple[int, int]:
    a ^= b
    b ^= a
    a ^= b
    return a, b


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    a, b = xor_swap(a, b)

    print(f"After swapping: a = {a}, b = {b}")


if __name__ == "__main__":
    main()
