def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    counted_characters = count_letters(text)
    counted_letters = only_letters(counted_characters)
    sorted_letters = sort_by_count(counted_letters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in document")
    for letter in sorted_letters:
        char = letter["letter"]
        count = letter["count"]
        print(f"The {char} character was found {count} times")
    print("--- End report ---")


def sort_by_count(counted_letters: dict):
    def sort_on(dict):
        return dict["count"]
    sorted = []
    for letter in counted_letters:
        sorted.append({"letter": letter, "count": counted_letters[letter]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted


def only_letters(counted_chars: dict):
    letters = {}
    for c in counted_chars:
        if c.isalpha():
            letters[c] = counted_chars[c]
    return letters


def count_letters(text: str):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered not in characters:
            characters[lowered] = 0
        characters[lowered] += 1
    return characters


def count_words(text: str):
    words = text.split()
    return len(words)


def get_book_text(path: str):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


main()
