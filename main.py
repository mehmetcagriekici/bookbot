import sys

from stats import get_char_count, get_number_of_words

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_link = sys.argv[1]
    book_text = get_book_text(book_link)

    word_count = get_number_of_words(book_text)
    char_count = get_char_count(book_text)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_link}...\n----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------\n{char_count}")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

main()
