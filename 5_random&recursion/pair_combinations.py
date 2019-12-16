pair_combinations = []

current = [-1] * 6


def get_all_pair_combinations(current, pair_combinations):
    if -1 not in current:
        # find one pair combination
        pair_combinations.append(current[:])
    else:
        first_index = current.index(-1)
        for second_index in range(first_index+1, len(current)):
            if current[second_index] == -1:
                current[first_index] = second_index
                current[second_index] = first_index

                get_all_pair_combinations(current, pair_combinations)

                current[first_index] = -1
                current[second_index] = -1


get_all_pair_combinations(current, pair_combinations)

print(len(pair_combinations))
print(pair_combinations)
