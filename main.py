def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  chars_dict = get_chars_dict(text)
  sorted_list = sort_chars(chars_dict)
  print(
    f"============ BOOKBOT ============\n"
    f"Analyzing book found at {book_path}..."
    )
  print(
    f"----------- Word Count ----------\n"
    f"Found {num_words} total words"
    )
  print(f"--------- Character Count -------\n")
  for char_dict in sorted_list:
    print(f"{char_dict['char']}: {char_dict['count']}")
  print("============= END ===============")

from stats import get_num_words

from stats import get_book_text

from stats import get_chars_dict

from stats import sort_chars
main()
