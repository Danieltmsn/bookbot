import sys 


from stats import word_counter, char_counter
from report import generate_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = sys.argv[1]

    generate_report(book_path)
    
if __name__ == "__main__":
    main()



