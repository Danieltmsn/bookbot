from stats import word_counter

with open("books/frankenstein.txt") as f:
    text = f.read()

print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
{word_counter(text)}
--------- Character Count -------
""")