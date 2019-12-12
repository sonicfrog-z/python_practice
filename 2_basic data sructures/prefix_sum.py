def prefix_sum(numbers):
    result = []

    sum_ = 0
    for number in numbers:
        sum_ += number
        result.append(sum_)

    return result


# arr = [1, 4, 3, 10, 6, 8]
# ps = prefix_sum(arr)
# print(ps)  # [1, 5, 8, 18, 24, 32]


def promotion_count(before, after):
    prefix_sum_before = prefix_sum(before)
    prefix_sum_after = prefix_sum(after)

    # diff = []
    #
    # for index in range(len(prefix_sum_after)):
    #     level_diff = prefix_sum_after[index] - prefix_sum_before[index]
    #     diff.append(level_diff)
    #
    # return diff

    return list(
        map(
            lambda a, b: a - b,
            prefix_sum_after,
            prefix_sum_before
        )
    )


before = [26, 33, 19, 30]  # from platinum to bronze
after = [53, 8, 28, 40]

diffs = promotion_count(before, after)
print(diffs)  # [27, 2, 11, 21]