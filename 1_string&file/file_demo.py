# fd = open('names.txt', 'w')
#
# fd.write('Alice\n')
# fd.write('Bob\n')
# fd.write('Charles\n')
# fd.write('David\n')
#
# fd.close()
#
# fin = open('names.txt')
#
# line = fin.readline()
# while line:
#     name = line.strip()
#     print(name)
#     print(len(name))
#     line = fin.readline()
#
# fin.close()

with open('names.txt', 'w') as fd:
    fd.write('Alice\n')
    fd.write('Bob\n')
    fd.write('Charles\n')
    fd.write('David\n')

with open('names.txt', 'r') as fin:
    for line in fin:
        name = line.strip()
        print(name)

with open('names.txt') as fin, open('names_upper.txt', 'w') as fout:
    for line in fin:
        name = line.strip()
        fout.write('{}\n'.format(name.upper()))
