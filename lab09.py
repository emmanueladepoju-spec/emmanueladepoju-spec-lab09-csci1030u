
# Problem-solving practice (LeetCode / ICPC style).


def two_sum(nums, target):
    # Outline:
    # Find two numbers that add up to the target.
    # Example: [2, 7, 11, 15], target = 9.
    # 2 + 7 = 9, so the answer is [0, 1].
    # Use a dictionary to remember numbers and their indices.
    # Check if the required complement has already been seen.

    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i



def max_profit(prices):
    # Outline:
    # Find the maximum profit from buying first and selling later.
    # If the list is empty, return 0.
    # Track the lowest price seen so far.
    # Calculate possible profits and keep the highest one.

    if not prices:
        return 0

    lowest = prices[0]
    best_profit = 0

    for price in prices:
        profit = price - lowest

        if profit > best_profit:
            best_profit = profit

        if price < lowest:
            lowest = price

    return best_profit


def max_subarray(nums):
    # Outline:
    # Find the largest sum of consecutive numbers.
    # Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4].
    # The best group is [4, -1, 2, 1], which adds up to 6.
    # Track the current sum and the largest sum.
    # Either extend the current group or start a new group.

    current_sum = nums[0]
    best_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)

    return best_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    # Check that every opening bracket has a matching closing bracket.
    # Example: "{[]}" is balanced, but "([)]" is not.
    # Use a stack to store opening brackets.
    # Check each closing bracket against the most recent opening bracket.

    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in '([{':
            stack.append(char)

        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(is_balanced("{[]}"))  # True


if __name__ == "__main__":
    main()
