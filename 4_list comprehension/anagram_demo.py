def form_anagram(fd):
    anagram_dict = {}

    for line in fd:
        word = line.strip()
        signature = ''.join(sorted(word))
        anagram_dict.setdefault(signature, [])
        anagram_dict[signature].append(word)

    return list(anagram_dict.values())


def get_top_anagrams(anagram_list, rank):
    return sorted(anagram_list, key=len, reverse=True)[:rank]


with open('words.txt') as fin:
    result = form_anagram(fin)
    print(get_top_anagrams(result, 5))
