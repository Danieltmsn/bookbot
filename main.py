from stats import word_counter, char_counter
from report import generate_report


#function to read the file(to bee converted into a string later on)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
#main function
    
def main(get_book_text):
    text = get_book_text("books/frankenstein.txt")
    generate_report()
    
    



main(get_book_text)



