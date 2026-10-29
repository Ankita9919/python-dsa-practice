def binary_search_descending(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def main():
    nums = list(map(int, input("Enter descending-order numbers: ").split()))
    target = int(input("Enter target: "))

    print("Index:", binary_search_descending(nums, target))


if __name__ == "__main__":
    main()
