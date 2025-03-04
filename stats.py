def get_num_words(text):
  words = text.split()
  return len(words)

def get_book_text(path):
  with open(path) as f:
    content = f.read()
    return content

def get_chars_dict(text):
  chars = {}
  for c in text:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def sort_chars(chars_dict):
  chars_list = []
  for char, count in chars_dict.items():
    if char.isalpha():
      chars_list.append({"char": char, "count": count})
  
  chars_list.sort(reverse=True, key=lambda x: x["count"])

  return chars_list