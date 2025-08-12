from stats import word_counter,char_counter,sorted_dict

def generate_report():
    with open("books/frankenstein.txt") as f:
        text = f.read()

    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
{word_counter(text)}
--------- Character Count -------""")

    char_counts = char_counter(text)
    sorted_chars = sorted_dict(char_counts)

    for item in sorted_chars:
        print(f"{item['key']}: {item['value']}")
    print("============= END ===============")

if __name__ == "__main__":
    generate_report()
