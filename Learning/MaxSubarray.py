def max_subarrays_with_same_sum(values):
    sum_counts = {}  # Dictionary to store sum -> frequency mapping

    for start in range(len(values)):
        sub_sum = 0
        for end in range(start, len(values)):
            sub_sum += values[end]
            sum_counts[sub_sum] = sum_counts.get(sub_sum, 0) + 1

    # Find the highest frequency
    max_count = max(sum_counts.values(), default=0)

    return max_count


# Example usage
values = [2, 4, 1, 3, 2]
print(max_subarrays_with_same_sum(values))  # Output: 2