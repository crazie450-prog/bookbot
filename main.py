# Import Functions from stats module
from stats import get_num_words
from stats import get_char_count
from stats import sort_char_count

# Define Filepaths
frankenstein_filepath = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


    
def main():
    char_count = get_char_count(get_book_text(frankenstein_filepath))
    
    #print(f"Found {get_num_words(get_book_text(frankenstein_filepath))} total words.")
    #print(char_count)
    
    print(sort_char_count(char_count))
    
    
main()