def printer():
    try:
        while True:
            line = yield
            print(line)
    except GeneratorExit:
        pass


def next_line_remover(cr):
    next(cr)
    try:
        while True:
            line = yield
            line = line.strip()
            cr.send(line)
    except GeneratorExit:
        cr.close()


def core_course_checker(marker, cr):
    next(cr)
    try:
        while True:
            title = yield
            if title.endswith(marker):
                cr.send(title)
    except GeneratorExit:
        cr.close()


def unit_adder(cr):
    next(cr)

    total = 0
    try:
        while True:
            units = yield
            try:
                total += float(units.split()[0])
            except:
                pass
    except GeneratorExit:
        cr.send('Total units: {}'.format(total))
        cr.close()


def separator(delimiter, cr1, cr2):
    next(cr1)
    next(cr2)
    try:
        while True:
            line = yield
            try:
                pos = line.rindex(delimiter)
                part1 = line[:pos].strip()
                part2 = line[pos+1:].strip()
                cr1.send(part1)
                cr2.send(part2)
            except:
                pass
    except GeneratorExit:
        cr1.close()
        cr2.close()


processor = next_line_remover(
    separator(
        ',',
        core_course_checker('*', printer()),
        unit_adder(printer())
    )
)
next(processor)

with open('course-list1.txt') as fin:
    for line in fin:
        processor.send(line)

    processor.close()
