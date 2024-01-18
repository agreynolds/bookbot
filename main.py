def main():
    book_path = "books/frankenstein.txt"
    
    book_contents = read_book(book_path)

    count = word_count(book_contents)
    print(count)

def read_book(book_path):
    with open(book_path) as book:
        book_contents = book.read()
    return book_contents

def word_count(text):
    words = text.split()
    return len(words)

main()