def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(num_words)

def count_words(text):
    return len(text.split())  

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
