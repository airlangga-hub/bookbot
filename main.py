from stats import count_char, sort_dic
from sys import argv, exit

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def main():
    # filepath = "./books/frankenstein.txt"
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
        return
    content = get_book_text(argv[1])
    # n_words = count_words(content)
    # print(f"Found {n_words} total words")
    char_count = count_char(content)
    # print(char_count)
    sort_dic(char_count)
    # print(sort_)

if __name__ == "__main__":
    main()