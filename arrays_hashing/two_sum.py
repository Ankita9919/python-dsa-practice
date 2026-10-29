


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], index]

        seen[num] = index

    return []


def main():
    nums = list(map(int, input("Enter numbers: ").split()))
    target = int(input("Enter target: "))

    result = two_sum(nums, target)

    if result:
        print("Indices:", result)
    else:
        print("No solution found")


if __name__ == "__main__":
    main()
