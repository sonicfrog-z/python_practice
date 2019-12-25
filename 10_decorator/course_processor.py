def printer():
    try:
        while True:
            line = yield
            print(line)
    except GeneratorExit:
        pass

    print('printer done')


def next_line_remover(next_cr):
    next(next_cr)
    try:
        while True:
            line = yield
            line = line.strip()
            next_cr.send(line)
    except GeneratorExit:
        pass

    print('next_line_remover done')
    next_cr.close()


processor = next_line_remover(printer())
next(processor)

with open('course-list1.txt') as fin:
    for line in fin:
        processor.send(line)

    processor.close()
