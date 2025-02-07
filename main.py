def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_set = count_chars(file_contents)
        print(char_set)

def count_words(file_contents):
    count = 0
    words = file_contents.split()
    for word in words: 
        count += 1
    return count

def count_chars(file_contents):
    lowered_file_contents = file_contents.lower()
    dict = {}
    for char in lowered_file_contents:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict
    
main()