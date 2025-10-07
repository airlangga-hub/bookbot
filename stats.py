def count_words(words):
    return len(words.split())

def count_char(words):
    counter = {}
    for char in words:
        char = char.lower()
        counter[char] = counter.get(char, 0) + 1
    return counter

def sort_dic(dic):
    sort_ = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    # print(dic.items())
    # print(sort_)
    print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------""")
    for key, value in sort_:
        if key.isalpha():
            print(f"{key}: {value}")
    print("""============= END ===============""")