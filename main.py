def get_book_text(filepath):
    frankenstein_book_string = ""

    with open(filepath) as book:
        frankenstein_book_string = book.read()
        return frankenstein_book_string


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(file_contents)


main()
