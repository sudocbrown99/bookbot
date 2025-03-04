import sys
from stats import get_num_words, get_book_text, get_chars_dict, sort_chars

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  book_path = sys.argv[1]

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
main()
