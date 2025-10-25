# Import Functions from stats module
import sys
from stats import get_num_words
from stats import get_char_count
from stats import sort_char_count

# Define Filepaths
if len(sys.argv) == 2:
    filepath = sys.argv [1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Read in book text
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# Main Program Logic    
def main():
    char_count = get_char_count(get_book_text(filepath))
    word_count = get_num_words(get_book_text(filepath))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sort_char_count(char_count):
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

# Entry Point    
main()