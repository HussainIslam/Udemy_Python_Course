def string_process(*args):
  return sorted([item.upper() for item in args])

print(string_process('item one', 'item two', 'item three'))