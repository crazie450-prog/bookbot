# Import Functions from stats module
import sys
from stats import get_num_words
from stats import get_char_count
from stats import sort_char_count

# Define Filepaths
if len(sys.argv) == 2:
    frankenstein_filepath = sys.argv [1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    char_count = get_char_count(get_book_text(frankenstein_filepath))
    word_count = get_num_words(get_book_text(frankenstein_filepath))
    #print(f"Found {get_num_words(get_book_text(frankenstein_filepath))} total words.")
    #print(char_count)
    #print(sort_char_count(char_count))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {frankenstein_filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sort_char_count(char_count):
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
    
main()