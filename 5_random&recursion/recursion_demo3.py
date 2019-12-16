def replace_all(sentence, target, replacement):
    if target not in sentence:
        # base case
        return sentence

    pos = sentence.index(target)
    prefix = sentence[:pos]
    suffix = sentence[pos + len(target):]

    return prefix + replacement + replace_all(suffix, target, replacement)


print(replace_all('to be or not to be', 'to', '2'))  # 2 to or not 2 be
print(replace_all('gogogo', 'go', 'gone'))  # gonegonegone
print(replace_all('aaaaa', 'aaa', 'b'))  #baa
print(replace_all('advanced calculus', 'math', 'science'))  # advanced calculus
