import sys
from stats import (
    get_num_words,
    get_chars_appear,
    sort_chars,
)


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    frankenstein_book_string = ""

    with open(filepath) as book:
        frankenstein_book_string = book.read()
        return frankenstein_book_string


def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_chars_dict = get_chars_appear(book_text)
    sorted_list = sort_chars(num_chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")
    # print(book_text)


main()
