Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def count_repeated_alphabets(paragraph):
...     # Convert the paragraph to lowercase to make the comparison case-insensitive
...     paragraph = paragraph.lower()
... 
...     # Initialize a dictionary to store the count of each alphabet
...     alphabet_count = {}
... 
...     # Iterate through each character in the paragraph
...     for char in paragraph:
...         # Check if the character is an alphabet
...         if char.isalpha():
...             # Increment the count of the alphabet in the dictionary
...             alphabet_count[char] = alphabet_count.get(char, 0) + 1
... 
...     # Filter the dictionary to contain only alphabets with counts greater than 1
...     repeated_alphabets = {char: count for char, count in alphabet_count.items() if count > 1}
... 
