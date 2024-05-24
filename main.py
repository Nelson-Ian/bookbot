
def main():                                 # prints the file contents
    book_path = "books/frankenstein.txt"    # give the program a path to follow
    text = get_book_text(book_path)         # Call function to retrieve text from .txt file
    print(text)                             # print the text to the console
    print("Word count:" )
    print(word_count(book_path))            # print word count using word_count function
    print("Instances of each letter:" )
    print(letter_counter(book_path))


def get_book_text(path):    # returns string of the text 
    with open(path) as f:   # open() file defaults to read mode
        return f.read()     # returns the text to the main function where it is printed.

def word_count(path):                       
    txt_string = list(get_book_text(path).split())  # book as string, split string, assign each word to a list
    return len(txt_string)                          # feed length of list to main() to print

def letter_counter(path):
    letter_count = {

    }
    lower_case = get_book_text(path).lower()
    for letter in lower_case:
        if letter in letter_count: letter_count[letter] += 1
        else: letter_count[letter] = 1
    return letter_count

main()