def remove_duplicates(nums: list[int]) -> list[int]:
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


def main():
    nums = list(map(int, input("Enter numbers: ").split()))
    print("Unique elements:", remove_duplicates(nums))


if __name__ == "__main__":
    main()
