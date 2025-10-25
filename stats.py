
def sort_on_num(item):
    return item["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    all_lower = text.lower()
    for char in all_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count  

def sort_char_count(char_count):
    list_dict_char_count = []
    
    for char in char_count:
        list_dict_char_count.append({"char" : char, "num" : char_count[char]})
    
    list_dict_char_count.sort(key=sort_on_num,  reverse=True)
    
    return list_dict_char_count   
