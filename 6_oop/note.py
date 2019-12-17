class Note:
    def __init__(self, content, category):
        self.content = content
        self.category = category

    def __str__(self):
        return '{} ({})'.format(self.content, self.category)


if __name__ == '__main__':
    n1 = Note('Drink a lot of water', 'health')
    n2 = Note('Exercise regularly', 'health')
    n3 = Note('Always say "Hello"', 'social')
    print(n1)  # Drink a lot of water (health)
    print(n2)
    print(n3)
