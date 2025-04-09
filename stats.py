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


def sort_on(dictionary):
    return dictionary["count"]


def sort_chars(num_chars):
    sorted_list = []

    for char in num_chars:
        sorted_list.append({"char": char, "count": num_chars[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
