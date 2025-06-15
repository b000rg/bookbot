import sys
from stats import get_word_count
from stats import get_char_counts
from stats import sort_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(filepath, word_count, char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for c in char_counts:
        if c["char"].isalpha():
            print(c["char"] + ": " + c["num"])
    print("============= END ===============")

def main():
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)
    char_counts = get_char_counts(book_text)
    print_report(filepath, word_count, sort_counts(char_counts))

main()
