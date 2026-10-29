
def is_valid(s: str) -> bool:
    stack = []
    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


def main():
    s = input("Enter brackets: ")

    if is_valid(s):
        print("Valid parentheses")
    else:
        print("Invalid parentheses")


if __name__ == "__main__":
    main()
