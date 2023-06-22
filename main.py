def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

input_string = input("Введите строку: ")
if is_palindrome(input_string):
    print("True")
else:
    print("False")

