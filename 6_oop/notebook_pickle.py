import pickle
from note import Note


class Notebook:
    def __init__(self, filename, title):
        self.filename = filename
        self.title = title
        self.notes = []
        self.load()

    def load(self):
        try:
            with open(self.filename, 'rb') as fin:
                self.title = pickle.load(fin)
                #self.notes = pickle.load(fin)
                while True:
                    try:
                        self.notes.append(pickle.load(fin))
                    except EOFError:
                        break
        except FileNotFoundError:
            return None

    def save(self):
        with open(self.filename, 'wb') as fout:
            pickle.dump(self.title, fout)
            # pickle.dump(self.notes, fout)
            for note in self.notes:
                pickle.dump(note, fout)

    def add_note(self, content, category):
        self.notes.append(Note(content, category))

    def __str__(self):
        result = '{}:\n'.format(self.title)
        for index, note in enumerate(self.notes, start=1):
            result += '{}. {}\n'.format(index, note)
        return result


if __name__ == '__main__':
    nb = Notebook('john_notes.dat', "John's Notes")
    nb.add_note('Drink a lot of water', 'health')
    nb.add_note('Exercise regularly', 'health')
    nb.add_note('Always say "Hello"', 'social')
    print(nb)
    # John's Notes:
    # 1. Drink a lot of water (health)
    # 2. ...
    nb.save()
