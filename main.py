def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_letters(text)
    print_report(book_path, num_words, chars_dict)

def count_words(text):
    return len(text.split())  

def count_letters(text):
    character_count = {}

    for i in text:
        lower_char = i.lower()
        character_count[lower_char] = character_count.get(lower_char, 0) + 1
    
    return character_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, chars_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    
    sorted_chars = sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)

    for i in sorted_chars:
        if (i[0].isalpha()):
            print(f"The '{i[0]}' character was found {i[1]} times")

    print("--- End report ---")


main()
