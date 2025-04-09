def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)

    return num_words


def get_chars_appear(book_text):
    lower_case_chars = book_text.lower()
    num_chars = {}

    for char in lower_case_chars:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1

    return num_chars
