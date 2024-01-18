def main():
    book_path = "books/frankenstein.txt"
    book_contents = read_book(book_path)
    word_count = count_words(book_contents)
    letter_count = count_letters(book_contents)
    sorted_letters = sort_letters(letter_count)


    print("\n")
    print("=============================================")
    print(f"=== Book Report of {book_path} ===")
    print("=============================================")
    print("\n")
    print("---------------- Word Count -----------------")
    print(f"{word_count} words found in the document")
    print("\n")
    print("--------------- Letter Count ----------------")
    print_letter_counts(sorted_letters)

      


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

def sort_letters(letter_count):
    letters = []
    for letter in letter_count:
        if letter.isalpha():
            letter_tuple = (letter_count[letter], letter)
            letters.append(letter_tuple)
    letters.sort(reverse = True)
    return letters

def print_letter_counts(sorted_letters):
    for letter in sorted_letters:
        print(f"The letter \'{letter[1]}\' was found in the document {letter[0]}")

main()
