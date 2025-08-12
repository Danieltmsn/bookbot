#function that finds the length of words in our book

def word_counter(text):
    words = text.split()
    amount = len(words)
    return f"{amount} words found in the document"

# 1. makes our text lowercase 
# 2. we create an empty dictionary
# 3. run a loop through our lowercase text 
# 4. loop stores and counts all characters in our dict

def char_counter(text):
    lowercase_text = text.lower()
    my_dict = {}
    for n in lowercase_text:
        if n in my_dict:
            my_dict[n] += 1
        else:
            my_dict[n] = 1
    return my_dict

def sorted_dict(my_dict):
    dict_list = []
    for key, value in my_dict.items():
        dict_list.append({"key": key, "value": value})

    dict_list.sort(key=lambda x: x["value"], reverse=True)
    return dict_list

    



