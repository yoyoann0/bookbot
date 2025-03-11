from stats import (
    count_words,
    count_characters,
    dict_list,
)
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    counted_characters = count_characters(book_text)
    list_of_dict = dict_list(counted_characters)
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for item in list_of_dict:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()