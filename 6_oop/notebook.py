from note import Note


class Notebook:
    def __init__(self, filename, title):
        self.filename = filename
        self.title = title
        self.notes = []
        self.load()

    def load(self):
        try:
            with open(self.filename) as fin:
                for index, line in enumerate(fin):
                    line = line.strip()
                    if index == 0:
                        self.title = line
                    else:
                        left = line.rindex('(')
                        right = line.rindex(')')
                        content = line[:left]
                        category = line[left+1:right]
                        self.add_note(content.strip(), category.strip())
        except FileNotFoundError:
            pass


    def save(self):
        with open(self.filename, 'w') as fout:
            fout.write('{}\n'.format(self.title))
            for note in self.notes:
                fout.write('{}\n'.format(note))

    def add_note(self, content, category):
        self.notes.append(Note(content, category))

    def __str__(self):
        result = '{}:\n'.format(self.title)
        for index, note in enumerate(self.notes, start=1):
            result += '{}. {}\n'.format(index, note)
        return result


if __name__ == '__main__':
    nb = Notebook('john_notes.txt', "John's Notes")
    nb.add_note('Drink a lot of water', 'health')
    nb.add_note('Exercise regularly', 'health')
    nb.add_note('Always say "Hello"', 'social')
    print(nb)
    # John's Notes:
    # 1. Drink a lot of water (health)
    # 2. ...
    nb.save()
