from stats import get_num_words, get_chars_appear


def get_book_text(filepath):
    frankenstein_book_string = ""

    with open(filepath) as book:
        frankenstein_book_string = book.read()
        return frankenstein_book_string


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    num_chars = get_chars_appear(book_text)
    print(f"{num_words} words found in the document")
    print(num_chars)
    # print(book_text)


main()
