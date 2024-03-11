def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_letters(text)
    print(chars_dict)

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


main()
