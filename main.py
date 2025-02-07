book = "books/frankenstein.txt"

def main():
    with open(book) as f:
        file_contents = f.read()
        count = count_words(file_contents)
        d = count_chars(file_contents)
        sorted_list = list_of_d(d)
        #Print Final Report
        print(f"--- Begin report of {book} ---")
        print(f"{count} words found in the document\n")
        for item in sorted_list:
            print(f"The '{item['char']}' character was found {item['num']} times")
        print(f"--- End report ---")        

def count_words(file_contents):
    count = 0
    words = file_contents.split()
    for word in words: 
        count += 1
    return count

def count_chars(file_contents):
    lowered_file_contents = file_contents.lower()
    d = {}
    for char in lowered_file_contents:
        if char in d:
            d[char] += 1
        else:
            if char.isalpha():
                d[char] =1
    return d
    
def list_of_d(d):
        char = d.keys()
        num = d.values()
        list = [{"char": char, "num": num} for char, num in d.items()]
        list.sort(reverse=True, key=sort_on)
        return list

def sort_on(d):
    return d["num"]

main()