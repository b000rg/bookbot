def get_word_count(book_text):
    return len(book_text.split())

def get_char_counts(book_text):
    char_counts = {}
    for c in book_text:
        char = c.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["num"]

def sort_counts(char_counts):
    new_list = []
    for item in char_counts:
        new_list.append({"char": item, "num": str(char_counts[item])})
    new_list.sort(reverse=True, key=sort_on)
    return new_list
