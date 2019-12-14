with open('signup.txt') as fin:
    usage = {}

    for line in fin:
        group_name = ','.join(sorted(line.strip().split(',')))
        usage.setdefault(group_name, 0)
        usage[group_name] += 1

    for group_name, freq in usage.items():
        print('{}: {}'.format(group_name, freq))
