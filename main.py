def main():
    book_path = "books/frankenstein.txt"
    
    book_contents = read_book(book_path)

    word_count = count_words(book_contents)
    print(f"{book_path} has {word_count} words.")
    print("---------")
    letter_count = count_letters(book_contents)
    for key in letter_count:
        if letter_count[key] == 1:
            print(f"{book_path} has {letter_count[key]} {key} character.")
        else: 
            print(f"{book_path} has {letter_count[key]} {key} characters.")


def read_book(book_path):
    with open(book_path) as book:
        book_contents = book.read()
    return book_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    letter_dictionary = {}
    for char in text:
        if char in letter_dictionary:
            letter_dictionary[char] += 1
        else: 
            letter_dictionary[char] = 1
    return letter_dictionary        

main()
