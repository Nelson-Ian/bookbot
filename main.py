
def main():                                 # prints the file contents
    book_path = "books/frankenstein.txt"    # give the program a path to follow
    text = get_book_text(book_path)         # Call function to retrieve text from .txt file
    print(text)                             # print the text to the console
    print("Word count:" )
    print(word_count(book_path))            # print word count using word_count function
    print("Instances of each letter:" )
    print(letter_counter(book_path))
    instance_sort(letter_counter(book_path))


def get_book_text(path):    # returns string of the text 
    with open(path) as f:   # open() file defaults to read mode
        return f.read()     # returns the text to the main function where it is printed.

def word_count(path):                       
    txt_string = list(get_book_text(path).split())  # book as string, split string, assign each word to a list
    return len(txt_string)                          # feed length of list to main() to print

def letter_counter(path):                                       # function to count instances of each letter
    letter_count = {}                                           # create dict for storing letter counts
    lower_case = get_book_text(path).lower()                    # convert entire text to lowercase
    for letter in lower_case:                                   # iterate over all letters of text
        if letter in letter_count: letter_count[letter] += 1    # +1 to dict value of each letter 
        else: letter_count[letter] = 1                          # add letter to dict if not already there
    return letter_count                                         # return dictionary with count of each letter

def instance_sort(counts):
    dict_list = []                          # create empty list for list of dictionaries
    for key, value in counts.items():       # looking at the key and calue for each dictionary entry
        if key.isalpha():                   # eliminating non-alphabetical keys
            dict_list.append({key : value}) # add alpha keys an dtheir values to list as dictionary
    list_sort = []                          # Gotta figure out how to sort it
    


main()