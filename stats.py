def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    counted_characters = {}
    for char in text:
        char = char.lower()
        if char not in counted_characters:
            counted_characters[char] = 1
        else:
            counted_characters[char] += 1
    return counted_characters

def sorting(item):
    return item["count"]

def dict_list(counted_characters):
    list_of_dict = []
    for char in counted_characters:
        list_of_dict.append({"char": char, "count": counted_characters[char]})
    list_of_dict.sort(key=sorting, reverse=True)
    return list_of_dict