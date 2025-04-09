def get_book_text(filepath):
    frankenstein_book_string = ""

    with open(filepath) as book:
        frankenstein_book_string = book.read()
        return frankenstein_book_string


def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)

    return num_words


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")
    print(book_text)

main()
