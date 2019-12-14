def validate(record):
    name, sid, *scores, grade = record.split(',')
    scores = list(map(int, scores))
    ave = sum(scores) // len(scores)
    print(name, ave, assign_grade(ave))


def assign_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


with open('students2.csv') as fin:
    for line in fin:
        record = line.strip()
        validate(record)