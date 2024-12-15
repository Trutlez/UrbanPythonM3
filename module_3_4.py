# Задача "Однокоренные"

def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if str(root_word).lower().count(str(word).lower()) > 0:
            same_words.append(word)
        elif str(root_word).lower() in (str(word).lower()):
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

result3 = single_root_words(7, 'z7', 'seven', 'good luck - 73' )
print(result3)