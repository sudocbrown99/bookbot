def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  chars_dict = get_chars_dict(text)
  print(num_words, "words found in the document")

from stats import get_num_words

from stats import get_book_text

from stats import get_chars_dict
main()
