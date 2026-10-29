
def single_number(nums: list[int]) -> int:
    result = 0

    for num in nums:
        result ^= num

    return result


def main():
    nums = list(map(int, input("Enter numbers: ").split()))
    print("Single number:", single_number(nums))


if __name__ == "__main__":
    main()
