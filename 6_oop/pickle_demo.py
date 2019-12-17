import pickle

with open('test.dat', 'ab+') as fout:
    pickle.dump([1, 2, 3], fout)
    pickle.dump({1: 'hello world', 2: 'bye'}, fout)
    pickle.dump(100, fout)

with open('test.dat', 'rb') as fin:
    while True:
        try:
            curr = pickle.load(fin)
            print(curr)
        except EOFError:
            break
