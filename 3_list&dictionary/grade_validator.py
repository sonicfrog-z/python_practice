def validate(record):
    name, sid, q1, q2, q3, grade = record.split(',')
    scores = list(map(int, [q1, q2, q3]))
    ave = sum(scores) // len(scores)
    if assign_grade(ave) != grade:
        print(name, sid)


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


with open('students.csv') as fin:
    for line in fin:
        record = line.strip()
        validate(record)