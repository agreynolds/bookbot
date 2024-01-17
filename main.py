def main():
    book_path = "books/frankenstein.txt"
    
    with open(book_path) as book:
        book_contents = book.read()

    count = word_count(book_contents)
    print(count)

def word_count(text):
    words = text.split()
    return len(words)

main()